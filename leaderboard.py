# method to add a new user
leaderboard = {'Norah22': 450, 'jordaniscool': 126, 'maya_studies': 788, 'leahlockedin': 439}

def get_leaderboard():
    return leaderboard

def get_points(user):
    return leaderboard[user]

def add_user(new_user):
    if new_user not in leaderboard:
        leaderboard[new_user] = 0

def add_points(user, new_points):
    old_points = get_points(user)
    new_points += old_points
    leaderboard[user] = new_points

def get_top_ten():
    N = 10
    top_ten = dict(sorted(leaderboard.items(), key=lambda item: item[1], reverse=True))
    return top_ten


