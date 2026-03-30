import pandas as pd

# Load dataset
df = pd.read_csv("Hr_Dataset.csv")

while True:
    print("\n====== HR DATA HANDLING MENU ======")
    print("1. Display Original Dataset")
    print("2. Handle Missing Values (Mean)")
    print("3. Remove Duplicate Records")
    print("4. Convert Data Types")
    print("5. Perform ALL the above Operations")
    print("6. Display Updated Dataset")
    print("7. Exit")
    try:
        choice = int(input("Enter your choice: "))
    except:
        print("Invalid input. Enter a number.")
        continue

    if choice == 1:
        print("\nOriginal Dataset:\n")
        print(df)

    elif choice == 2:
        mean_score = round(df['Performance_Score'].mean(), 1)
        mean_salary = round(df['Salary'].mean(), 1)

        df['Performance_Score'] = df['Performance_Score'].fillna(mean_score)
        df['Salary'] = df['Salary'].fillna(mean_salary)
        df['Join_Date'] = df['Join_Date'].fillna("2022-01-01")

        print("\nMissing values handled.")

    elif choice == 3:
        df = df.drop_duplicates()

        # Auto reset index
        df.reset_index(drop=True, inplace=True)
        df.index = df.index + 1

        print("\nDuplicates removed.")

    elif choice == 4:
        df['Join_Date'] = pd.to_datetime(df['Join_Date'])
        df['Performance_Score'] = df['Performance_Score'].astype(int)

        print("\nData types converted.")

    elif choice == 5:
        print("\nPerforming ALL operations...\n")

        # Handle missing values
        mean_score = round(df['Performance_Score'].mean(), 1)
        mean_salary = round(df['Salary'].mean(), 1)

        df['Performance_Score'] = df['Performance_Score'].fillna(mean_score)
        df['Salary'] = df['Salary'].fillna(mean_salary)
        df['Join_Date'] = df['Join_Date'].fillna("2022-01-01")

        # Remove duplicates
        df = df.drop_duplicates()

        # Convert data types
        df['Join_Date'] = pd.to_datetime(df['Join_Date'])
        df['Performance_Score'] = df['Performance_Score'].astype(int)

        # Reset index automatically
        df.reset_index(drop=True, inplace=True)
        df.index = df.index + 1

        print("All operations completed.")

    elif choice == 6:
        print("\nUpdated Dataset:\n")
        print(df)

    elif choice == 7:
        print("Program Exited.")
        break

    else:
        print("Invalid choice.")