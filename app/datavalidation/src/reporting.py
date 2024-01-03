import matplotlib.pyplot as plt
from datavalidation import write_csv

def create_exceptions_report(result_df, path):
    if result_df.empty:
        return "Input DataFrame is empty, no exceptions to report"

    # Filter out rows where holdings are not equal
    exceptions_report = result_df[result_df['is_equal'] == False][['account_id', 'product_id', 'total_product_balance', 'total_cashflow', 'difference']]

    # Write the exceptions report to a CSV file
    write_csv(exceptions_report, path)
    
    return len(exceptions_report)

def create_exceptions_chart(result_df, path):
    if result_df.empty:
        return "Input DataFrame is empty, no exceptions to report"

    unique_accounts = len(result_df['account_id'].unique())
    total_holdings = len(result_df)
    valid_holdings = len(result_df[result_df['is_equal']])
    invalid_holdings = len(result_df[~result_df['is_equal']])

    # Values for the chart
    values = [unique_accounts, total_holdings, valid_holdings, invalid_holdings]

    # Creating the chart
    plt.figure(figsize=(10, 6))
    plt.bar(['Total Accounts', 'Total Holdings', 'Valid Holdings', 'Invalid Holdings'], values)
    plt.ylabel('Number of Records')
    plt.title('Summary Chart of Account Holdings')
    plt.show()

    # Saving the chart to a PNG file
    plt.savefig(path)
    plt.close()

    return f"Chart saved successfully at {path}"