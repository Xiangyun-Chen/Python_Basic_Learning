# 05_data_structures_tuple.py
# 学习 Python 中的不可变序列 - 元组 (Tuple)

# --- 1. 元组的定义 ---
# 元组 (Tuple) 是一个不可变的、有序的元素集合。
# 特点：用小括号 () 定义，一旦创建，其内部元素不可被修改、添加或删除。
# "不可变"是它与列表最核心的区别。

print("--- 场景1：创建元组 ---")
# 创建一个包含不同类型的元组
t1 = (1, "hello", True)
print(f"t1 的类型是 {type(t1)}，内容是: {t1}")

# 创建一个空元组
t2 = ()
t3 = tuple() # 也可以用 tuple() 函数创建
print(f"t2 是一个空元组: {t2}")

# 注意：创建只含一个元素的元组，必须在元素后加一个逗号 ","
t_single = ("hello",)
print(f"单元素元组 t_single 的类型是 {type(t_single)}\n")


# --- 2. 元组的访问、统计与遍历 ---
# 元组在“读”操作上和列表非常相似。
print("--- 场景2：读取元组内容 ---")
t4 = ("itcast", "python", 666, 100, 100)

# 通过索引访问元素 (和列表一样)
first_item = t4[0]
print(f"元组的第一个元素是: {first_item}")

# 使用 .index() 方法查找元素的索引
index_of_666 = t4.index(666)
print(f"元素 666 的索引是: {index_of_666}")

# 使用 .count() 方法统计元素出现的次数
count_of_100 = t4.count(100)
print(f"元素 100 在元组中出现了 {count_of_100} 次")

# 使用 len() 函数获取元组的长度
length_of_t4 = len(t4)
print(f"元组 t4 的总长度是: {length_of_t4}\n")

# 遍历元组 (和列表一样)
print("--- 使用 for 循环遍历元组 ---")
for item in t4:
    print(f"元组元素: {item}")
print("\n")

# --- 3. 元组的不可变性 (Immutability) ---
# 这是元组最重要的特性。尝试修改元组会引发 TypeError。
# 下面的代码如果取消注释，将会报错: TypeError: 'tuple' object does not support item assignment
# t4[0] = "new_value"


# --- 4. 元组的特殊情况：嵌套的可变对象 ---
# 元组本身的元素是不可变的，但如果元组中的某个元素本身是可变对象（如列表），
# 那么这个可变对象的内容是可以被修改的。
print("--- 场景3：元组嵌套列表 ---")
# 场景：记录学生信息，姓名和年龄是固定的，但兴趣爱好是可以改变的。
student_info = ("周杰伦", 11, ["football", "music"])
print(f"初始学生信息: {student_info}")

# 修改元组内的列表元素：这是允许的！
student_info[2].remove("football")  # 移除一个爱好
student_info[2].append("coding")    # 添加一个新爱好
print(f"更新后学生信息: {student_info}")

# 再次强调：我们修改的是列表 `["football", "music"]`，
# 而不是元组 `student_info` 的结构。元组的第2个元素永远指向那个列表。