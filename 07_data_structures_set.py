# 07_data_structures_set.py
# 学习 Python 中的无序去重容器 - 集合 (Set)

# --- 1. 集合的定义与特性 ---
# 集合 (Set) 是一个无序的、不含重复元素的容器。
# 特点：
# 1. 自动去重：集合内的元素是唯一的，重复添加的元素会被忽略。
# 2. 无序性：集合不记录元素的位置或插入顺序，因此不能使用索引访问。
# 主要用途：高效地去除重复项、进行成员资格测试以及执行数学集合运算。

print("--- 场景1：创建集合 ---")
# 使用花括号 {} 创建集合，集合会自动去除重复的 "python" 和 "it"
my_set = {"itcast", "python", "it", "python", "it"}
print(f"my_set 内容是 {my_set}, 类型是 {type(my_set)}")

# 创建空集合必须使用 set() 函数，因为 {} 用于创建空字典。
empty_set = set()
print(f"empty_set 内容是 {empty_set}, 类型是 {type(empty_set)}\n")


# --- 2. 集合的常用方法 ---
print("--- 场景2：增删改查 ---")
# .add(): 添加一个元素到集合中。如果元素已存在，则无效果。
my_set.add("heima")
my_set.add("it") # "it" 已存在，此操作无效
print(f"添加元素后: {my_set}")

# .remove(): 从集合中移除一个指定的元素。如果元素不存在，会报错 KeyError。
my_set.remove("itcast")
print(f"移除 'itcast' 后: {my_set}")

# .pop(): 随机从集合中移除一个元素并返回它。对空集合操作会报错。
popped_element = my_set.pop()
print(f"随机弹出一个元素 '{popped_element}' 后: {my_set}")

# len(): 获取集合中元素的数量
num_elements = len(my_set)
print(f"当前集合有 {num_elements} 个元素\n")

# 遍历集合 (注意：遍历顺序是不确定的)
print("--- 遍历集合元素 ---")
set_to_iterate = {1, 2, 3, 4, 5}
for element in set_to_iterate:
    print(f"集合元素: {element}")
print("")


# --- 3. 集合的数学运算 ---
print("--- 场景3：集合的数学运算 ---")
set1 = {1, 2, 3}
set2 = {1, 5, 6}
print(f"原始集合: set1={set1}, set2={set2}")

# .difference() 或 - : 计算差集 (在 set1 中但不在 set2 中的元素)，返回新集合。
diff_set = set1.difference(set2)
print(f"set1 和 set2 的差集是: {diff_set}")
print(f"原集合不变: set1={set1}, set2={set2}")

# .difference_update(): 从 set1 中移除两个集合的共同元素，直接修改原集合。
set1_copy = set1.copy() # 复制一个副本进行操作
set1_copy.difference_update(set2)
print(f"set1 执行 difference_update 后: {set1_copy}")

# .union() 或 | : 计算并集 (两个集合的所有元素)，返回新集合。
union_set = set1.union(set2)
print(f"set1 和 set2 的并集是: {union_set}\n")


# --- 4. 集合的应用：列表去重 ---
print("--- 场景4：列表去重练习 ---")
my_list = ["黑马程序员", "传智播客", "黑马程序员", "传智播客", "itheima", "itcast", "itheima", "itcast", "best"]
print(f"原始列表: {my_list}")

# 利用集合的自动去重特性
unique_set = set(my_list)
print(f"转换为集合后，实现去重: {unique_set}")

# 如果需要去重后的列表，可以再转换回来
unique_list = list(unique_set)
print(f"去重后的列表: {unique_list}")