import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

chat_id = 1109095907  # Ваш chat ID, не меняйте название переменной


def solution(x, y) -> bool:
    alpha = 0.06
    res = ttest_ind(x, y, alternative='greater')
    if res.pvalue <= alpha:
        return True
    else:
        return False
