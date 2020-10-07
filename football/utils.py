from . import db
from . import app
#from .models import Domains, DNSTwist
import click

from flask import Blueprint

bp = Blueprint('utils', __name__)

@bp.cli.command('import_teams_players')
def import_teams_players():
    """ Import teams and players """
    import json
    import os 
    from . import db

    ROOT_DIR = "/Users/rogerioluz/Documents/football/files/"
    for file_name in os.listdir(ROOT_DIR):
        print("###########################-----------------")
        print("CAMPEONATO: {}".format(file_name))
        print("###########################-----------------")
        
        championship = db.championship.insert(name=file_name.split(".json")[0])

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

            team = db.team.insert(
                championship=championship, 
                name=club.get("name"), 
                nation=club.get("nation"), 
                amount_of_players=club.get("amount_of_players"), 
                media_age=club.get("media_age"), 
                market_value=club.get("market_value")
            )
            manager = club.get("manager")
            db.manager.insert(
                name=manager.get("name"), 
                team=team, 
                nation=manager.get("nation"), 
                contract_expires=manager.get("contract_expires"), 
                since=manager.get("since"), 
                age=manager.get("age"))

            players = club.get("players")
            for i in players:
                print("{} - {} ({}) - {}".format(i.get("number"), i.get("name"), i.get("position"), i.get("nation")) )
                db.player.insert(
                    name=i.get("name"), 
                    team=team, 
                    number=i.get("number"), 
                    position=i.get("position"), 
                    nation=i.get("nation"), 
                    contract_expires=i.get("contract_expires"), 
                    date_of_birth=i.get("date_of_birth"), 
                    age=i.get("age"), 
                    market_value=i.get("market_value"))
    db.commit()


app.register_blueprint(bp)