# 防呆計算機情境

## 任務三：執行測試，觀察綠燈與紅燈結果

本專案展示如何使用單元測試來驗證程式的防呆機制（以 `safe_division` 函式為例）。

### 📁 專案檔案結構

```
.
├── calculator.py          # 包含 safe_division 函式的主程式
├── test_calculator.py     # 單元測試檔案
├── demo.py               # 展示綠燈/紅燈測試結果的示範腳本
├── TEST_REPORT.md        # 完整的測試報告
└── README.md             # 本檔案
```

### 🚀 快速開始

#### 1. 執行單元測試（綠燈測試）

```bash
python -m unittest test_calculator.py -v
```

**預期結果**：所有 5 個測試案例都通過 ✅
- 正常的數值相除
- 負數相除
- 除以零的情況（防呆機制）
- 邊界值相除
- 浮點數除法

#### 2. 執行示範腳本

```bash
python demo.py
```

這個腳本會自動展示：
- 🟢 有防呆機制的情況（綠燈）
- 🔴 沒有防呆機制的情況（紅燈）

#### 3. 觀察紅燈測試

如果要手動觀察紅燈測試結果：

1. 開啟 `calculator.py`
2. 將 `safe_division` 函式修改為：
   ```python
   def safe_division(a, b):
       return a / b  # 直接除法，不處理例外
   ```
3. 再次執行測試：
   ```bash
   python -m unittest test_calculator.py -v
   ```
4. 觀察 `test_division_by_zero` 測試失敗並拋出 `ZeroDivisionError`

### 📊 測試結果說明

#### 🟢 綠燈（通過）
- 執行單元測試後，所有測試案例都通過
- `safe_division` 函式能正確處理各種情境，包含除以零
- 程式不會當機，具有良好的防呆機制

#### 🔴 紅燈（失敗）
- 當移除防呆機制後，`test_division_by_zero` 測試失敗
- 程式直接拋出 `ZeroDivisionError` 例外
- 這證明了防呆機制對程式穩定性的重要性

### 📝 詳細報告

請查看 [TEST_REPORT.md](TEST_REPORT.md) 以獲得完整的測試報告和說明。

### 💡 學習重點

1. **防呆機制的重要性**：能讓程式更加穩定安全
2. **單元測試的價值**：幫助驗證程式的正確性
3. **綠燈/紅燈測試**：TDD（測試驅動開發）的核心概念

### 🎯 問題解答

**哪個測試失敗？請簡單說明原因：**

失敗的是測試「當 b 為零時，safe_division 是否能妥善處理」的單元測試（`test_division_by_zero`）。

**原因**：函式內部沒有處理除以零的例外，導致執行時拋出 `ZeroDivisionError` 錯誤，測試無法通過。因此，這也證明了防呆機制的重要性，能讓程式更加穩定安全。
