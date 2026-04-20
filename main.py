def annuity_factor(rate, years):
    return rate * (1 + rate) ** years / ((1 + rate) ** years - 1)


def annualized_cost(investment, rate, years, annual_om):
    return investment * annuity_factor(rate, years) + annual_om


def levelized_cost(total_annual_cost, annual_output):
    return total_annual_cost / annual_output
