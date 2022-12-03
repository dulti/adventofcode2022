# 0 - rock, 1 - paper, 2 - scissors
# 0 - tie, 1 - player wins, 2 - opponent wins

outcomes_opp = {'A': 0, 'B': 1, 'C': 2}
outcomes_you = {'X': 2, 'Y': 0, 'Z': 1}
round_outcomes = {0: 3, 1: 6, 2: 0}

rounds = []
with open('day2_input.txt', 'r') as f:
    while line := f.readline():
        rounds.append(tuple(line.strip().split(' ')))
        
# part 1
total_score = 0

for round in rounds:
    total_score += shape_scores[outcomes_you[round[1]]]
    round_outcome = round_outcomes[
                        (shape_scores[outcomes_you[round[1]]] - 
                         shape_scores[outcomes_opp[round[0]]]) % 3]
    total_score += round_outcome

print(total_score)

# part 2
total_score = 0

for round in rounds:
    opp_choice = outcomes_opp[round[0]]
    strat = outcomes_you[round[1]]
    if strat == 0:
        total_score += 3
        player_choice = opp_choice
    elif strat == 1:
        total_score += 6
        player_choice = (opp_choice + 1) % 3
    else:
        player_choice = (opp_choice - 1) % 3
    
    total_score += player_choice + 1
    
print(total_score)