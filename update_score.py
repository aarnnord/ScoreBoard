import requests

def update_score(team_name, new_score):
    # URL for the score update endpoint
    url = 'http://192.168.1.108:5000/update_score'
    
    # Data to be sent in the request
    data = {
        'team_name': team_name,
        'new_score': new_score
    }
    
    # Send POST request to update the score
    response = requests.post(url, json=data)
    
    if response.status_code == 200:
        print(f"Successfully updated {team_name}'s score to {new_score}.")
    else:
        print(f"Failed to update score: {response.json()['error']}")

# Example usage
if __name__ == '__main__':

    while(True):
        team_name = input("Enter the team name: ")
        new_score = int(input("Enter the new score: "))
        
        update_score(team_name, new_score)
