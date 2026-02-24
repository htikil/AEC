import numpy as np

goals = np.array([[2, 3, 2]
                  [1, 2, 1]
                  [0, 2, 0]])

print("Goals scored by 3 Players:\n", goals)
player_total=np.sum(goals, axis=1)
print("Total goals by each Player : ", player_total)
bonus_goals=goals.copy()
bonus_goals[:, 2]*=2
print("Goalsheet after Bonus Applied :\n", bonus_goals)
