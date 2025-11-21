"""
防呆計算機 - Foolproof Calculator
提供安全的數學運算功能
"""


def safe_division(dividend, divisor):
    """
    安全除法函數 - 提供防呆機制的除法運算
    
    Args:
        dividend: 被除數
        divisor: 除數
        
    Returns:
        float: 除法結果
        
    Raises:
        ValueError: 當除數為0時拋出錯誤
        TypeError: 當輸入不是數字時拋出錯誤
    """
    # 檢查輸入是否為數字
    if not isinstance(dividend, (int, float)) or not isinstance(divisor, (int, float)):
        raise TypeError("Both dividend and divisor must be numbers")
    
    # 檢查除數是否為0
    if divisor == 0:
        raise ValueError("Cannot divide by zero")
    
    # 執行除法運算
    return dividend / divisor
