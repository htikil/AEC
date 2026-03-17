import numpy as np
from statistics import mode

# Input temperature data from user
n = int(input("Enter the number of temperature readings: "))
temps = []

for i in range(n):
    value = float(input(f"Enter temperature {i+1}: "))
    temps.append(value)

temperature = np.array(temps)

while True:
    print("\n----- Temperature Data Analysis Menu -----")
    print("1. Calculate Mean")
    print("2. Calculate Median")
    print("3. Calculate Mode")
    print("4. Calculate Variance")
    print("5. Calculate Standard Deviation")
    print("6. Display All Data")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\nMean:", np.mean(temperature))

    elif choice == 2:
        print("\nMedian:", np.median(temperature))

    elif choice == 3:
        try:
            print("\nMode:", mode(temperature))
        except:
            print("No unique mode found.")

    elif choice == 4:
        print("\nVariance:", np.var(temperature))

    elif choice == 5:
        print("\nStandard Deviation:", np.std(temperature))

    elif choice == 6:
        print("\nTemperature Data:", temperature)

    elif choice == 7:
        print("Program Exited.")
        break

    else:
        print("Invalid choice. Please try again.")