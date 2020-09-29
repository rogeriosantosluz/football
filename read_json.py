import json
import os 

ROOT_DIR = "/Users/rogerioluz/Documents/football/transfermarkt-scrapper/files/"
for file_name in os.listdir(ROOT_DIR):
    print("###########################-----------------")
    print("CAMPEONATO: {}".format(file_name))
    print("###########################-----------------")
    # read file
    with open(ROOT_DIR + file_name, 'r') as myfile:
        data=myfile.read()

    # parse file
    obj = json.loads(data)

    print("###########################-----------------")
    print("PAIS: {}".format(obj.get("nation")))
    print("###########################-----------------")

    for club in obj.get("clubs"):
        print("-----------------")
        print(club.get("name"))
        print("-----------------")
        players = club.get("players")
        for i in players:
            print("{} - {} ({}) - {}".format(i.get("number"), i.get("name"), i.get("position"), i.get("nation")) )