# 10_builtin_functions_sorted.py
# 学习 Python 的通用排序函数 - sorted()

# --- 1. sorted() 函数的基本用法 ---
# sorted() 是一个内置函数，可以对任何可迭代对象（iterable）进行排序。
# 特点：
# 1. 通用性：可用于列表、元组、字符串、集合、字典等。
# 2. 返回新列表：它不会修改原始对象，而是返回一个全新的、排好序的【列表】。

print("--- 场景1：对不同类型进行排序 ---")
my_list = [3, 4, 2, 1, 5]
my_tuple = (3, 2, 4, 1, 5)
my_str = "bdcefga"
my_set = {3, 1, 2, 5, 4}
my_dict = {"key3": 1, "key1": 2, "key2": 3, "key5": 4, "key4": 5}

# 对列表排序
print(f"列表排序结果: {sorted(my_list)}")
# 对元组排序
print(f"元组排序结果: {sorted(my_tuple)}")
# 对字符串排序（按字符的ASCII码）
print(f"字符串排序结果: {sorted(my_str)}")
# 对集合排序
print(f"集合排序结果: {sorted(my_set)}")
# 对字典排序（默认只对键'key'进行排序）
print(f"字典排序结果: {sorted(my_dict)}\n")


# --- 2. 反向排序 ---
# sorted() 函数接受一个 `reverse` 参数，当设置为 True 时，进行降序排序。
print("--- 场景2：反向排序 (降序) ---")
print(f"列表反向排序: {sorted(my_list, reverse=True)}")
print(f"元组反向排序: {sorted(my_tuple, reverse=True)}")
print(f"字符串反向排序: {sorted(my_str, reverse=True)}\n")


# --- 3. 排序原理：字符串比较 ---
# sorted() 对字符串排序时，遵循的是字典序（lexicographical order），
# 实际上是比较每个字符的ASCII码值。
print("--- 场景3：排序原理浅析 ---")
# 逐个字符比较: 'a'=='a', 'b'=='b', 'd'>'c', 所以 "abd" > "abc"
print(f"'abd' > 'abc' 的结果是: {'abd' > 'abc'}")
# 长度更长的字符串更大
print(f"'ab' > 'a' 的结果是: {'ab' > 'a'}")
# 小写字母的ASCII码大于大写字母
print(f"'a' > 'A' 的结果是: {'a' > 'A'}")
# 同样适用于其他字符串
print(f"'key2' > 'key1' 的结果是: {'key2' > 'key1'}")