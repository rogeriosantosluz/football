#!/usr/bin/env python
# -*- coding: latin-1 -*-

import random
import time

atributos = {
    "expectativa": {
        5: {"nome": "Campeão", "comentario": "A equipe do {} tem a expectativa de ser campeão do torneio"},
        4: {"nome": "Ficar entre os 4", "comentario": "A equipe do {} pretende ficar entre os 4 primeiros do torneio"},
        3: {"nome": "Ficar entre os 8", "comentario": "A equipe do {} pretende ficar entre os 8 primeiros do torneio"},
        2: {"nome": "Não rebaixar", "comentario": "A equipe do {} pretende não ser rebaixada no torneio"},
        1: {"nome": "Cumprir tabela", "comentario": "A equipe do {} apenas cumpre tabela no torneio"}
    },
    "mentalidade" : {
        5: {"nome": "Vencer a qualquer custo", "comentario": "A equipe do {} veio para vencer a qualquer custo"},
        4: {"nome": "Vencer", "comentario": "A equipe do {} quer vencer"},
        3: {"nome": "Empatar", "comentario": "A equipe do {} veio para arrancar o empate"},
        2: {"nome": "Não perder", "comentario": "A equipe do {} vai vender caro a derrota"},
        1: {"nome": "Perder de pouco", "comentario": "A equipe do {} se segura como pode"}
    },
    "forma" : {
        5: {"nome": "Melhor forma", "comentario": "A equipe do {} está em sua melhor forma"},
        4: {"nome": "Boa", "comentario": "A equipe do {} está em boa forma"}, 
        3: {"nome": "Regular", "comentario": "A equipe do {} está em forma"},
        2: {"nome": "Baixa", "comentario": "A equipe do {} está em má forma"},
        1: {"nome": "Péssima", "comentario": "A equipe do {} está em péssima forma"}
    },
    "moral" : {
        5: {"nome": "Moral alta", "comentario": "A equipe do {} está com a moral alta"},
        4: {"nome": "Moral boa", "comentario": "A equipe do {} está com a moral boa"}, 
        3: {"nome": "Moral", "comentario": "A equipe do {} está com moral"},
        2: {"nome": "Moral baixa", "comentario": "A equipe do {} está com moral baixa"},
        1: {"nome": "Nenhuma moral", "comentario": "A equipe do {} está sem moral"}
    },
    "formacao": {
        5: {"nome": "4-2-4", "comentario": "A equipe do {} está em um 4-2-4 ultra ofensivo"},
        4: {"nome": "4-3-3", "comentario": "A equipe do {} está em um 4-3-3 ofensivo"},
        3: {"nome": "3-6-1", "comentario": "A equipe do {} está em um 3-6-1 dominando o meio-campo"},
        2: {"nome": "5-3-1", "comentario": "A equipe do {} está em um 5-3-2 defensivo"},
        1: {"nome": "5-5-0", "comentario": "A equipe do {} está em um 5-5-0 ultra defensivo"}
    }
}

equipe_da_casa = {
    "nome": "Santos FC",
    "valor_mercado_em_milhoes": 46,
    "expectativa": random.choice(list(atributos.get("expectativa").keys())),
    "maior_expectativa": False,
    "mentalidade": random.choice(list(atributos.get("mentalidade").keys())),
    "melhor_mentalidade": False,
    "moral": random.choice(list(atributos.get("moral").keys())),
    "melhor_moral": False,
    "forma": random.choice(list(atributos.get("forma").keys())),
    "melhor_forma": False,
    "formacao": random.choice(list(atributos.get("formacao").keys())),
    "melhor_formacao": False,
    "favoritismo": 0,
    "favorito": False,
    "gols": 0
}

equipe_visitante = {
    "nome": "Palmeiras",
    "valor_mercado_em_milhoes": 104,
    "expectativa": random.choice(list(atributos.get("expectativa").keys())),
    "maior_expectativa": False,
    "mentalidade": random.choice(list(atributos.get("mentalidade").keys())),
    "melhor_mentalidade": False,
    "moral": random.choice(list(atributos.get("moral").keys())),
    "melhor_moral": False,
    "forma": random.choice(list(atributos.get("forma").keys())),
    "melhor_forma": False,
    "formacao": random.choice(list(atributos.get("formacao").keys())),
    "melhor_formacao": False,
    "favoritismo": 0,
    "favorito": False,
    "gols": 0
}

def print_equipes(equipe_da_casa, equipe_visitante):
    for k,v in equipe_da_casa.items():
        print("{} - {}".format(k, v))

    print("-----------")

    for k,v in equipe_visitante.items():
        print("{} - {}".format(k, v))

    print("-----------")

def calcula_favorito(equipe_da_casa, equipe_visitante):
    equipe_da_casa["favoritismo"] = equipe_da_casa.get("expectativa") + equipe_da_casa.get("mentalidade") + equipe_da_casa.get("moral") + equipe_da_casa.get("forma") + equipe_da_casa.get("formacao") + (equipe_da_casa.get("valor_mercado_em_milhoes")/20)
    equipe_visitante["favoritismo"] = equipe_visitante.get("expectativa") + equipe_visitante.get("mentalidade") + equipe_visitante.get("moral") + equipe_da_casa.get("forma") + equipe_da_casa.get("formacao") + (equipe_visitante.get("valor_mercado_em_milhoes")/20)

    if equipe_da_casa.get("expectativa") >= equipe_visitante.get("expectativa"):
        equipe_da_casa["maior_expectativa"] = True
    else:
        equipe_visitante["maior_expectativa"] = True

    if equipe_da_casa.get("mentalidade") >= equipe_visitante.get("mentalidade"):
        equipe_da_casa["melhor_mentalidade"] = True
    else:
        equipe_visitante["melhor_mentalidade"] = True

    if equipe_da_casa.get("moral") >= equipe_visitante.get("moral"):
        equipe_da_casa["melhor_moral"] = True
    else:
        equipe_visitante["melhor_moral"] = True

    if equipe_da_casa.get("forma") >= equipe_visitante.get("forma"):
        equipe_da_casa["melhor_forma"] = True
    else:
        equipe_visitante["melhor_forma"] = True

    if equipe_da_casa.get("formacao") >= equipe_visitante.get("formacao"):
        equipe_da_casa["melhor_formacao"] = True
    else:
        equipe_visitante["melhor_formacao"] = True

    if equipe_da_casa["favoritismo"] >= equipe_visitante["favoritismo"]:
        equipe_da_casa["favorito"] = True
        return equipe_da_casa, equipe_visitante
    else:
        equipe_visitante["favorito"] = True
        return equipe_visitante, equipe_da_casa

def comentarios_aleatorios_positivos(jogo):
    tipo_comentario = {
        "maior_expectativa": "expectativa",
        "melhor_mentalidade": "mentalidade",
        "melhor_moral": "moral",
        "melhor_forma": "forma",
        "melhor_formacao": "formacao"
    }
    
    k, v = random.choice(list(tipo_comentario.items()))
    #print(k, v)
    if jogo["equipe_da_casa"].get(k):
        print(atributos.get(v).get(jogo["equipe_da_casa"].get(v)).get("comentario").format(jogo["equipe_da_casa"].get("nome")))
    else:
        print(atributos.get(v).get(jogo["equipe_visitante"].get(v)).get("comentario").format(jogo["equipe_visitante"].get("nome")))

def gol(jogo):
    chance_gol_pelo_favoritismo = dict()
    for i in range(0,90):
        chance_gol_pelo_favoritismo[i] = (["gol"]*i)+([""]*(90-i))
    #print(jogo["favoritismo"])
    #print(chance_gol_pelo_favoritismo)
    fav = chance_gol_pelo_favoritismo.get(round(abs(int(jogo["favoritismo"]))))
    #print(fav)
    choice = random.choice(fav)
    #print(choice)
    return choice

    #import numpy as np

    #keys, weights = zip(*chance_gol_pelo_favoritimos.items())
    #probs = np.array(weights, dtype=float) / float(sum(weights))
    #sample_np = np.random.choice(keys, 2, p=probs)
    #sample = [str(val) for val in sample_np]
    #print(sample)



def bola_rolando(jogo):
    if jogo["minuto"] <= 45:
        print("1º Tempo {} minutos".format(jogo["minuto"]))
    else:
        print("2º Tempo {} minutos".format(jogo["minuto"]))

    try:
        comentarios_aleatorios_positivos(jogo)
    except Exception as inst:
        print_equipes(jogo["equipe_da_casa"], jogo["equipe_visitante"])
        raise inst
    

    g = gol(jogo)
    if g == "gol":
        if jogo["favoritismo"] >= 0:
            fav_pos = int(100/2+jogo["favoritismo"]*1)
            fav_neg = int(100/2-jogo["favoritismo"]*1)
        else:
            fav_pos = int(100/2-jogo["favoritismo"]*1)
            fav_neg = int(100/2+jogo["favoritismo"]*1)      

        chance_gol = [jogo["favorito"]["nome"]]*fav_pos + [jogo["nao_favorito"]["nome"]]*fav_neg
        #print(chance_gol)
        nome = random.choice(chance_gol)

        print("#"*50)
        print("GOOOOOOOOOL do {} !!!".format(nome))
        print("#"*50)

        #GOL DIMINUI O AUMENTA A MORAL, A FORMACAO E A MENTALIDADE
        if jogo["equipe_da_casa"]["nome"] == nome:
            jogo["equipe_da_casa"]["gols"] += 1
            if jogo["equipe_da_casa"]["moral"] < 5:
                jogo["equipe_da_casa"]["moral"] += 1
            if jogo["equipe_visitante"]["moral"] > 1:
                jogo["equipe_visitante"]["moral"] -= 1
            if jogo["equipe_visitante"]["mentalidade"] < 5:
                jogo["equipe_visitante"]["mentalidade"] +=1
        else:
            jogo["equipe_visitante"]["gols"] += 1
            if jogo["equipe_da_casa"]["moral"] > 1:
                jogo["equipe_da_casa"]["moral"] -= 1
            if jogo["equipe_visitante"]["moral"] < 5:
                jogo["equipe_visitante"]["moral"] += 1
            if jogo["equipe_da_casa"]["mentalidade"] < 5:
                jogo["equipe_da_casa"]["mentalidade"] +=1

        placar(jogo["equipe_da_casa"], jogo["equipe_visitante"])

    if jogo["minuto"] % 5 == 0:
        placar(jogo["equipe_da_casa"], jogo["equipe_visitante"])

    #DESGASTE DIMINUI A FORMA
    if jogo["minuto"] > 70:
        desgaste = [True]*2 + [False]*8
        if random.choice(desgaste):
            if jogo["equipe_da_casa"]["forma"] > 2:
                jogo["equipe_da_casa"]["forma"] -=1 
        if random.choice(desgaste):
            if jogo["equipe_visitante"]["forma"] > 2:
                jogo["equipe_visitante"]["forma"] -=1

    #time.sleep(.5)

def placar(equipe_da_casa, equipe_visitante):
    print("-"*25+"PLACAR"+"-"*25)
    print("{} {}X{} {}".format(equipe_da_casa.get("nome"), equipe_da_casa.get("gols"), equipe_visitante.get("gols"), equipe_visitante.get("nome")))
    print("-"*56)

def jogo(equipe_da_casa, equipe_visitante):

    jogo = {
        "favorito": "",
        "equipe_da_casa": equipe_da_casa,
        "equipe_visitante": equipe_visitante
    }

    favorito, nao_favorito = calcula_favorito(jogo["equipe_da_casa"], jogo["equipe_visitante"])

    print_equipes(equipe_da_casa, equipe_visitante)

    jogo["favorito"] = favorito
    jogo["nao_favorito"] = nao_favorito

    print("-----------")
    print("Inicio de partida")
    for minuto in range(1, 91):
        jogo["favoritismo"] = equipe_da_casa.get("favoritismo") - equipe_visitante.get("favoritismo")
        print("Favoritismo: {}".format(jogo["favoritismo"]))
        jogo["minuto"] = minuto
        bola_rolando(jogo)
        favorito, nao_favorito = calcula_favorito(jogo["equipe_da_casa"], jogo["equipe_visitante"])
        jogo["favorito"] = favorito
        jogo["nao_favorito"] = nao_favorito

    print("FIM DE JOGO")
    print_equipes(equipe_da_casa, equipe_visitante)
    print("Favoritismo: {}".format(jogo["favoritismo"]))
    print("Favorito: {}".format(jogo["favorito"]["nome"]))

if __name__=="__main__":
    jogo(equipe_da_casa, equipe_visitante)



