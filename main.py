import csv


def calculate(company_name):
    income_statement = "data/" + company_name + "/" + company_name + " Income Statement.csv"
    balance = "data/" + company_name + "/" + company_name + " Balance Sheet.csv"
    cash = "data/" + company_name + "/" + company_name + " Cash Flow.csv"

    file = open(income_statement)
    income_statement_reader = csv.reader(file)
    # Company Name
    finance_name = [name.replace("ï»¿", "") for name in next(income_statement_reader)][0]
    print(finance_name)

    file = open(balance)
    balance_reader = csv.reader(file)
    next(balance_reader)

    file = open(cash)
    cash_reader = csv.reader(file)
    next(cash_reader)

    income_statement_data = []

    for row in income_statement_reader:
        new_data_child = [row[0], row[1:]]
        income_statement_data.append(new_data_child)

    balance_data = []

    for row in balance_reader:
        new_data_child = [row[0], row[1:]]
        balance_data.append(new_data_child)

    cash_data = []

    for row in cash_reader:
        new_data_child = [row[0], row[1:]]
        cash_data.append(new_data_child)

    print(income_statement_data)
    print(balance_data)
    print(cash_data)

    year = [numeric_string for numeric_string in
            search_name_in_array("Fiscal year ends in September. USD in millions except per share data.", balance_data)]
    csv_data = [year]

    # Calculations
    # --------------------------------------------------------------------------------------------------------------
    print("Liquidity Ratio")
    current_assets = [float(numeric_string) for numeric_string in
                      search_name_in_array("Total current assets", balance_data)]

    current_liabilities = [float(numeric_string) for numeric_string in
                           search_name_in_array("Total current liabilities", balance_data)]

    current_ratio = [d1 / d2 for d1, d2 in zip(current_assets, current_liabilities)]
    print("Current Ratio", current_ratio)
    csv_data.append(current_ratio)

    inventories = [float(numeric_string) for numeric_string in
                   search_name_in_array("Inventories", balance_data)]

    acid_test_ratio = [d1 / d2 for d1, d2 in zip(inventories, current_liabilities)]
    print("Acid Test Ratio", acid_test_ratio)
    csv_data.append(acid_test_ratio)

    cash_and_cash_equivalents = [float(numeric_string) for numeric_string in
                                 search_name_in_array("Cash and cash equivalents", balance_data)]

    cash_ratio = [d1 / d2 for d1, d2 in zip(cash_and_cash_equivalents, current_liabilities)]
    print("Cash ratio", cash_ratio)
    csv_data.append(cash_ratio)

    # --------------------------------------------------------------------------------------------------------------
    print("Debt Ratio")
    total_assets = [float(numeric_string) for numeric_string in
                    search_name_in_array("Total assets", balance_data)]

    total_liabilities = [float(numeric_string) for numeric_string in
                         search_name_in_array("Total liabilities", balance_data)]

    total_debt_ratio = [d1 / d2 for d1, d2 in zip(total_liabilities, total_assets)]
    print("Total Debt Ratio", total_debt_ratio)
    csv_data.append(total_debt_ratio)

    short_term_debt = [float(numeric_string) for numeric_string in
                       search_name_in_array("Short-term debt", balance_data)]

    total_debt_ratio = [d1 / d2 for d1, d2 in zip(short_term_debt, total_liabilities)]
    print("Short-Term Debt Ratio", total_debt_ratio)
    csv_data.append(total_debt_ratio)

    ebit = [float(numeric_string) for numeric_string in
            search_name_in_array("EBITDA", income_statement_data)]

    interest_expense = [float(numeric_string) for numeric_string in
                        search_name_in_array("Interest Expense", income_statement_data)]

    times_interest_earned = [d1 / d2 for d1, d2 in zip(ebit, interest_expense)]
    print("Times interest earned", times_interest_earned[:len(times_interest_earned)-1])
    csv_data.append(times_interest_earned[:len(times_interest_earned)-1])
    # --------------------------------------------------------------------------------------------------------------
    print("Profitability Ratio")
    gross_profit = [float(numeric_string) for numeric_string in
                    search_name_in_array("Gross profit", income_statement_data)]

    sales = [float(numeric_string) for numeric_string in
             search_name_in_array("Sales, General and administrative", income_statement_data)]

    gross_profit_margin = [d1 / d2 for d1, d2 in zip(gross_profit, sales)]
    print("Gross profit margin", gross_profit_margin[:len(gross_profit_margin)-1])
    csv_data.append(gross_profit_margin[:len(gross_profit_margin)-1])

    operating_profit_margin = [d1 / d2 for d1, d2 in zip(ebit, sales)]
    print("Operating profit margin", operating_profit_margin[:len(operating_profit_margin)-1])
    csv_data.append(operating_profit_margin[:len(operating_profit_margin)-1])

    net_income = [float(numeric_string) for numeric_string in
                  search_name_in_array("Net income", income_statement_data)]

    net_profit_margin = [d1 / d2 for d1, d2 in zip(net_income, sales)]
    print("Net profit margin", net_profit_margin[:len(net_profit_margin)-1])
    csv_data.append(net_profit_margin[:len(net_profit_margin)-1])
    # --------------------------------------------------------------------------------------------------------------
    print("Efficiency Rate")

    total_asset_turnover = [d1 / d2 for d1, d2 in zip(sales, total_assets)]
    print("Total Asset Turnover", total_asset_turnover)
    csv_data.append(total_asset_turnover)

    fixed_assets = [float(numeric_string) for numeric_string in
                    search_name_in_array("Total non-current assets", balance_data)]

    fixed_asset_turnover = [d1 / d2 for d1, d2 in zip(sales, fixed_assets)]
    print("Fixed asset turnover", fixed_asset_turnover)
    csv_data.append(fixed_asset_turnover)

    accounts_receivable = [float(numeric_string) for numeric_string in
                           search_name_in_array("Accounts receivable", cash_data)]

    accounts_receivable_turnover = [d1 / d2 for d1, d2 in zip(sales, accounts_receivable)]
    print("Accounts receivable turnover", accounts_receivable_turnover[:len(accounts_receivable_turnover)-1])
    csv_data.append(accounts_receivable_turnover[:len(accounts_receivable_turnover)-1])

    with open("data/result.csv", 'w') as result_file:
        writer = csv.writer(result_file)
        writer.writerows(csv_data)
    # --------------------------------------------------------------------------------------------------------------


def search_name_in_array(search_name, array):
    for data in array:
        if data[0] == search_name:
            return data[1]


if __name__ == '__main__':
    # http://financials.morningstar.com/income-statement/is.html?t=AAPL&region=usa&culture=en-US
    # AAPL => Apple

    # http://financials.morningstar.com/income-statement/is.html?t=MSFT&region=usa&culture=en-US
    # MSFT => Microsoft

    value = input("Lütfen data klasörü altında bulunan bir şirketin finans kodunu giriniz:\n")
    value = value.upper()
    calculate(value)
