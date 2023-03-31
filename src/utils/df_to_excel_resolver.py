import pandas as pd


def df_to_excel(df):
    out_path = r"C:\BI\Projects\judiciary-information-system\src\data\query_result.xlsx"
    writer = pd.ExcelWriter(out_path, engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1')
    writer.save()
