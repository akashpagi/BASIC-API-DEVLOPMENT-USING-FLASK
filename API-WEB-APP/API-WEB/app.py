from flask import Flask,render_template,request
import requests # library and only 'request' is class function

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get('http://127.0.0.1:5000/api/teams')
    teams = response.json()['teams']
    # at the loading teams=teams dispaly teams name page at index page 
    return render_template('index.html',teams = sorted(teams))

@app.route('/teamvsteam')
def team_vs_team():
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')
    response = requests.get('http://127.0.0.1:5000/api/teamvsteam?team1={}&team2={}'.format(team1, team2))
    response = response.json()
    
    team_response = requests.get('http://127.0.0.1:5000/api/teams')
    teams = team_response.json()['teams']
    
    return render_template('index.html', result = response, teams = sorted(teams))

app.run(debug=True, port=8000)