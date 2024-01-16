import pandas as pd
import os

<<<<<<< HEAD
def clean_and_preprocess_titanic_data(input_file='datasets/titanic.csv', output_file_csv='datasets/titanic_cleaned.csv', output_file_excel='datasets/titanic_cleaned.xlsx'):
=======

def clean_and_preprocess_titanic_data(input_file='datasets/titanic.csv', output_file='datasets/titanic_cleaned.csv'):
>>>>>>> 149bb0447dd25a1e1c7cd16e4d1bba6462b0dc1d
    print("\n\n-------------------------------------------------------------")

    df = pd.read_csv(input_file, sep=',')

    print(df.columns)
    print()

    print(df.isnull().sum())
    print()

    print(df.head())

    df = df.drop(['Cabin', 'Embarked'], axis=1)

    df['Age'].fillna(df['Age'].median(), inplace=True)
    df['Fare'].fillna(df['Fare'].mean(), inplace=True)

    df['Fare'] = df['Fare'].round(2)

    df = df.drop(['SibSp', 'Parch', 'Name', 'Ticket'], axis=1)

    print(df.head())

    df.to_csv(output_file_csv, index=False)

    # Convert to Excel and save
    df.to_excel(output_file_excel, index=False)

    num_rows, num_cols = df.shape
    print(f"\nDimensions of the CSV File (Rows, Columns): {num_rows}, {num_cols - 1}")

    print("\n\n-------------------------------------------------------------")


# Example usage
clean_and_preprocess_titanic_data()
