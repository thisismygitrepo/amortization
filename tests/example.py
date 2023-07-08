

from amortization.schedule import amortization_schedule
from tabulate import tabulate
from amortization.amount import calculate_amortization_amount
import pandas as pd


# can choose period of loan?
# can I choose shared equity?
# why shared equity and docs don't match on sharing losses and on fate of equity after refinance?
# is there a gaurantee that HomeStart will alaways be no more than 2% above the market in IR ?
# No LMI in HomeStart,but then with Home Gaurantee there is no LMI either, so no advantage is added to HomeStart in calculations below.
# is their offset account?
# but I don't have LMI if I wanted to switch and I have home gaurantee.
# maximum initial deposit as ratio of PP?


"""
* maximize your payback, in shortest time to escape HomeStart high interest rate and refinance.
* Get smaller loan and maximum shared equity
"""


def main(ir):
    pp_raw = 600_000
    equity_rate = 0.25
    pp = pp_raw * (1 - equity_rate)
    deposit = 0.15 * pp
    print(deposit)
    principal = pp - deposit - 15_000
    no_lmi_principal = 0.8 * pp
    interest_rate = 1 / 26 * 0.01 * ir
    period = 26 * 40

    amount = calculate_amortization_amount(principal=principal, interest_rate=interest_rate, period=period)
    table = [x for x in amortization_schedule(principal=principal, interest_rate=interest_rate, period=period)]
    df = pd.DataFrame(table, columns=["Number", "Amount", "Interest", "Principal", "Balance"])
    df_split = df.query(f'Balance < {no_lmi_principal}')
    year_before_refinance = df_split.iloc[0].Number / 26
    interest_before_refinance = df.iloc[0: df_split.index[0]].Interest.sum()
    print(f"Periodic Payment: {amount}")
    print(f"Year before refinancing: {year_before_refinance}")
    print(f"Interest paid before refinancing {interest_before_refinance}")
    print("\n")
    return amount, year_before_refinance, interest_before_refinance


amount1, year_before_refinance1, interest_before_refinance1 = main(6.5)
amount2, year_before_refinance2, interest_before_refinance2 = main(8.5)
print(f"Interest difference = {interest_before_refinance2 - interest_before_refinance1}")
