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

def match_won(winner_games_count, loser_games_count):
    if ( winner_games_count >=6 and (winner_games_count - loser_games_count >=2)):
        return True
    else:
        return False


def find_winner(tennis_points):
    game_points = {"A": 0, "B": 0}             # 15, 30, 40 etc
    game_won_count = {"A": 0, "B": 0}                    # 1,2,3, 4, 5, 6

    for point_winner in tennis_points:
        point_loser = opponent(point_winner)
        game_points[point_winner] += 1

        if game_won(game_points[point_winner],game_points[point_loser]):
            game_won_count[point_winner] += 1
            game_points = { "A": 0, "B": 0 }

            if match_won(game_won_count[point_winner],game_won_count[point_loser]):
                 return point_winner, game_won_count


    return





# all won by b
tennis_points = [ "A", "B", "B", "B","A", "B", "A", "B", "B", "B","A", "B", "A", "B", "B", "B","A", "B", "A", "B", "B", "B","A", "B", "A", "B", "B", "B","A", "B", "A", "B", "B", "B","A", "B"]

tennis_points = [ "A", "B", "B", "B","A", "B", "A", "B", "B", "B","A", "B", "A", "B", "B", "B","A", "B", "A", "B", "B", "B","A", "B", "A", "B", "B", "B","A", "B", "A", "B", "B", "B","A", "B"]

point_winner, game_won_count = find_winner(tennis_points)


print (point_winner)
print (game_won_count)
