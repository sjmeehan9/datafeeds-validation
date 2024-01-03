import pandas as pd

def transform_transactions(df):
    required_columns = ['transaction_type', 'account_id', 'product_id', 'amount']
    for column in required_columns:
        if column not in df.columns:
            raise ValueError(f"Input DataFrame does not have required column: {column}")

    # Filter and sum deposits
    deposit_sums = df[df['transaction_type'] == 'deposit'].groupby(['account_id', 'product_id']).amount.sum().reset_index()
    deposit_sums.rename(columns={'amount': 'total_deposit'}, inplace=True)

    # Filter and sum withdrawals, make them negative
    withdrawal_sums = df[df['transaction_type'] == 'withdrawal'].groupby(['account_id', 'product_id']).amount.sum().reset_index()
    withdrawal_sums['amount'] = -withdrawal_sums['amount']
    withdrawal_sums.rename(columns={'amount': 'total_withdrawal'}, inplace=True)

    # Merge the sums into a single DataFrame
    merged_df = pd.merge(deposit_sums, withdrawal_sums, on=['account_id', 'product_id'], how='outer')

    # Replace NaN values with 0 (for cases where there are only deposits or only withdrawals)
    merged_df.fillna(0, inplace=True)

    # Add a new column that totals the 'total_withdrawal' and 'total_deposit' columns
    merged_df['total_cashflow'] = merged_df['total_deposit'] + merged_df['total_withdrawal']

    return merged_df