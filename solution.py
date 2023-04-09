import pandas as pd
import numpy as np
from scipy.stats import mannwhitneyu

chat_id = 1109095907  # Ваш chat ID, не меняйте название переменной


def solution(x, y) -> bool:
    alpha = 0.06
    res = mannwhitneyu(x, y, alternative='greater', method='asymptotic')
    if res.pvalue <= alpha:
        return True
    else:
        return False
