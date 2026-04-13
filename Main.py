"""
Mini PV Cost Calculator - Core functions for PV financial metrics.
Extracted from energy economics coursework.
"""

def annuity_factor(rate: float, years: int) -> float:
    """
    Calculate capital recovery factor (annuity factor).
    
    Formula: CRF = r * (1 + r)^n / ((1 + r)^n - 1)
    
    Args:
        rate: Discount rate (e.g., 0.05 for 5%)
        years: Project lifetime (e.g., 20)
    
    Returns:
        Annuity factor.
    
    Raises:
        ValueError: If rate <= 0 or years <= 0.
    """
    if rate <= 0 or years <= 0:
        raise ValueError("Rate and years must be positive.")
    
    r_pow_n = (1 + rate) ** years
    crf = rate * r_pow_n / (r_pow_n - 1)
    return crf


def annualized_cost(investment: float, rate: float, years: int) -> float:
    """
    Annualize upfront CAPEX using annuity factor.
    
    Args:
        investment: Initial investment (e.g., 100000 €)
        rate: Discount rate
        years: Lifetime
    
    Returns:
        Annual cost in €/year.
    """
    crf = annuity_factor(rate, years)
    return investment * crf


def specific_cost(annual_cost: float, annual_output: float) -> float:
    """
    Simple LCOE proxy: annual cost per kWh.
    
    Args:
        annual_cost: Annualized cost (€/year)
        annual_output: Annual energy output (kWh/year)
    
    Returns:
        Specific cost (€/kWh).
    
    Raises:
        ValueError: If annual_output <= 0.
    """
    if annual_output <= 0:
        raise ValueError("Annual output must be positive.")
    
    return annual_cost / annual_output
