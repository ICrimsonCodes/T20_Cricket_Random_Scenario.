import random

# List of teams
teams = ["Afghanistan", "Australia", "Bangladesh", "England", "India", "Ireland", "Pakistan", "Scotland", "South Africa", "Sri Lanka", "West Indies", "Zimbabwe"]

# Round One
round_one_winners = []
for i in range(6):
    team_a = random.choice(teams)
    teams.remove(team_a)
    team_b = random.choice(teams)
    teams.remove(team_b)
    winner = random.choice([team_a, team_b])
    round_one_winners.append(winner)
    print("Match {}: {} vs. {}, won by {}".format(i+1, team_a, team_b, winner))

# Round Two
round_two_winners = []
for i in range(3):
    team_a = round_one_winners[i*2]
    team_b = round_one_winners[i*2+1]
    winner = random.choice([team_a, team_b])
    round_two_winners.append(winner)
    print("Match {}: {} vs. {}, won by {}".format(i+7, team_a, team_b, winner))

# Round Three
if round_two_winners[0] == round_two_winners[1]:
    team_a = round_two_winners[0]
    team_b = round_two_winners[2]
    winner = random.choice([team_a, team_b])
    if winner == team_a:
        print("Team {} qualified for the final after winning the toss.".format(team_a))
        print("Match 13: {} vs. {}, won by {}".format(team_a, team_b, winner))
    else:
        print("Match 13: {} vs. {}, won by {}".format(team_a, team_b, winner))
        print("Team {} qualified for the final after winning the toss.".format(team_b))
else:
    for i in range(3):
        if round_two_winners[i] != round_two_winners[(i+1)%3]:
            team_a = round_two_winners[i]
            team_b = round_two_winners[(i+1)%3]
            print("Match 10: {} vs. {}, won by {}".format(team_a, team_b, team_a))
            print("Match 11: {} vs. {}, won by {}".format(team_b, team_a, team_b))
            print("Match 12: {} vs. {}, won by {}".format(team_a, team_b, team_b))
            break

# Final Match
team_a = round_two_winners[0]
team_b = round_two_winners[1]
winner = random.choice([team_a, team_b])
print("Match 14: {} vs. {}, won by {}".format(team_a, team_b, winner))
print("Congratulations to {} for winning the T20 World Cup 2020.".format(winner))
