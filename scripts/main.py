import os
from expconfig.load_config import config_loader
from datavalidation import load_csv, transform_transactions, compare, create_exceptions_report, create_exceptions_chart

def main():
    locconfig = config_loader()

    script_directory = os.path.dirname(os.path.abspath(__file__))

    acc_input_file = os.path.join(os.path.dirname(script_directory),locconfig["raw"]["raw_data_dir"], locconfig["raw"]["account_filename"])

    acc_data = load_csv(acc_input_file)

    tra_input_file = os.path.join(os.path.dirname(script_directory),locconfig["raw"]["raw_data_dir"], locconfig["raw"]["transactions_filename"])

    tra_data = load_csv(tra_input_file)

    merged_df = transform_transactions(tra_data)

    merged_df = compare(acc_data, merged_df)

    exception_report_path = os.path.join(os.path.dirname(script_directory),locconfig["processed"]["pro_data_dir"], locconfig["processed"]["report_filename"])
    exceptions_chart_path = os.path.join(os.path.dirname(script_directory),locconfig["processed"]["pro_data_dir"], locconfig["processed"]["chart_filename"])

    create_exceptions_report(merged_df, exception_report_path)
    create_exceptions_chart(merged_df, exceptions_chart_path)

    return "Data validation completed successfully"

if __name__ == "__main__":
    main()
