import pandas as pd

# Load CSV file
file = input("Enter the CSV file name (example: covid_data.csv): ")
data = pd.read_csv(file)

while True:
    print("\n----- COVID Data Exploration Menu -----")
    print("1. Display First 5 Records")
    print("2. Display Last 5 Records")
    print("3. Display Dataset Information")
    print("4. Display Statistical Summary")
    print("5. Show Total Cases, Deaths, and Recoveries")
    print("6. Find Town with Highest Cases")
    print("7. Calculate Recovery Rate")
    print("8. Preventive Measures Suggestion")
    print("9. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\nFirst 5 Records:")
        print(data.head())

    elif choice == 2:
        print("\nLast 5 Records:")
        print(data.tail())

    elif choice == 3:
        print("\nDataset Information:")
        print(data.info())

    elif choice == 4:
        print("\nStatistical Summary:")
        print(data.describe())

    elif choice == 5:
        print("\nTotal Cases:", data["Cases"].sum())
        print("Total Deaths:", data["Deaths"].sum())
        print("Total Recoveries:", data["Recovered"].sum())

    elif choice == 6:
        highest = data.loc[data["Cases"].idxmax()]
        print("\nTown with Highest Cases:")
        print(highest)

    elif choice == 7:
        recovery_rate = (data["Recovered"].sum() / data["Cases"].sum()) * 100
        print("\nRecovery Rate: {:.2f}%".format(recovery_rate))

    elif choice == 8:
        print("\nSuggested Preventive Measures:")
        print("1. Wear masks in crowded places")
        print("2. Maintain social distancing")
        print("3. Take vaccination")
        print("4. Wash hands frequently")
        print("5. Avoid large gatherings")

    elif choice == 9:
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")