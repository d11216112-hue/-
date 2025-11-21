"""
示範腳本：展示綠燈與紅燈測試結果
此腳本會自動展示有防呆機制和沒有防呆機制的差異
"""

import sys
from calculator import safe_division


def demonstrate_green_light():
    """展示綠燈測試（有防呆機制）"""
    print("=" * 60)
    print("🟢 綠燈測試：有防呆機制的 safe_division 函式")
    print("=" * 60)
    
    test_cases = [
        (10, 2, "正常除法"),
        (-10, 2, "負數除法"),
        (10, 0, "除以零（防呆機制）"),
        (0, 5, "零除以數字"),
        (7, 2, "浮點數結果"),
    ]
    
    all_passed = True
    for a, b, description in test_cases:
        result = safe_division(a, b)
        expected = None if b == 0 else a / b
        passed = result == expected
        all_passed = all_passed and passed
        
        status = "✅ 通過" if passed else "❌ 失敗"
        print(f"\n測試：{description}")
        print(f"  運算：{a} ÷ {b}")
        print(f"  結果：{result}")
        print(f"  狀態：{status}")
    
    print("\n" + "=" * 60)
    if all_passed:
        print("✅ 所有測試通過！程式具有良好的防呆機制。")
    else:
        print("❌ 有測試失敗！")
    print("=" * 60)
    return all_passed


def demonstrate_red_light():
    """展示紅燈測試（沒有防呆機制）"""
    print("\n\n" + "=" * 60)
    print("🔴 紅燈測試：沒有防呆機制的除法")
    print("=" * 60)
    print("\n說明：以下展示如果直接使用 Python 的除法運算子")
    print("      而不處理除以零的情況會發生什麼事...\n")
    
    def unsafe_division(a, b):
        """不安全的除法，沒有錯誤處理"""
        return a / b
    
    test_cases = [
        (10, 2, "正常除法"),
        (10, 0, "除以零（會引發錯誤！）"),
    ]
    
    for a, b, description in test_cases:
        print(f"測試：{description}")
        print(f"  運算：{a} ÷ {b}")
        try:
            result = unsafe_division(a, b)
            print(f"  結果：{result}")
            print(f"  狀態：✅ 通過")
        except ZeroDivisionError as e:
            print(f"  結果：❌ 程式崩潰！")
            print(f"  錯誤：ZeroDivisionError - {e}")
            print(f"  狀態：🔴 失敗（未處理除以零）")
        print()
    
    print("=" * 60)
    print("⚠️  沒有防呆機制的程式在遇到除以零時會崩潰！")
    print("✅ 這就是為什麼 safe_division 的防呆機制如此重要。")
    print("=" * 60)


def main():
    """主程式"""
    print("\n" + "🚀 " * 20)
    print("防呆計算機測試示範")
    print("🚀 " * 20 + "\n")
    
    # 展示綠燈測試
    green_passed = demonstrate_green_light()
    
    # 展示紅燈測試
    demonstrate_red_light()
    
    # 總結
    print("\n\n" + "=" * 60)
    print("📝 總結")
    print("=" * 60)
    print("""
1. 🟢 綠燈測試證明：
   - safe_division 函式能正確處理各種情境
   - 除以零時不會崩潰，而是返回 None
   - 所有測試案例都能通過

2. 🔴 紅燈測試證明：
   - 沒有防呆機制的程式會在除以零時崩潰
   - 直接拋出 ZeroDivisionError 例外
   - 這會導致程式不穩定

3. 💡 學習重點：
   - 防呆機制能讓程式更加穩定安全
   - 單元測試能幫助我們驗證程式的正確性
   - 綠燈/紅燈測試是 TDD（測試驅動開發）的核心概念
    """)
    print("=" * 60)


if __name__ == "__main__":
    main()
