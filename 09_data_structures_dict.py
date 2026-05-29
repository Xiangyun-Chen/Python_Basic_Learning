# 09_data_structures_dict.py
# 学习 Python 最核心的键值对容器 - 字典 (Dictionary)

# --- 1. 字典的定义与特性 ---
# 字典 (Dictionary) 是一个可变的、无序的（在 Python 3.7+ 中为有序）键值对集合。
# 特点：
# 1. 键值对 (key-value pair): 每个元素都由一个唯一的键和对应的值组成。
# 2. 键的唯一性: 字典中的键必须是唯一的，且通常是不可变类型（如字符串、数字、元组）。
# 3. 高效查询: 通过键来访问值，速度非常快，远胜于在列表中搜索。
# 4. 可变性: 可以随时添加、修改或删除键值对。

print("--- 场景1：创建字典 ---")
# 使用花括号 {} 创建字典
my_dict = {"小红": 95, "张三": 93, "小明": 88}
print(f"字典1内容为 {my_dict}, 类型为 {type(my_dict)}")

# 创建空字典
my_dict2 = {}
my_dict3 = dict()
print(f"字典2和3都是空字典: {my_dict2}, {my_dict3}\n")


# --- 2. 字典的访问、新增与修改 ---
print("--- 场景2：访问与修改 ---")
# 通过键获取值
score = my_dict["小红"]
print(f"小红的考试分数是: {score}")

# 新增键值对
my_dict["小丽"] = 66
print(f"新增'小丽'后: {my_dict}")

# 修改已存在的键对应的值
my_dict["小红"] = 90
print(f"更新'小红'的分数后: {my_dict}\n")


# --- 3. 字典的删除与清空 ---
print("--- 场景3：删除元素 ---")
# .pop(): 移除指定的键值对，并返回被移除的键对应的值。
removed_score = my_dict.pop("小红")
print(f"移除'小红'后字典为 {my_dict}，被移除的分数是 {removed_score}")

# .clear(): 清空字典内的所有键值对
my_dict.clear()
print(f"清空字典后: {my_dict}\n")


# --- 4. 字典的遍历 ---
print("--- 场景4：遍历字典 ---")
stu_scores = {"小红": 95, "张三": 93, "小明": 88}
print(f"待遍历的字典: {stu_scores}")
print(f"字典中共有 {len(stu_scores)} 个元素。\n")

# 方法一：直接遍历字典（推荐）
# for循环直接遍历字典，得到的是每一个键(key)
print("--- 推荐的遍历方式 ---")
for name in stu_scores:
    score = stu_scores[name]
    print(f"学生: {name}, 分数: {score}")

# 方法二：遍历 .keys()
# .keys() 方法会获取字典中所有的键
print("\n--- 遍历 keys() 的方式 ---")
for name in stu_scores.keys():
    score = stu_scores[name]
    print(f"学生: {name}, 分数: {score}")
print("")


# --- 5. 嵌套字典与综合练习 ---
print("--- 场景5：嵌套字典与综合应用 ---")
# 嵌套字典非常适合表示结构化的信息
staff_info = {
    "王力鸿": {"部门": "科技部", "工资": 3000, "级别": 1},
    "周杰轮": {"部门": "市场部", "工资": 5000, "级别": 2},
    "林俊节": {"部门": "市场部", "工资": 7000, "级别": 3},
    "张学油": {"部门": "科技部", "工资": 4000, "级别": 1},
    "刘德滑": {"部门": "科技部", "工资": 6000, "级别": 2}
}
print(f"原始员工信息:\n{staff_info}\n")

# 需求：为所有级别为 1 的员工涨薪1000元，并将级别提升到 2
for name in staff_info:
    # 检查员工级别
    if staff_info[name]["级别"] == 1:
        # 直接修改嵌套字典中的值
        staff_info[name]["工资"] += 1000
        staff_info[name]["级别"] = 2

print(f"批量加薪后员工信息:\n{staff_info}")