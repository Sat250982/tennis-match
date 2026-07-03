# Tennis Match Program 

Since only valid tennis match is given as input , if we just have to find the winner, we can find the last 
string in the input array( A or B) - who will be the winner.

## Approach
- Each point updates the current game_points score. A game is won with at least 4 points and a lead of 2
- The match is won with atleast 6 in game_won_count and 2 - game_won_count gap
- Tie break happens at 6 -6 in game_won_count. In tie break first to reach 7 points with 2 point leads wins


# Run 
python tennis_match.py
Three testcases are updated in the code including tie-break scenario



#Design decision
- Assumed valid input only as per problem statement
- Procedural style is opted as state machine is simple 
- find_winner function accpets the input sequence gives out put with time completexity O(n) and space complexity of O(1)


