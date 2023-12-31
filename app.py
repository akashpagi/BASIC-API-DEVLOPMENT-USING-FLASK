
from flask import Flask, jsonify, request
import ipl
import extra_ipl
import json

app = Flask(__name__)

@app.route('/')
def home():
    return 'Home'

# Teams api
@app.route('/api/teams')
def teams():
    # call the teamAPI function form ipl.py
    teams = ipl.teamAPI()
    # jsonify convert the temas list into json format
    return jsonify(teams)

# teamVsteamAPI
@app.route('/api/teamvsteam')
def teamvsteam():
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')
    t1vst2 = ipl.teamVsteamAPI(team1, team2)
    return jsonify(t1vst2)

# team record
# api hit : Ex. http://127.0.0.1:5000/api/team-record?team=Mumbai%20Indians
@app.route('/api/team-record')
def team_record():
    team_name = request.args.get('team')
    response = extra_ipl.teamAPI(team_name)
    return response

# batting record
# api hit : Ex. http://127.0.0.1:5000/api/batting-record?batsman=V%20Kohli
@app.route('/api/batting-record')
def batting_record():
    batsman_name = request.args.get('batsman')
    response = extra_ipl.batsmanAPI(batsman_name)
    return response

# bowler record
# api hit : Ex. http://127.0.0.1:5000/api/bowler-record?bowler=Kuldeep%20Yadav
@app.route('/api/bowler-record')
def bowling_record():
    bowler_name = request.args.get('bowler')
    response = extra_ipl.bowlerAPI(bowler_name)
    return response

app.run(debug=True)