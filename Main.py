from flask import Flask, render_template, request
import random

# Define a class to represent a user
class User:
    def __init__(self, name, age, gender, preferences):
        self.name = name
        self.age = age
        self.gender = gender
        self.preferences = preferences

# Define a function to calculate match score
def calculate_match_score(user1, user2):
    # Define a dictionary of preference weights
    preference_weights = {
        "non-smoking": 2,  # Non-smoking is twice as important as other preferences
        "morning person": 1,
        "night owl": 1,
        "likes pets": 1,
        "vegetarian": 1,
    }

    # Initialize a match score variable
    match_score = 0

    # Increment the match score for each preference that the users have in common, using the preference weights
    for preference in user1.preferences:
        if preference in user2.preferences:
            match_score += preference_weights[preference]

    # Return the match score
    return match_score

# Define a function to find the best match for a given user
def find_best_match(user, users):
    # Initialize variables to keep track of the best match
    best_match = None
    best_match_score = 0

    # Loop through the list of users and calculate the match score for each one
    for potential_match in users:
        # Skip the user themselves
        if potential_match == user:
            continue

        # Calculate the match score for the potential match
        match_score = calculate_match_score(user, potential_match)

        # If the match score is higher than the current best match score, update the best match
        if match_score > best_match_score:
            best_match = potential_match
            best_match_score = match_score

    # Return the best match and the best match score
    return best_match, best_match_score

# List of possible preferences
preferences = ["non-smoking", "morning person", "night owl", "likes pets", "vegetarian"]

# List of possible names
names = ["Alice", "Brianca", "Charlie", "Diane", "Eve", "Frank", "Greta", "Henry"]

# List of possible genders
genders = ["male", "female"]

# Generate 1000 users with random attributes
users = [
    User(
        random.choice(names),  # Random name
        random.randint(18, 60),  # Random age between 18 and 60
        random.choice(genders),  # Random gender
        random.sample(preferences, random.randint(1, len(preferences)))  # Random preferences
    )
    for _ in range(1000)
]

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get user input
        name = request.form.get('name')
        age = int(request.form.get('age'))
        gender = request.form.get('gender')
        preferences = request.form.getlist('preferences')

        # Create a new user with the input data
        user = User(name, age, gender, preferences)

        # Find the best match for the new user
        best_match, best_match_score = find_best_match(user, users)

        # Calculate the match score breakdown
        match_score_breakdown = {}
        if best_match:
            for preference in user.preferences:
                if preference in best_match.preferences:
                    match_score_breakdown[preference] = calculate_match_score(user, best_match)

        # Return the result to the user
        return render_template('result.html', match=best_match, score=best_match_score, match_score_breakdown=match_score_breakdown)

    # If method is GET, show the form
    return render_template('form.html')

#if __name__ == '__main__':
    #app.run(debug=True)