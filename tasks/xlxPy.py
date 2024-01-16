import pandas as pd

def create_excel_file(file_path='datasets/employees_multi_sheets.xlsx'):
    sheet1_data = {'Name': ['Rohan', 'Sneha', 'Aryan', 'Ananya', 'Vikram'],
                   'Salary': [50000, 60000, 55000, 70000, 48000]}

    sheet2_data = {'Name': ['Pooja', 'Kiran', 'Neha', 'Arjun', 'Simran'],
                   'Salary': [75000, 65000, 72000, 58000, 69000]}

    sheet3_data = {'Name': ['Rahul', 'Mira', 'Amit', 'Priya', 'Deepak'],
                   'Salary': [62000, 58000, 70000, 54000, 67000]}

    with pd.ExcelWriter(file_path) as writer:
        pd.DataFrame(sheet1_data).to_excel(writer, sheet_name='Sheet1', index=False)
        pd.DataFrame(sheet2_data).to_excel(writer, sheet_name='Sheet2', index=False)
        pd.DataFrame(sheet3_data).to_excel(writer, sheet_name='Sheet3', index=False)

    print(f"Excel file '{file_path}' created with 3 sheets.")

def read_excel_file(file_path='datasets/employees_multi_sheets.xlsx'):
    try:
        xls = pd.ExcelFile(file_path)
        print("\nContent of the Excel file:")
        for sheet_name in xls.sheet_names:
            df = pd.read_excel(file_path, sheet_name=sheet_name)
            print(f"\nSheet: {sheet_name}")
            print(df)
    except FileNotFoundError:
        print(f"File '{file_path}' not found. Please create the Excel file first.")

# Example usage
create_excel_file()
read_excel_file()
