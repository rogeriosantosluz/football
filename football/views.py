from flask import Flask, render_template, request, redirect, flash, url_for, session, g, jsonify
from . import app
from . import db
#from .models import Domains, DNSTwist

@app.route("/")
def home():
    #metrics(request, session)
    app.logger.info("Home")
    return render_template("home.html")

@app.route("/players", methods=['GET'])
def players():
    team = request.args.get("team")
    response_object = {'status': 'success'}
    app.logger.info("Players team:{}".format(team))
    response_object['players'] = db((db.player.team==db.team.id)&(db.team.id==team)).select(db.player.ALL).as_list()
    return jsonify(response_object)

@app.route("/teams", methods=['GET'])
def teams():
    championship = request.args.get("championship")
    response_object = {'status': 'success'}
    app.logger.info("Teams championship:{}".format(championship))
    response_object['teams'] = db((db.team.championship==db.championship.id) & (db.championship.id==championship)).select(db.team.ALL).as_list()
    return jsonify(response_object)

@app.route("/championships", methods=['GET'])
def championships():
    response_object = {'status': 'success'}
    app.logger.info("Championships")
    response_object['championships'] = db(db.team.championship==db.championship.id).select(db.championship.id, db.championship.name, distinct=True).as_list()
    return jsonify(response_object)

@app.route("/fp/")
def fp():
    #app.logger.info("GGGGGGGGG")
    session["fingerprint"] = request.args.get("fp")
    return "OK"

def to_index():
    return redirect(url_for('home'))

@app.before_request
def login_handle():
    g.logged_in = bool(session.get('logged_in'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    app.logger.info('Login')
    if session.get('logged_in'):
        flash("You are already logged in")
        return to_index()
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if (username == app.config['ADMIN_USERNAME'] and
            password == app.config['ADMIN_PASSWORD']):
            session['logged_in'] = True
            flash("Successfully logged in")
            return to_index()
        else:
            flash("Those credentials were incorrect")
    return render_template('login.html')


@app.route('/logout')
def logout():
    if session.get('logged_in'):
        session['logged_in'] = False
        flash("Successfully logged out")
    else:
        flash("You weren't logged in to begin with")
    return to_index()