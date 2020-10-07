from . import db, Field

import datetime

"""
flask shell
from football import db
championship = db.championship.insert(name="Campeonato Brasileiro")
team1 = db.team.insert(championship=championship, name="Santos F.C.")
team2 = db.team.insert(championship=championship, name="C.R. Flamengo")
player1 = db.player.insert(name="Robinho", team=team1)
player2 = db.player.insert(name="Diego", team=team2)
player3 = db.player.insert(name="Giovani", team=team1)
match1 = db.match.insert(championship=1, home_team=team1, away_team=team2)
db(db.match.id==match1).update(home_goals=[db.goal.insert(player=player1), db.goal.insert(player=player3)])
db(db.match.id==match1).update(away_goals=[db.goal.insert(player=player2)])
for i in db(db.match.id==match1).select():
  print(i.home_team.name, len(i.home_goals), len(i.away_goals), i.away_team.name)
db.commit()

sqlite3 football/db/storage.db 
sqlite> select * from championship;
1|Campeonato Brasileiro
sqlite> select * from team;
1|1|Santos F.C.
2|1|C.R. Flamengo
sqlite> select * from player;
1|Robinho|
2|Diego|
sqlite> select * from match;
1|1|1|2||1|2|||3|
"""

db.define_table('championship',
    Field('name', type="string", notnull=True),
    Field('nation', type="string")
)

db.define_table('team',
    Field('championship', 'reference championship'),
    Field('nation', type="string"),
    Field('amount_of_players', type="string"),
    Field('media_age', type="string"),
    Field('market_value', type="string"),
    Field('name', type="string", notnull=True)
)

db.define_table('manager',
    Field('name', type="string", notnull=True),
    Field('nation', type="string"),
    Field('since', type="string"),
    Field('contract_expires', type="string"),
    Field('age', type="string"),
    Field('team', 'reference team')
)

db.define_table('player',
    Field('name', type="string", notnull=True),
    Field('nation', type="string"),
    Field('number', type="string"),
    Field('position', type="string"),
    Field('contract_expires', type="string"),
    Field('date_of_birth', type="string"),
    Field('age', type="string"),
    Field('market_value', type="string"),
    Field('team', 'reference team')
)

db.define_table('goal',
    Field('player', 'reference player')
)

db.define_table('match',
    Field('championship', 'reference championship'),
    Field('home_team', 'reference team'),
    Field('away_team', 'reference team'),
    Field('home_goals', 'list:reference goal', default = []),
    Field('away_goals', 'list:reference goal', default = [])
)