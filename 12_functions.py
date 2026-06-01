# 12_functions.py
# 学习定义和使用函数，封装代码逻辑

# --- 1. 定义和调用最简单的函数 ---
# 场景：封装一段重复执行的业务逻辑，例如进入门口检查体温。
print("--- 场景1：定义和调用函数 ---")

def temperature_check(temperature):
    """
    检查体温，并根据体温是否超过37.5度打印不同提示。
    这是一个函数文档字符串 (Docstring)，用来解释函数的功能。
    :param temperature: 传入的体温，浮点型或整型。
    """
    print("您好！请出示健康码和核酸证明。")
    if temperature <= 37.5:
        print(f"您的体温是 {temperature} 度，体温正常，请进！")
    else:
        print(f"您的体温是 {temperature} 度，体温异常，需要隔离观察！")

# 调用函数，并传入不同的参数
temperature_check(36.9)
print("-" * 20) # 分隔线
temperature_check(38.0)
print("\n")


# --- 2. 函数的返回值 `return` ---
# 场景：函数执行完一个计算后，需要将结果返回给调用者，而不是直接打印。
print("--- 场景2：使用 `return` 返回值 ---")

def add(x, y):
    """计算两个数的和并返回结果。"""
    result = x + y
    return result

# 调用函数，并用一个变量 `sum_result` 来接收返回值
sum_result = add(5, 6)
print(f"调用 add(5, 6) 函数，得到的结果是: {sum_result}\n")


# --- 3. 函数返回 None 类型 ---
# 场景：函数在某些条件下可能没有有效值可以返回。
# 在 Python 中，如果一个函数没有显式的 return 语句，或者 return 后面没有值，它会默认返回 None。
print("--- 场景3：函数返回 None ---")

def check_age(age):
    """检查年龄，如果大于18岁返回'Success'，否则返回None。"""
    if age > 18:
        return "Success"
    # 如果 age <= 18，函数会走到最后，没有 return 语句，所以隐式返回 None

# 调用函数并检查返回值
result = check_age(16)
print(f"检查16岁的结果是: {result}")
if not result:  # None 在布尔判断中等同于 False，所以 `not None` 就是 True
    print("判断结果：未成年，需要监护人陪同。\n")


# --- 4. 函数的嵌套调用 ---
# 场景：一个复杂的任务可以分解成多个小任务，由不同的函数完成，然后串联起来。
print("--- 场景4：函数的嵌套调用 ---")

def process_data():
    print("步骤2：开始处理数据...")

def main_task():
    print("步骤1：开始主任务。")
    process_data()  # 在 main_task 内部调用 process_data
    print("步骤3：主任务完成。")

main_task()
print("\n")


# --- 5. 变量的作用域 (Scope) ---
# 场景：理解函数内部和外部变量的关系。
print("--- 场景5：变量作用域 ---")
# 这是一个全局变量 (Global Variable)，在文件的任何地方都可以访问
global_num = 200 

def read_global_var():
    # 函数内部可以直接读取全局变量的值
    print(f"在函数 read_global_var 内部读取到 global_num: {global_num}")

def modify_global_var():
    # 如果想在函数内部修改全局变量的值，必须使用 `global` 关键字声明
    global global_num
    global_num = 500
    print(f"在函数 modify_global_var 内部将 global_num 修改为: {global_num}")

print(f"调用函数前，全局变量 global_num 的值是: {global_num}")
read_global_var()
print(f"调用 read_global_var 后，全局变量的值是: {global_num}")
modify_global_var()
print(f"调用 modify_global_var 后，全局变量的值是: {global_num}")


# --- 6. 函数的特殊参数与高级用法 ---

print("\n--- 场景5.1：函数多返回值 ---")
# Python 函数可以返回多个值，实际上是以元组的形式返回。
def test_multi_return():
    return 1, "hello", True

# 接收多返回值可以直接用多个变量进行解包
x, y, z = test_multi_return()
print(f"x 的值是: {x}, 类型是: {type(x)}")
print(f"y 的值是: {y}, 类型是: {type(y)}")
print(f"z 的值是: {z}, 类型是: {type(z)}")


print("\n--- 场景5.2：不定长参数 (*args) ---")
# *args (arguments) 用于收集所有未被匹配的【位置参数】，
# 它会将这些参数打包成一个【元组】。
def user_info_args(*args):
    print(f"接收到的参数是: {args}, 类型是: {type(args)}")

user_info_args("Tom")
user_info_args("Tom", 18)
user_info_args("Alice", 25, "Beijing", "Engineer")


print("\n--- 场景5.3：不定长关键字参数 (**kwargs) ---")
# **kwargs (keyword arguments) 用于收集所有未被匹配的【关键字参数】，
# 它会将这些参数打包成一个【字典】。
def user_info_kwargs(**kwargs):
    print(f"接收到的参数是: {kwargs}, 类型是: {type(kwargs)}")

user_info_kwargs(name="Tom", age=12, city="New York")
user_info_kwargs(product="Laptop", price=999, brand="HP", weight=2.5)


print("\n--- 场景5.4：函数作为参数传递 ---")
# 函数在 Python 中是“一等公民”，可以像其他数据类型一样被传递、赋值。
def calculate_and_print(operation_func, num1, num2):
    """
    接收一个函数作为参数，并用其对两个数字进行计算和打印结果。
    """
    print(f"接收到的操作函数类型是: {type(operation_func)}")
    result = operation_func(num1, num2)
    print(f"使用 {operation_func.__name__} 函数计算 {num1} 和 {num2} 的结果是: {result}")

# 定义一个加法函数
def add_numbers(a, b):
    return a + b

# 定义一个乘法函数
def multiply_numbers(a, b):
    return a * b

calculate_and_print(add_numbers, 10, 5)
calculate_and_print(multiply_numbers, 10, 5)


print("\n--- 场景5.5：匿名函数 (lambda 表达式) ---")
# lambda 表达式用于创建小型、一次性的匿名函数。
# 语法：lambda arguments: expression
# 只能包含一个表达式，表达式的结果就是函数的返回值。

# 结合函数作为参数的例子使用 lambda
calculate_and_print(lambda x, y: x - y, 20, 7) # 匿名实现减法
calculate_and_print(lambda a, b: a / b, 100, 4) # 匿名实现除法

# lambda 也可以直接赋值给变量 (但不推荐用于复杂逻辑)
get_max = lambda x, y: x if x > y else y
print(f"使用 lambda 获取最大值: max(10, 20) = {get_max(10, 20)}")
