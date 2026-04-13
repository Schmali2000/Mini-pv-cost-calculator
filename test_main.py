"""
Unit tests for Mini PV Cost Calculator.
Tests all functions with realistic PV scenarios and edge cases.
"""

import pytest
from main import annuity_factor, annualized_cost, specific_cost


def test_annuity_factor_typical():
    """Test typical PV scenario: 5% rate, 20 years."""
    result = annuity_factor(0.05, 20)
    expected = 0.08024278375655413  # Pre-computed reference
    assert abs(result - expected) < 1e-10


def test_annuity_factor_edge_cases():
    """Test edge cases for annuity_factor."""
    # Test invalid inputs
    with pytest.raises(ValueError):
        annuity_factor(0, 20)      # Zero rate
    with pytest.raises(ValueError):
        annuity_factor(0.05, 0)    # Zero years
    with pytest.raises(ValueError):
        annuity_factor(-0.01, 20)  # Negative rate


def test_annualized_cost_typical():
    """Test typical PV CAPEX: 100k€ investment."""
    result = annualized_cost(100000, 0.05, 20)
    expected = 8024.278375655413
    assert abs(result - expected) < 1e-10


def test_specific_cost_typical():
    """Test LCOE: 8024€/year, 15k kWh/year."""
    result = specific_cost(8024.278375655413, 15000)
    expected = 0.053495189171036086
    assert abs(result - expected) < 1e-10


def test_specific_cost_edge_case():
    """Test zero/negative output for specific_cost."""
    with pytest.raises(ValueError):
        specific_cost(1000, 0)     # Zero output
    with pytest.raises(ValueError):
        specific_cost(1000, -100)  # Negative output


def test_full_pipeline():
    """Test complete PV calculation pipeline."""
    rate, years, capex, output = 0.05, 20, 100000, 15000
    crf = annuity_factor(rate, years)
    ann_cost = annualized_cost(capex, rate, years)
    lcoe = specific_cost(ann_cost, output)
    
    assert 0.08 < crf < 0.09        # CRF range check
    assert 8000 < ann_cost < 8100   # Annual cost range
    assert 0.05 < lcoe < 0.06       # LCOE range check
