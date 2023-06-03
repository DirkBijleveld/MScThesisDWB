from pandas import DataFrame
from statsmodels.formula.api import quantreg
from statsmodels.regression.linear_model import RegressionResultsWrapper


def quantile(formula: str, frame: DataFrame) -> RegressionResultsWrapper:
    return quantreg(formula, data=frame).fit()


def make_formula(dependent: str, *independent: str) -> str:
    return dependent + " ~ " + " + ".join(independent)
