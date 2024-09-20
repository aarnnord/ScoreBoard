from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__, static_folder='static')

# Initial team data
if os.path.exists("static/data.json"):
    with open("static/data.json", "r") as json_file:
        teams = json.load(json_file)
else:
    teams = [
        {"name": "AISODOI", "logo": "aisodoi2.png", "score": 0},
        {"name": "MONKEY INTELLIGENCE", "logo": "monkey2.png", "score": 0},
        {"name": "MAINOSPAIKKA", "logo": "mp2.png", "score": 0},
        {"name": "TUNKKAAJAT", "logo": "tunkkaajat2.png", "score": 0},
        {"name": "WTEAMHAMK", "logo": "wth2.png", "score": 0},
        {"name": "ZERO ONES GIVEN", "logo": "zog2.png", "score": 0}
    ]

@app.route('/')
def scoreboard():
    return render_template('scoreboard_new_test.html', teams=teams)

@app.route('/update_score', methods=['POST'])
def update_score():
    data = request.get_json()
    team_name = data.get('team_name')
    new_score = data.get('new_score')
    
    for team in teams:
        if team['name'] == team_name:
            team['score'] = new_score
            break
    
    #Save to json file
    with open("static/data.json", "w") as json_file:
        json.dump(teams, json_file, indent=4)  # 'indent=4' makes the output readable (pretty-printed)
    
    return jsonify({"message": "Score updated successfully!"})

@app.route('/get_scores', methods=['GET'])
def get_scores():
    return jsonify(teams)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
