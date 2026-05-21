# 03_control_flow.py
# 演示 Python 中的流程控制语句
import random # 将 import 语句放在文件顶部，这是 PEP8 规范

# --- 1. 基础 if 语句 ---
# 场景：判断年龄是否成年
print("--- 场景1：基础 if 语句 ---")
age = 20
if age >= 18:
    print("你已经成年了。\n")


# --- 2. if...else 结构 ---
# 场景：根据考试成绩判断是否及格
print("--- 场景2：if...else 结构 ---")
score = 55
if score >= 60:
    print("考试及格。\n")
else:
    print("考试不及格，需要补考。\n")


# --- 3. if...elif...else 结构 ---
# 场景：根据不同的分数段给予不同的评级
print("--- 场景3：if...elif...else 结构 ---")
score = 85
if score >= 90:
    print("评级：优秀\n")
elif score >= 80:
    print("评级：良好\n")
elif score >= 60:
    print("评级：合格\n")
else:
    print("评级：不合格\n")


# --- 4. 嵌套 if 语句 ---
# 场景：检查门票，需要同时满足级别和携带物品要求
print("--- 场景4：嵌套 if 语句 ---")
vip_level = 3
has_dangerous_item = False
if vip_level > 0:
    print("欢迎VIP用户！")
    if not has_dangerous_item:
        print("安检通过，请入场。\n")
    else:
        print("检测到危险物品，禁止入场！\n")
else:
    print("非VIP用户，请购买门票。\n")


# --- 5. 基础 while 循环 ---
# 场景：重复打印数字
print("--- 场景5：基础 while 循环 ---")
i = 1
while i <= 3:
    print(f"这是第 {i} 次循环")
    i += 1
print("")


# --- 6. while 循环与布尔标志位 ---
# 场景：模拟一个需要用户输入正确密码才能退出的程序
print("--- 场景6：while 循环与布尔标志位 ---")
is_running = True
while is_running:
    password = input("请输入密码 (输入'exit'退出): ")
    if password == "12345":
        print("密码正确，程序退出。")
        is_running = False
    elif password == "exit":
        print("用户选择退出。")
        is_running = False
    else:
        print("密码错误！")
print("")


# --- 7. for 循环遍历序列 ---
# 场景：统计字符串中特定字符的数量
print("\n--- 场景7：for 循环遍历字符串 ---")
my_string = "itheima is a brand of itcast"
char_count = 0
for char in my_string:
    if char == "a":
        char_count += 1
print(f"字符串 '{my_string}' 中含有 {char_count} 个 'a' 字母。\n")


# --- 8. range() 函数 ---
# 场景：生成一系列数字用于循环
print("--- 场景8：range() 函数 ---")
# range(stop): 从 0 开始到 stop-1
print("range(5):", end=' ')
for i in range(5):
    print(i, end=' ')
# range(start, stop): 从 start 开始到 stop-1
print("\nrange(2, 8):", end=' ')
for i in range(2, 8):
    print(i, end=' ')
# range(start, stop, step): 从 start 开始到 stop-1，步长为 step
print("\nrange(1, 10, 2):", end=' ')
for i in range(1, 10, 2):
    print(i, end=' ')
print("\n")


# --- 9. 循环嵌套 (打印九九乘法表) ---
print("--- 场景9：for 循环嵌套打印九九乘法表 ---")
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}*{i}={j*i}\t", end='')
    print()
print()


# --- 10. 循环控制 `break` 和 `continue` ---
# 场景：模拟发工资，当余额不足时停止(break)，当员工绩效不达标时跳过(continue)。
print("--- 场景10：使用 break 和 continue ---")
total_money = 10000
for employee_id in range(1, 21):
    performance_score = random.randint(1, 10)
    
    if performance_score < 5:
        print(f"员工 {employee_id}，绩效分 {performance_score}，不达标，跳过。")
        continue # 跳过本次循环中余下的代码，直接开始下一次循环

    # 绩效达标，准备发工资
    if total_money >= 1000:
        total_money -= 1000
        print(f"向员工 {employee_id} 发放工资1000元，账户余额还剩 {total_money} 元。")
    else:
        print(f"余额不足，无法为员工 {employee_id} 发放工资。")
        print("工资已发完！")
        break # 余额不足，使用 break 彻底终止整个发工资循环

print("--- 发放结束 ---")
