from pickle import TRUE
import arrow
import pandas as pd

CURRENT_DATETIME = arrow.utcnow().to('Asia/Jakarta').strftime("%d-%m-%Y %H%M%S")
# print(CURRENT_DATETIME)

file_path = '../belajar-python/name-file.csv'

df = pd.read_csv(file_path)

#How to get list of columns name
column_names = df.columns.values

data_df = pd.DataFrame(df,columns=column_names)

new_df = pd.DataFrame(columns=[
    "id",
    "json"
])

for index,row in data_df.iterrows():
    new_records = pd.DataFrame.from_records({
        "id":[row['Voucher_Code']],
        "json":[row.to_json()]
    })
    new_df = pd.concat([new_df,new_records],ignore_index=TRUE)

output_file_path = f'script/output/output-{CURRENT_DATETIME}.csv'
create_csv = new_df.to_csv(output_file_path,sep=',',index=False,encoding='utf-8')
# print(data_df)