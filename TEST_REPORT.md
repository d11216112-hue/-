# 任務三：執行測試，觀察綠燈與紅燈結果

## 測試報告

### 一、綠燈測試結果（通過）

執行 Copilot 生成的單元測試後，所有預期的測試案例都通過，顯示為綠燈。

#### 執行指令：
```bash
python -m unittest test_calculator.py -v
```

#### 測試結果：
```
test_boundary_values (test_calculator.TestSafeDivision.test_boundary_values)
測試邊界值 ... ok
test_division_by_zero (test_calculator.TestSafeDivision.test_division_by_zero)
測試除以零的情況（最重要的防呆機制） ... ok
test_float_division (test_calculator.TestSafeDivision.test_float_division)
測試浮點數除法 ... ok
test_negative_division (test_calculator.TestSafeDivision.test_negative_division)
測試負數相除 ... ok
test_normal_division (test_calculator.TestSafeDivision.test_normal_division)
測試正常的數值相除 ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK
```

**結論**：所有 5 個測試案例都通過 ✅
- ✅ 正常的數值相除（test_normal_division）
- ✅ 負數相除（test_negative_division）
- ✅ 除以零的情況（test_division_by_zero）
- ✅ 邊界值相除（test_boundary_values）
- ✅ 浮點數除法（test_float_division）

這代表 `safe_division` 函式能正確處理各種情境，包含處理除以零的狀況，使程式不會當機。

---

### 二、紅燈測試結果（失敗）

當我們將 `safe_division` 函式中的「處理除以零」的程式碼註解或刪除後，再次執行單元測試，結果出現紅燈。

#### 如何觀察紅燈結果：

1. 開啟 `calculator.py` 檔案
2. 將處理除以零的程式碼註解掉：

```python
def safe_division(a, b):
    # # 處理除以零的情況
    # if b == 0:
    #     return None
    
    # 直接執行除法，不處理例外
    return a / b
```

3. 再次執行測試：
```bash
python -m unittest test_calculator.py -v
```

#### 預期的失敗結果：

```
test_division_by_zero (test_calculator.TestSafeDivision.test_division_by_zero)
測試除以零的情況（最重要的防呆機制） ... ERROR

======================================================================
ERROR: test_division_by_zero (test_calculator.TestSafeDivision.test_division_by_zero)
測試除以零的情況（最重要的防呆機制）
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_calculator.py", line XX, in test_division_by_zero
    self.assertIsNone(safe_division(10, 0))
  File "calculator.py", line XX, in safe_division
    return a / b
ZeroDivisionError: division by zero
```

---

### 三、哪個測試失敗？請簡單說明原因

**失敗的測試**：`test_division_by_zero` - 測試「當 b 為零時，safe_division 是否能妥善處理」的單元測試

**失敗原因**：
- 函式內部沒有處理除以零的例外（`ZeroDivisionError`）
- 當執行 `safe_division(10, 0)` 時，程式直接拋出 `ZeroDivisionError` 錯誤
- 測試預期函式應該返回 `None`，但實際上程式崩潰並拋出例外
- 因此測試無法通過

**證明的重要性**：
這也證明了防呆機制的重要性，能讓程式更加穩定安全。透過適當的錯誤處理：
1. 程式不會因為除以零而崩潰
2. 使用者能得到可預期的結果（返回 `None` 而非錯誤）
3. 系統的穩定性和可靠性大幅提升

---

## 測試涵蓋的情境

本專案的單元測試涵蓋了以下情境：

1. **正常數值相除**：測試一般的除法運算是否正確
2. **負數相除**：測試負數除法的各種組合
3. **除以零**：測試防呆機制，確保除以零時不會崩潰
4. **邊界值**：測試特殊數值如 0、1 等
5. **浮點數除法**：測試小數點運算的準確性

---

## 如何執行測試

### 執行所有測試：
```bash
python -m unittest test_calculator.py
```

### 執行詳細測試（顯示每個測試名稱）：
```bash
python -m unittest test_calculator.py -v
```

### 執行特定測試：
```bash
python -m unittest test_calculator.TestSafeDivision.test_division_by_zero
```
