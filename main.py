from json_reader import read_json_files_in_folder
from data_transformer import transform_json_to_dataframe

folder_path = 'source'
json_data = read_json_files_in_folder(folder_path)

df = transform_json_to_dataframe(json_data)


df.to_parquet('output/file.parquet', index=False) 
