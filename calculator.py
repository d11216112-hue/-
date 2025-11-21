"""
防呆計算機模組
包含安全除法函式，能妥善處理除以零的情況
"""


def safe_division(a, b):
    """
    安全除法函式
    
    參數:
        a: 被除數
        b: 除數
    
    返回:
        除法結果，若除數為零則返回 None
    
    範例:
        >>> safe_division(10, 2)
        5.0
        >>> safe_division(10, 0)
        None
    """
    # 處理除以零的情況
    if b == 0:
        return None
    return a / b
