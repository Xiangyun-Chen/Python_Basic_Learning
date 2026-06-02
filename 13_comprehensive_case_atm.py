# 13_综合案例_ATM.py
# 综合运用函数、循环和判断，模拟一个简单的ATM机操作流程。

# --- 全局变量定义 ---
# 模拟账户初始余额
account_balance = 5000000
# 在程序开始时获取用户名，后续操作都针对此用户
user_name = input("请输入您的姓名: ")


# --- 功能函数定义 ---

def query_balance(show_header):
    """
    查询并打印当前账户余额。
    :param show_header: 布尔值，如果为 True，则打印查询标题。
    """
    if show_header:
        print("------- 查询余额 -------")
    print(f"{user_name}，您好，您的账户余额为: {account_balance} 元")

def deposit(amount):
    """
    执行存款操作，并更新全局余额。
    :param amount: 要存入的金额 (int)。
    """
    global account_balance
    account_balance += amount
    print("------- 存款操作 -------")
    print(f"成功存入 {amount} 元。")
    # 存款后，调用查询函数显示最新余额，且不显示标题
    query_balance(False)

def withdraw(amount):
    """
    执行取款操作，并更新全局余额。
    在取款前会检查余额是否充足。
    :param amount: 要取出的金额 (int)。
    """
    global account_balance
    print("------- 取款操作 -------")
    # 增加关键判断：检查余额是否足够
    if amount > account_balance:
        print(f"操作失败！您的余额不足，无法取出 {amount} 元。")
    else:
        account_balance -= amount
        print(f"成功取出 {amount} 元。")
    # 无论成功与否，都调用查询函数显示最新余额
    query_balance(False)

def main_menu():
    """
    打印主菜单并获取用户的选择。
    :return: 用户输入的选择 (str)。
    """
    print("\n-------- ATM 主菜单 --------")
    print(f"{user_name}，您好，欢迎使用ATM。")
    print("查询余额\t[输入 1]")
    print("存款\t\t[输入 2]")
    print("取款\t\t[输入 3]")
    print("退出\t\t[输入 4]")
    return input("请输入您的操作选择: ")

# --- 主程序执行 ---
# `if __name__ == '__main__':` 是Python的推荐写法，
# 它确保只有当这个文件被直接执行时，下面的代码块才会运行。
if __name__ == '__main__':
    while True:
        choice = main_menu()

        if choice == "1":
            query_balance(True)
        elif choice == "2":
            # 这里可以增加try-except来防止用户输入非数字，但目前保持简单
            deposit_amount = int(input("请输入您要存款的金额: "))
            deposit(deposit_amount)
        elif choice == "3":
            withdraw_amount = int(input("请输入您要取款的金额: "))
            withdraw(withdraw_amount)
        elif choice == "4":
            print("感谢您的使用，程序已退出。")
            break # 退出 while 循环
        else:
            print("无效输入，请重新选择。")
        
        # 使用 continue 不是必需的，因为 if-elif 结构本身就会执行完一个分支后
        # 自然地回到 while 循环的开头开始下一次循环。