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
    if (winner_games_count >=6 and (winner_games_count - loser_games_count >=2)):
        return True
    else:
        return False

def tiebreak_won(winner_tiebreak_count, loser_tiebreak_count):
    if  ((winner_tiebreak_count >=7) and (winner_tiebreak_count - loser_tiebreak_count >=2)):
        return True
    else:
        return False


def find_winner(tennis_points):
    game_points = {"A": 0, "B": 0}             # 15, 30, 40 etc
    game_won_count = {"A": 0, "B": 0}          # 1,2,3, 4, 5, 6
    tiebreak_points = {"A": 0, "B": 0}
    is_tiebreak = False


    for point_winner in tennis_points:
        point_loser = opponent(point_winner)

        if is_tiebreak:
            tiebreak_points[point_winner] += 1
            if tiebreak_won(tiebreak_points[point_winner],tiebreak_points[point_loser]):
                is_tiebreak = False
                game_won_count[point_winner] += 1
                return point_winner, point_loser, game_won_count, tiebreak_points
        else :
            game_points[point_winner] += 1

            if game_won(game_points[point_winner],game_points[point_loser]):
                game_won_count[point_winner] += 1
                game_points = { "A": 0, "B": 0 }

                if match_won(game_won_count[point_winner],game_won_count[point_loser]):
                         return point_winner, point_loser, game_won_count, None

                if((game_won_count[point_winner] == 6) and (game_won_count[point_loser] == 6)):
                        is_tiebreak = True


    return





# all won by b
tennis_points = [ "A", "B", "B", "B","A", "B", "A", "B", "B", "B","A", "B", "A", "B", "B", "B","A", "B", "A", "B", "B", "B","A", "B", "A", "B", "B", "B","A", "B", "A", "B", "B", "B","A", "B"]

tennis_points = [ "A", "B", "B", "B","A", "B", "A", "B", "B", "B","A", "B", "A", "B", "B", "B","A", "B", "A", "B", "B", "B","A", "B", "A", "B", "B", "B","A", "B", "A", "B", "B", "B","A", "B"]

winner,loser, game_won_count, tiebreak_points = find_winner(tennis_points)


print (f"{winner} Won the Game")
print (f" Game results A : {game_won_count['A']}, B: {game_won_count['B']}")
if tiebreak_points:
    print(tiebreak_points)
    print(f" Tiebreak results A : {tiebreak_points['A']}, B: {tiebreak_points['B']}")
