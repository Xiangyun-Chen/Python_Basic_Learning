# 03_data_structures_string.py
# 深入探索 Python 的文本序列 - 字符串 (String)

# --- 1. 字符串的本质与特性 ---
# 字符串 (String) 是一个由字符组成的不可变序列。
# 特点：
# 1. 不可变性：和元组一样，字符串一旦创建就不能被修改。任何修改操作都会返回一个新字符串。
# 2. 序列特性：可以用索引访问，可以被遍历。

print("--- 场景1：字符串的索引与长度 ---")
my_str = "itheima and itcast"
print(f"原始字符串: '{my_str}'")

# 通过索引访问单个字符 (同列表和元组)
char_at_2 = my_str[2]
print(f"索引为 2 的字符是: '{char_at_2}'")

# 使用 len() 函数获取字符串的长度 (字符总数)
str_length = len(my_str)
print(f"字符串的总长度是: {str_length}\n")


# --- 2. 字符串的查找与统计 ---
print("--- 场景2：查找与统计 ---")
# .index(): 查找子字符串第一次出现的起始索引。如果找不到会报错。
index_of_and = my_str.index("and")
print(f"子字符串 'and' 的起始索引是: {index_of_and}")

# .count(): 统计子字符串在字符串中出现的次数。
count_of_it = my_str.count("it")
print(f"子字符串 'it' 出现了 {count_of_it} 次\n")


# --- 3. 字符串的修改与转换 (返回新字符串) ---
# 记住：所有这些方法都不会改变原字符串，而是返回一个新的字符串。
print("--- 场景3：修改与转换 ---")
original_str = "  itheima and itcast  "
print(f"待处理的原始字符串: '{original_str}'")

# .replace(): 替换字符串中的指定内容。
# 将所有的 "it" 替换为 "程序"
new_str_1 = original_str.replace("it", "程序")
print(f"使用 replace 替换后: '{new_str_1}'")

# .strip(): 去除字符串首尾的空白字符（空格、换行符、制表符）。
# 也可以指定要去除的字符集。
new_str_2 = original_str.strip()
print(f"使用 strip 去除首尾空格后: '{new_str_2}'")

# 示例：去除首尾的指定字符
test_strip = "12abcheaderabc12"
print(f"去除'12abc'后的结果: '{test_strip.strip('12abc')}'")


# .split(): 将字符串按照指定的分隔符分割成一个列表 (List)。
new_str_3_list = new_str_2.split(" and ")
print(f"使用 split 分割后得到列表: {new_str_3_list}, 类型是 {type(new_str_3_list)}\n")


# --- 4. 综合练习 ---
print("--- 场景4：综合练习 ---")
exercise_str = "itheima itcast boxuegu"
print(f"练习字符串: '{exercise_str}'")

# 1. 统计 "it" 出现的次数
it_count = exercise_str.count("it")
print(f"1. 字符串中有 {it_count} 个 'it'")

# 2. 将所有空格替换为竖线 "|"
replaced_str = exercise_str.replace(" ", "|")
print(f"2. 将空格替换为'|'后: '{replaced_str}'")

# 3. 再按 "|" 进行分割，得到一个列表
final_list = replaced_str.split("|")
print(f"3. 按'|'分割后得到列表: {final_list}")