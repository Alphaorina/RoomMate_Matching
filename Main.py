# Define a class to represent a user
class User:
    def __init__(self, name, age, gender, preferences):
        self.name = name
        self.age = age
        self.gender = gender
        self.preferences = preferences


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

    # Return the best match
    return best_match


# Define some sample users
import random

# List of possible preferences
preferences = ["non-smoking", "smoking", "morning person", "night owl", "likes pets", "vegetarian"]

# Generate 1000 users with random attributes
users = [
    User("Dennis", 25, "female", ["non-smoking", "morning person"]),
    User("Fidel", 32, "male", ["non-smoking", "night owl"]),
    User("Charlie", 29, "male", ["smoking", "morning person"]),
    User("Diane", 27, "female", ["smoking", "night owl"]),
    User("SHeila", 22, "female", ["non-smoking", "morning person", "likes pets"]),
    User("Frank", 35, "male", ["smoking", "night owl", "likes pets"]),
    User("Greta", 31, "female", ["non-smoking", "morning person", "vegetarian"]),
    User("Henry", 30, "male", ["smoking", "night owl", "vegetarian"]),
]



# Find the best match for Alice
best_match = find_best_match(users[0], users)
print(
    f"{best_match.name} is the best match for Dennis with a match score of {calculate_match_score(users[0], best_match)}")
