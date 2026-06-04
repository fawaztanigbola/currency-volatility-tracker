import pytest

from main import CurrencyAnalyzer, CurrencyDataPoint

def test_currency_analyzer_math():
    # The triple AAA for pytest - Arrange, Act and Assert
    # Arrange
    analysis = CurrencyAnalyzer()
    analysis.datapoints = [
        CurrencyDataPoint("2026-03-01", 1.0),
        CurrencyDataPoint("2026-03-02", 2.0),
        CurrencyDataPoint("2026-03-03", 3.0)
    ]

    # Act
    calculate_mean = analysis.calculate_mean()
    calculate_variance = analysis.calculate_variance()
    calculate_volatility = analysis.calculate_volatility()

    # Assert
    assert calculate_mean == 2.0
    assert calculate_variance == pytest.approx(0.666666667)
    assert calculate_volatility == pytest.approx(0.666666667**0.5)

def test_empty_analyzer():
    empty_analysis = CurrencyAnalyzer()

    assert empty_analysis.get_total_days() == 0
    assert empty_analysis.calculate_mean() == 0.0
    assert empty_analysis.calculate_mean() == 0.0
    assert empty_analysis.calculate_volatility() == 0.0
