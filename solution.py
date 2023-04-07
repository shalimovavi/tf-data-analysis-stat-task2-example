import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1267315308 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    y = x - 0.059
    return max(y)/(pow((1+p)/2,1/n)+0.059), \ max(y)/(pow((1-p)/2,1/n)+0.059)
