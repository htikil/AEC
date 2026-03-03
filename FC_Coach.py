import numpy as np

goals = np.array([[2, 3, 2],
                  [1, 2, 1],
                  [0, 2, 0]])

while True :
    print("\n--- Match Statistics Menu ---")
    print("\nEnter 1 to Display the Goals Scored by 3 players in 3 Matches. \nEnter 2 to Display the Total Goals scored by each Player in 3 Matches.\nEnter 3 to Apply double Points for each goals scored on Match 3. \nEnter 4 to Display Total Goals Scored by each player after Bonus Applied. \nEnter 5 to Display all the data in a Single Row.\nEnter 6 to Exit")
    
    try:
        n = int(input("\nEnter Your Choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    
    if n==1 :
        print("\nGoals scored by 3 Players:\n", goals)
        
    elif n==2 :
        player_total=np.sum(goals, axis=1)
        print("\nTotal goals scored by each Player : ", player_total)
        
    elif n==3 :
        bonus_goals=goals.copy()
        bonus_goals[:, 2]*=2
        print("\nGoalsheet after Bonus Applied :\n", bonus_goals)
        
    elif n==4 :
        bonus_goals=goals.copy()
        bonus_goals[:, 2]*=2
        new_total=np.sum(bonus_goals, axis=1)
        print("\nNew player total after bonus: ", new_total)
        
    elif n==5 :
        flattened=goals.reshape(1,9)
        print("\nFlattened Matrix :", flattened)
        
    elif n==6 :
        print("Exiting program. Goodbye!")
        break
    
    else :
        print("\nInvalid Entry, Enter a valid choice (1-6) and Try again.")
   