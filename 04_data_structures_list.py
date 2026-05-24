# 04_data_structures.py
# 深入探索 Python 中最核心的数据结构 - 列表 (List)

# --- 1. 创建列表与基本信息 ---
print("--- 场景1：创建与查看列表 ---")
# 列表是可变的、有序的元素集合。
# 我们来创建一个班级学生名单
students = ["张三", "李四", "王五", "赵六"]
print(f"初始学生名单: {students}")

# 使用 len() 函数获取列表中的元素总数
num_of_students = len(students)
print(f"当前班级总人数: {num_of_students}\n")


# --- 2. 访问、查找与修改元素 ---
print("--- 场景2：访问、查找与修改 ---")
# 访问：通过索引获取元素 (索引从0开始)
first_student = students[0]
last_student = students[-1]
print(f"第一个学生是 '{first_student}'，最后一个学生是 '{last_student}'")

# 查找：使用 .index() 方法查找元素的索引
index_of_wangwu = students.index("王五")
print(f"'王五' 同学的座位号 (索引) 是: {index_of_wangwu}")

# 修改：通过索引直接赋值
print(f"修改前: {students}")
students[1] = "李四郎"  # '李四' 改名为 '李四郎'
print(f"修改后: {students}\n")


# --- 3. 添加新元素 ---
print("--- 场景3：添加新同学 ---")
# .append(): 在列表末尾追加一个元素
students.append("钱七")
print(f"append '钱七' 后: {students}")

# .insert(): 在指定索引位置插入一个元素
students.insert(1, "新同学")
print(f"在索引 1 处 insert '新同学' 后: {students}")

# .extend(): 将另一个列表的多个元素全部追加到末尾
new_students = ["孙八", "周九"]
students.extend(new_students)
print(f"extend 一个新列表后: {students}\n")


# --- 4. 删除元素 ---
print("--- 场景4：移除同学 ---")
# .remove(): 根据值删除第一个匹配的元素
students.remove("新同学")
print(f"remove '新同学' 后: {students}")

# .pop(): 根据索引删除元素，并返回被删除的元素。不写索引默认删除最后一个。
graduated_student = students.pop(2) # '王五'毕业了
print(f"pop 索引为2的 '{graduated_student}' 后: {students}")

# del 关键字：根据索引删除元素
del students[0] # '张三'转学了
print(f"del 索引为0的元素后: {students}")

# .clear(): 清空整个列表
students.clear()
print(f"调用 clear() 后，名单被清空: {students}\n")


# --- 5. 统计与遍历 ---
print("--- 场景5：统计与遍历 ---")
students = ["张三", "李四", "王五", "赵六"]
# 假设又来了一个叫'赵六'的同学
students.append("赵六")
print(f"当前名单: {students}")

# .count(): 统计某个元素出现的次数
count_zhao_liu = students.count("赵六")
print(f"名单里叫 '赵六' 的同学有 {count_zhao_liu} 位")

# 使用 for 循环遍历列表，是处理列表中每个元素的标准方式
print("--- 点名时间 ---")
for student in students:
    print(f"{student}，到！")
print("\n")


# --- 6. 嵌套列表 ---
print("--- 场景6：嵌套列表 ---")
# 列表可以包含其他列表，形成嵌套结构，常用来表示二维数据，如矩阵或表格
grade_scores = [
    ["语文", 95],
    ["数学", 98],
    ["英语", 92]
]
print(f"成绩单: {grade_scores}")

# 访问嵌套列表的元素需要使用多个索引
# 获取'数学'这门课的成绩
math_score = grade_scores[1][1]
print(f"数学成绩是: {math_score} 分")


# --- 7. 列表遍历的更多实践 ---
print("--- 场景7：列表遍历实践 ---")

# 7.1 使用 while 循环遍历
# 虽然 for 循环更常用，但理解 while 遍历有助于加深对索引的理解。
print("\n--- while 循环遍历 ---")
my_list_1 = ["itcast", "heima", "python"]
index = 0
while index < len(my_list_1):
    element = my_list_1[index]
    print(f"索引 {index}: 列表元素是 {element}")
    index += 1

# 7.2 使用 for 循环遍历 (更简洁，更推荐)
print("\n--- for 循环遍历 ---")
my_list_2 = ["itcast", "heima", "python", 4, 5]
for element in my_list_2:
    print(f"列表元素为: {element}")

# 7.3 遍历练习：筛选列表中的偶数
print("\n--- 遍历筛选练习 ---")
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [] # 创建一个空列表，用于存放结果

for num in original_list:
    if num % 2 == 0: # 判断是否为偶数
        even_numbers.append(num)

print(f"从列表 {original_list} 中筛选出的偶数是: {even_numbers}")

# 7.4 综合练习
print("\n--- 综合练习 ---")
my_list_3 = [21, 25, 21, 23, 22, 20]
print(f"初始列表: {my_list_3}")

my_list_3.append(31)
print(f"追加元素 31 后: {my_list_3}")

my_list_3.extend([29, 33, 30])
print(f"追加新列表后: {my_list_3}")

first_element = my_list_3[0]
last_element = my_list_3[-1]
print(f"取出的第一个元素为 {first_element}，最后一个元素为 {last_element}")

index_of_31 = my_list_3.index(31)
print(f"查找到元素 31 的下标为: {index_of_31}")