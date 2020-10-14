import requests
import json
import time
from bs4 import BeautifulSoup

ROOT_DIR = "/Users/rogerioluz/Documents/football/files/"
BASE_URL = 'https://www.transfermarkt.com.br'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) \
                   AppleWebKit/537.36 (KHTML, like Gecko) \
                   Chrome/47.0.2526.106 Safari/537.36'
}

page = 'https://www.transfermarkt.com.br/wettbewerbe/europa'


def make_request(pageUrl):
    pageTree = requests.get(pageUrl, headers=headers)
    pageSoup = BeautifulSoup(pageTree.content, 'html.parser')

    return pageSoup

def extract_league_urls(pageSoup):
    urlSoup = pageSoup.find_all('table', {'class': 'inline-table'})
    leagueUrls = []

    for url in urlSoup:
        leagueUrls.append(
            BASE_URL + url.find_all('td')[1].find('a')['href']
        )

    return leagueUrls
    
def extract_club_urls(pageSoup):
    urlSoup = pageSoup.find('table', {'class': 'items'}).find_all('a', {'class': 'vereinprofil_tooltip'})
    clubUrls = set()

    for url in urlSoup:
        clubUrls.add(
            BASE_URL + url['href']
        )

    return clubUrls

def extract_players_info(pageSoup):
    playerSoup = pageSoup.find_all('tr', {'class': ['odd', 'even']})
    playersInfo = []

    for player in playerSoup:
        playersInfo.append({
            'name': player.find_all('a', {'class': 'spielprofil_tooltip'})[0].text,
            'position': player.find_all('td')[4].text,
            'number' : player.find_all('div', {'class': 'rn_nummer'})[0].text,
            'market_value': player.find_all('td', {'class': 'rechts hauptlink'})[0].text.split('€')[0] + '€', 
            'age': player.find_all('td', {'class': 'zentriert'})[1].text.split(' ')[1].replace('(', '').replace(')', ''),
            'date_of_birth': player.find_all('td', {'class': 'zentriert'})[1].text.split(' ')[0],
            'nation': player.find_all('img', {'class': 'flaggenrahmen'})[0]['title'],
            'contract_expires': player.find_all('td', {'class': 'zentriert'})[3].text.replace('.', '/')
        })
    
    return playersInfo

def extract_manager_info(pageSoup):
    managerSoup = pageSoup.find('div', {'class': 'container-inhalt'})

    confuseString = managerSoup.find('div', {'class': 'container-zusatzinfo'}).text

    age, since, contractExpires = 0,0,0
 
    confuseString = confuseString.split(':')
 
    if len(confuseString) > 3:
        age = confuseString[1].split(' ')[1]
        since = confuseString[2].split('\t')[0].replace(' ', '')
        contractExpires = confuseString[3].split('\t')[0].replace(' ', '').replace('.', '/')

    managerInfo = {
        'name': managerSoup.find('a').text,
        'nation': managerSoup.find('img')['alt'],
        'age': age,
        'contract_expires': contractExpires,
        'since': since,
    }

    return managerInfo

def extract_club_info(pageSoup):
    clubSoup = pageSoup.find_all('span', {'class': 'dataValue'})

    clubInfo = {
        'name': pageSoup.find('h1').text.replace('\n', '').replace(' ', ''),
        'amount_of_players': clubSoup[0].text.replace('\n', '').replace(' ', ''),
        'media_age': clubSoup[1].text.replace('\n', '').replace(' ', ''),
        'market_value': pageSoup.find('div', {'class': 'dataMarktwert'}).find('a').text.replace(' Valor de mercado total', ''),
        'manager': extract_manager_info(pageSoup)
    }

    detailPageUrl = BASE_URL + pageSoup.find('div', {'class': 'table-footer'}).find('a')['href']
    detailSoup = make_request(detailPageUrl)

    print('CLUB -> ', clubInfo['name'])
    clubInfo['players'] = extract_players_info(detailSoup)

    return clubInfo

def extract_league_info(pageSoup):
    profilheader = pageSoup.find_all('table', {'class': 'profilheader'})
    leagueSoup = profilheader[0].find_all('td')

    leagueInfo = {
        'name': pageSoup.find('h1', {'class': 'spielername-profil'}).text,
        'nation': leagueSoup[0].find('img')['alt'],
        'amount_of_clubs': leagueSoup[1].text.replace('\n', '').replace(' ', '').replace('Equipas', ''),
        'amount_of_players': leagueSoup[2].text.replace('\n', '').replace(' ', ''),
        'market_value': pageSoup.find('div', {'class': 'marktwert'}).find('a').text
    }

    clubUrls = extract_club_urls(pageSoup)
    clubsInfo = []

    n = len(clubUrls)
    i = 0
    print('\n\n\nLEAGUE -> ', leagueInfo['name'], '\n')
    print('0 of ', n, 'CLUBS scrapped')
    for url in clubUrls:
        clubsInfo.append(
            extract_club_info(
                make_request(url)
            )
        )
        i += 1
        print(i, ' of ', n, 'CLUBS scrapped')
        time.sleep(5)

    leagueInfo['clubs'] = clubsInfo

    return leagueInfo['name'], leagueInfo

if __name__ == "__main__":
    print('\n\nInicializando...\n\n')
    #baseSoup = make_request(page)
    #leagueUrls = extract_league_urls(baseSoup)
    #print(leagueUrls)
    
    leagueUrls = [
        'https://www.transfermarkt.com.br/premier-league/startseite/wettbewerb/GB1',
        'https://www.transfermarkt.com.br/national-league/startseite/wettbewerb/CNAT',
        'https://www.transfermarkt.com.br/superliga/startseite/wettbewerb/AR1N',
        'https://www.transfermarkt.com.br/primera-division-de-chile/startseite/wettbewerb/CLPD',
        'https://www.transfermarkt.com.br/liga-dimayor-i/startseite/wettbewerb/COLP',
        'https://www.transfermarkt.com.br/ligapro-serie-a-primera-etapa/startseite/wettbewerb/EL1A',
        'https://www.transfermarkt.com.br/major-league-soccer/startseite/wettbewerb/MLS1',
        'https://www.transfermarkt.com.br/j1-league/startseite/wettbewerb/JAP1',
        'https://www.transfermarkt.com.br/liga-mx-apertura/startseite/wettbewerb/MEXA',
        'https://www.transfermarkt.com.br/primera-division-apertura/startseite/wettbewerb/PR1A',
        'https://www.transfermarkt.com.br/liga-1-apertura/startseite/wettbewerb/TDeA',
        'https://www.transfermarkt.com.br/premier-liga/startseite/wettbewerb/RU1',
        'https://www.transfermarkt.com.br/primera-division-apertura/startseite/wettbewerb/URU1',
        'https://www.transfermarkt.com.br/torneo-apertura/startseite/wettbewerb/VZ1A'
    ] 
    """
        'https://www.transfermarkt.com.br/serie-a/startseite/wettbewerb/IT1', 
        'https://www.transfermarkt.com.br/1-bundesliga/startseite/wettbewerb/L1', 
        'https://www.transfermarkt.com.br/ligue-1/startseite/wettbewerb/FR1', 
        'https://www.transfermarkt.com.br/liga-nos/startseite/wettbewerb/PO1', 
        'https://www.transfermarkt.com.br/premier-liga/startseite/wettbewerb/RU1', 
        'https://www.transfermarkt.com.br/eredivisie/startseite/wettbewerb/NL1', 
        'https://www.transfermarkt.com.br/jupiler-pro-league/startseite/wettbewerb/BE1', 
        'https://www.transfermarkt.com.br/super-lig/startseite/wettbewerb/TR1', 
        'https://www.transfermarkt.com.br/premier-liga/startseite/wettbewerb/UKR1', 
        'https://www.transfermarkt.com.br/bundesliga/startseite/wettbewerb/A1', 
        'https://www.transfermarkt.com.br/super-league-1/startseite/wettbewerb/GR1', 
        'https://www.transfermarkt.com.br/scottish-premiership/startseite/wettbewerb/SC1', 
        'https://www.transfermarkt.com.br/super-league/startseite/wettbewerb/C1', 
        'https://www.transfermarkt.com.br/fortuna-liga/startseite/wettbewerb/TS1', 
        'https://www.transfermarkt.com.br/super-liga-srbije/startseite/wettbewerb/SER1', 
        'https://www.transfermarkt.com.br/superligaen/startseite/wettbewerb/DK1', 
        'https://www.transfermarkt.com.br/pko-ekstraklasa/startseite/wettbewerb/PL1', 
        'https://www.transfermarkt.com.br/liga-1/startseite/wettbewerb/RO1', 
        'https://www.transfermarkt.com.br/1-hnl/startseite/wettbewerb/KR1', 
        'https://www.transfermarkt.com.br/allsvenskan/startseite/wettbewerb/SE1', 
        'https://www.transfermarkt.com.br/eliteserien/startseite/wettbewerb/NO1', 
        'https://www.transfermarkt.com.br/protathlima-cyta/startseite/wettbewerb/ZYP1', 
        'https://www.transfermarkt.com.br/ligat-haal/startseite/wettbewerb/ISR1',
        'https://www.transfermarkt.com.br/premier-league/startseite/wettbewerb/GB1', 
        'https://www.transfermarkt.com.br/laliga/startseite/wettbewerb/ES1'
    ]
        'https://www.transfermarkt.com.br/serie-b/startseite/wettbewerb/BRA2',
    """

    n = len(leagueUrls)
    i = 0
    print('0 of ', n, 'LEAGUES scrapped')
    for leagueUrl in leagueUrls:
        leagueSoup = make_request(leagueUrl)

        nome, info = extract_league_info(leagueSoup)

        i += 1
        print('\n\n', i, ' of ', n, 'LEAGUES scrapped')

        time.sleep(5)

        with open(ROOT_DIR + "/{}.json".format(nome), 'w') as json_file:  
            json.dump(info, json_file)