import pandas as pd

def compare(account_df, transactions_df):
    required_columns = ['account_id', 'product_id']
    for df in [account_df, transactions_df]:
        for column in required_columns:
            if column not in df.columns:
                raise ValueError(f"Input DataFrame does not have required column: {column}")

    # Merging the dataframes
    merged_df = pd.merge(account_df, transactions_df, on=['account_id', 'product_id'], how='outer')

    # Adding a column to compare 'total_cashflow' and 'total_product_balance'
    merged_df['is_equal'] = merged_df['total_cashflow'] == merged_df['total_product_balance']

    # Adding a column to show the difference
    merged_df['difference'] = merged_df['total_cashflow'] - merged_df['total_product_balance']

    return merged_df