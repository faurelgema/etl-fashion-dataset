import pandas as pd

transaction_df = pd.read_excel("/content/process.xlsx", sheet_name="transaction")
master_process_df = pd.read_excel("/content/process.xlsx", sheet_name="masterprocess")


merged_df = pd.merge(transaction_df, master_process_df, on="process", how="left")

def check_process_order(processes):
    orders = []
    process_list = list(processes)  
    for process in process_list:
        order = master_process_df[master_process_df["process"]==process]["process order"].iloc[0] if not master_process_df[master_process_df["process"]==process].empty else float('inf')
        orders.append(order)
    return sorted(process_list, key=lambda x: orders[process_list.index(x)])


result_df = merged_df.groupby("finish_good").agg({
    "process": lambda x: list(x),
    "process order": lambda x: check_process_order(x),
}).reset_index()

print(result_df)
