# 02_io_operations.py
# 演示 Python 中的输入(input)和输出(print)操作

# --- 1. 基础 print 和 input ---
# 场景：程序与用户进行简单交互，获取用户名并打招呼。
print("--- 场景1：基础 print 和 input ---")
# input() 函数会暂停程序，等待用户输入，并返回一个字符串
user_name = input("请输入你的名字：") 
print(f"你好，{user_name}！\n") # 这里使用了 f-string 格式化，更直观


# --- 2. 字符串格式化输出 ---
# 场景：将多个变量优雅地组合成一句话进行输出。
print("--- 场景2：字符串格式化输出 (f-string) ---")
name = "小明"
age = 20
city = "上海"
# f-string 是目前最推荐的字符串格式化方式
print(f"大家好，我叫{name}，今年{age}岁，我来自{city}。\n")


# --- 3. print() 函数的高级用法 ---
# 场景：需要将多个 print 的内容输出到同一行。
# 默认情况下，print() 函数会在输出末尾添加一个换行符。
# 我们可以通过 `end` 参数来修改末尾的字符，实现不换行输出。
print("--- 场景3：print 高级用法 ---")
print("Hello", end='') # 末尾不加任何字符
print("World", end='---') # 末尾添加 '---'
print("END")
# 上面三行代码最终的输出会是：HelloWorld---END