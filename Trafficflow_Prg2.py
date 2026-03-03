import numpy as np

traffic = np.array([
    [100, 50],   # Direction 1 N->S
    [80, 60]     # Direction 2 E->W
])

transform = np.array([[0.7, 0.3],
                      [0.6, 0.4]])
# Transformed Matrix

while True :
    print("\n--- Traffic Statistics Menu ---")
    print("Enter 1 to display the Original Traffic Flow")
    print("Enter 2 to display the Transformatoin")
    print("Enter 3 to display the Optimized Traffic Flow")
    print("Enter 4 to display the Total Vechiles per Direction")
    print("Enter 5 to display the Total Vehicles per Phase")
    print("Enter 6 to Exit")
      
    try:
        n = int(input("\nEnter Your Choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if n==1 :
        print("\nOriginal Matrix:\n", traffic)
        # Displays the Transformed Matrix
        
    elif n==2 :
        print("\nTransformation Matrix:\n", transform)
        
    elif n==3 :
        new_traffic = np.dot(traffic, transform)
        # Dot product of 2 Matrices which provides the optimized result.
        print("\nTraffic After Signal Optimization:\n", new_traffic)
        # Displays the Optimized Matrix

    elif n==4 :
        print("\nTotal traffic per direction:", np.sum(new_traffic, axis=1))
        # Displays the Total traffic in each direction
    
    elif n==5 :
        print("Total traffic per phase:", np.sum(new_traffic, axis=0))
        # Displays the total traffic per Phase
        
    elif n==6 :
        print("Exiting program. Goodbye :)")
        break
    
    else :
        print("\nInvalid Entry, Enter a valid choice (1-6) and Try again.")
