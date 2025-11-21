# 防呆計算機 (Foolproof Calculator)

這個專案實作了一個防呆的除法函式，可以防止除以零的錯誤。

## 任務一：safe_division 函式

### 功能說明
`safe_division(a, b)` 函式提供了安全的除法運算，能夠：
- 執行正常的除法運算
- 防止除以零的錯誤
- 當除數為零時，返回 `None` 而不是拋出異常

### 使用方法

```python
from safe_division import safe_division

# 正常除法
result = safe_division(10, 2)  # 返回 5.0

# 除以零（防呆處理）
result = safe_division(10, 0)  # 返回 None

# 實際應用
numerator = 100
denominator = 5
result = safe_division(numerator, denominator)

if result is None:
    print(f"錯誤：無法除以 {denominator}")
else:
    print(f"{numerator} / {denominator} = {result}")
```

### 檔案說明
- `safe_division.py` - 主要的 safe_division 函式實作
- `test_safe_division.py` - 單元測試
- `example.py` - 使用範例

### 執行測試

```bash
python3 -m unittest test_safe_division.py -v
```

### 執行範例

```bash
python3 example.py
```
