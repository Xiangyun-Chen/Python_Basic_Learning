# 08_slicing_operations.py
# 掌握 Python 序列的强大工具 - 切片 (Slicing)

# --- 1. 切片的基本语法 ---
# 切片是对序列类型（如列表、元组、字符串）进行部分提取的操作。
# 语法: [start:end:step]
# - start: 起始索引（包含），留空则从头开始。
# - end: 结束索引（不包含），留空则到末尾结束。
# - step: 步长，默认为 1。可以为负数，表示反向提取。
# 切片操作返回的是一个新的序列，不会修改原始序列。

print("--- 场景1：基本切片 ---")
my_list = [0, 1, 2, 3, 4, 5, 6]
# 从索引 1 到索引 4 (不含4)，步长为 1
result1 = my_list[1:4] # 等同于 my_list[1:4:1]
print(f"列表 [1:4] -> {result1}")

my_tuple = (0, 1, 2, 3, 4, 5, 6)
# [:] 表示从头到尾复制整个序列
result2 = my_tuple[:]
print(f"元组 [:] -> {result2}, 这是一个副本\n")


# --- 2. 步长 (Step) 的应用 ---
print("--- 场景2：使用步长 ---")
my_str = "01234567"
# 从头到尾，每隔 2 个元素取一个 (取偶数索引的元素)
result3 = my_str[::2]
print(f"字符串 [::2] -> {result3}")

# 最常用的技巧：步长为 -1 表示完全反转序列
result4 = my_str[::-1]
print(f"字符串 [::-1] -> {result4}\n")


# --- 3. 反向切片 ---
print("--- 场景3：反向切片 ---")
# 当步长为负数时，start 和 end 的含义也应反向理解。
# start 应比 end 大。
my_list_rev = [0, 1, 2, 3, 4, 5, 6]
# 从索引 3 开始，反向取到索引 1 (不含1)
result5 = my_list_rev[3:1:-1]
print(f"列表 [3:1:-1] -> {result5}")

my_tuple_rev = (0, 1, 2, 3, 4, 5, 6)
# 从末尾开始，反向每隔 2 个元素取一个
result6 = my_tuple_rev[::-2]
print(f"元组 [::-2] -> {result6}\n")


# --- 4. 切片综合练习 ---
print("--- 场景4：切片综合练习 ---")
exercise_str = "月薪过万，员序程马黑来，nohtyP学"
print(f"原始字符串: '{exercise_str}'")

# 1. 倒序截取出 "黑马程序员"
# "黑"的索引是9，"员"的索引是5，从9取到5(不含)
result7 = exercise_str[9:4:-1]
print(f"反向切片结果: '{result7}'")

# 2. 知识回顾：split, replace 和切片结合
# 使用 split 分割
result8_list = exercise_str.split("，")
print(f"分割结果: {result8_list}")

# 先替换再反转，得到 "学Python,来黑马程序员,月薪过万"
result10_reversed = exercise_str[::-1]
print(f"完全反转后: '{result10_reversed}'")