#code implementation

def opponent(player):
    """Get the opponent of the player"""
    if player == "A":
        return "B"
    elif player == "B":
        return "A"


def game_won(winner_points, loser_points):
     """Checks whether the current game has been won"""
     if(winner_points >= 4 and ((winner_points-loser_points) >= 2)):
         return True
     else:
         return False

def match_won(winner_games_count, loser_games_count):
    """Checks whether the match is  won"""
    if (winner_games_count >=6 and (winner_games_count - loser_games_count >=2)):
        return True
    else:
        return False



def tiebreak_won(winner_tiebreak_count, loser_tiebreak_count):
    """Checks whether the tiebreak is won """
    if  ((winner_tiebreak_count >=7) and (winner_tiebreak_count - loser_tiebreak_count >=2)):
        return True
    else:
        return False


def find_winner(tennis_points):
    """Finds the winner of the game"""
    game_points = {"A": 0, "B": 0}             # 15, 30, 40 etc
    game_won_count = {"A": 0, "B": 0}          # 1,2,3, 4, 5, 6
    tiebreak_points = {"A": 0, "B": 0}         # 1,2,3,4,5,6,7
    is_tiebreak = False

    #iterating the input arrary
    for point_winner in tennis_points:
        point_loser = opponent(point_winner)

        #check for tie-break and winning criteria in tie-break
        if is_tiebreak:
            tiebreak_points[point_winner] += 1
            if tiebreak_won(tiebreak_points[point_winner],tiebreak_points[point_loser]):
                is_tiebreak = False
                game_won_count[point_winner] += 1
                return point_winner, game_won_count, tiebreak_points
        else :
            game_points[point_winner] += 1

            # which player won the game
            if game_won(game_points[point_winner],game_points[point_loser]):
                game_won_count[point_winner] += 1
                game_points = { "A": 0, "B": 0 }

                #which player won the match/set
                if match_won(game_won_count[point_winner],game_won_count[point_loser]):
                         return point_winner, game_won_count, None

                #Whether there was a tie-break in the match
                if((game_won_count[point_winner] == 6) and (game_won_count[point_loser] == 6)):
                        is_tiebreak = True


    return None


def run_test(name, tennis_points):
    print(f"--- {name} ---")
    result = find_winner(tennis_points)
    if result is None:
        print(" Invalid Input from user")
        return
    point_winner, game_won_count, tiebreak_points = result
    print(f"{point_winner} Won the Match")
    print(f"Game won count A = {game_won_count['A']}, B = {game_won_count['B']}")
    if tiebreak_points:
        print(f"Tiebreak points A = {tiebreak_points['A']}, B = {tiebreak_points['B']}")


if __name__ == "__main__":
    test1 = ["A", "B", "B", "B", "A", "B",  # 0-1
             "A", "B", "B", "B", "A", "B",  # 0-2
             "A", "B", "B", "B", "A", "B",  # 0-3
             "A", "B", "B", "B", "A", "B",  # 0-4
             "A", "B", "B", "B", "A", "B",  # 0-5
             "A", "B", "B", "B", "A", "B"]  # 0-6

    test2 = ["A", "A", "A","B", "B", "A",  # A leads 1-0
         "B", "B", "B", "B",  # 1-1
         "A", "A", "A", "A",  # 2-1
         "B", "B", "B", "B",  # 2-2
         "A", "A", "A", "A",  # 3-2
         "B", "B", "B", "B",  # 3-3
         "A", "A", "A", "A",  # 4-3
         "B", "B", "B", "B",  # 4-4
         "A", "A", "A", "A",  # 5-4
         "B", "B", "B", "B",  # 5-5
         "A", "A", "A", "A",  # A leads 6-5 (match NOT over - only 1 game lead)
         "A", "A", "A", "A"]  # A wins 7-5

    test3 = ["A", "A", "A", "A",   # A leads 1-0
             "B", "B", "B", "B",   # 1-1
             "A", "A", "A", "A",   # 2-1
             "B", "B", "B", "B",   # 2-2
             "A", "A", "A", "A",   # 3-2
             "B", "B", "B", "B",   # 3-3
             "A", "A", "A", "A",   # 4-3
             "B", "B", "B", "B",   # 4-4
             "A", "A", "A", "A",   # 5-4
             "B", "B", "B", "B",   # 5-5
             "A", "A", "A", "A",   # 6-5
             "B", "B", "B", "B",   # 6-6 -> tiebreak starts here
             # tiebreak points:
             "A", "B", "A", "B",   # 2-2
             "A", "B", "A", "B",   # 4-4
             "A", "B", "A", "B",   # 6-6 (A reached 7? no - 6 each, no lead)
             "A",                  # 7-6 (A has 7 but lead is only 1 - NOT won)
             "A"]

    run_test("B wins 6-0", test1)
    run_test("A Wins 7-5", test2)
    run_test("A Wins in Tie break 8-6", test3)






