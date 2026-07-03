#code implementation

def opponent(player):
    if player == "A":
        return "B"
    elif player == "B":
        return "A"


def game_won(winner_points, loser_points):
     if(winner_points >= 4 and ((winner_points-loser_points) >= 2)):
         return True
     else:
         return False


def find_winner(tennis_points):
    game_points = {"A": 0, "B": 0}
    game = {"A": 0, "B": 0}

    for point_winner in tennis_points:
        point_loser = opponent(point_winner)
        game_points[point_winner] += 1

        if game_won(game_points[point_winner],game_points[point_loser]):
            game[point_winner] += 1
            game_points = { "A": 0, "B": 0 }


    return game[]





tennis_points = [ "A", "B", "B", "B","A", "B"]
result = find_winner(tennis_points)
print (result )
