import pandas as pd
import os


def clean_and_preprocess_titanic_data(input_file='datasets/titanic.csv', output_file='datasets/titanic_cleaned.csv'):
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

    df.to_csv(output_file, index=False)

    num_rows, num_cols = df.shape
    print(f"\nDimensions of the CSV File (Rows, Columns): {num_rows}, {num_cols - 1}")

    print("\n\n-------------------------------------------------------------")


# Example usage
clean_and_preprocess_titanic_data()
