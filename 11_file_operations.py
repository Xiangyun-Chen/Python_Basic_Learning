# 11_file_operations.py
# 学习 Python 中的文件操作：读写与管理

# 文件操作是程序与外部数据交互的重要方式。
# 基本步骤：打开文件 -> 读取/写入 -> 关闭文件。

# --- 1. 文件打开与关闭 ---
# open(file, mode='r', encoding=None)
# - file: 文件路径（相对路径或绝对路径）
# - mode: 文件打开模式，常见有：
#   'r' (read): 读取模式（默认），文件不存在则报错。
#   'w' (write): 写入模式，如果文件存在会清空内容，文件不存在则创建。
#   'a' (append): 追加模式，如果文件存在在末尾添加，文件不存在则创建。
# - 文件写入：文件对象.write()内容并未真正写入文件，会积攒在缓冲区
# - 内容刷新：文件对象.flush()内容真正写入文件，close()内置了flush功能
# - encoding: 文件编码，常用 'UTF-8'。


print("--- 场景1：文件的打开与关闭 ---")
# 1. 以只读模式打开文件
file_path = "test.txt" # 假设文件在当前脚本的同级目录
try:
    f = open(file_path, "r", encoding="UTF-8")
    print(f"成功打开文件 '{file_path}', 文件对象类型是: {type(f)}")
except FileNotFoundError:
    print(f"错误：文件 '{file_path}' 不存在，请创建。")
except Exception as e:
    print(f"打开文件时发生其他错误: {e}")
finally:
    # 无论是否出错，都尝试关闭文件（如果文件被成功打开）
    if 'f' in locals() and not f.closed:
        f.close()
        print(f"文件 '{file_path}' 已关闭。")
print("-" * 30 + "\n")


# --- 2. 文件内容的读取 ---
print("--- 场景2：文件内容的读取方法 ---")
# 推荐使用 with open 语句，它会自动管理文件的打开和关闭，即使发生错误。
with open("test.txt", "r", encoding="UTF-8") as f:
    # .read(num): 读取指定数量的字符/字节，不传参数则读取所有内容。
    print(f"读取前10个字符: '{f.read(10)}'")
    # 再次调用 .read() 会从上次读取结束的位置继续。
    print(f"继续读取所有剩余内容: '{f.read()}'")
    # 注意：此时文件指针已在文件末尾，再次读取会是空字符串。

# 重新打开文件以演示其他读取方法
with open("test.txt", "r", encoding="UTF-8") as f:
    # .readline(): 读取文件的一行内容（包括换行符 \n）。
    print(f"\n第一行数据: '{f.readline().strip()}'") # .strip() 去除末尾的换行符
    print(f"第二行数据: '{f.readline().strip()}'")

# 重新打开文件以演示其他读取方法
with open("test.txt", "r", encoding="UTF-8") as f:
    # .readlines(): 读取所有行，并以列表形式返回，每行作为一个字符串元素。
    lines_list = f.readlines()
    print(f"\n所有行作为列表返回: {lines_list}")
    print(f"列表中第一个元素（第一行）是: '{lines_list[0].strip()}'")

# 重新打开文件以演示其他读取方法
with open("test.txt", "r", encoding="UTF-8") as f:
    # 迭代文件对象：最常用和推荐的读取大文件的方式，逐行读取，内存效率高。
    print("\n--- 逐行迭代文件对象 ---")
    for i, line in enumerate(f):
        print(f"第 {i+1} 行数据: '{line.strip()}'")
print("-" * 30 + "\n")


# --- 3. 练习：统计文件中指定单词出现的次数 ---
print("--- 场景3：文件读取练习 - 单词统计 ---")
# 需求：统计 'word.txt' 文件中 "itheima" 单词出现的次数。

# 方法一：一次性读取所有内容，然后使用字符串的 count 方法。
try:
    with open("word.txt", "r", encoding="UTF-8") as f_word_read_all:
        content = f_word_read_all.read()
        count_all = content.count("itheima")
        print(f"方法一：'itheima' 出现的次数是: {count_all} 次")
except FileNotFoundError:
    print("错误：'word.txt' 文件不存在，请创建。")
except Exception as e:
    print(f"读取文件时发生错误: {e}")


# 方法二：逐行读取，然后处理每一行。
try:
    count_per_line = 0
    with open("word.txt", "r", encoding="UTF-8") as f_word_per_line:
        for line in f_word_per_line:
            # 清理行内容，去除首尾空白符（包括换行符）
            line = line.strip()
            # 将行按空格分割成单词列表
            words = line.split(" ")
            # 遍历单词列表，进行统计
            for word in words:
                if word == "itheima":
                    count_per_line += 1
    print(f"方法二：'itheima' 出现的次数是: {count_per_line} 次")
except FileNotFoundError:
    print("错误：'word.txt' 文件不存在，请创建。")
except Exception as e:
    print(f"读取文件时发生错误: {e}")



# --- 4. 文件的写入与追加 ---

# 'w' (write) 模式：写入模式
# - 如果文件存在，会【清空】原有内容，然后写入新内容。
# - 如果文件不存在，会【创建】一个新文件。
print("--- 场景4：文件写入模式 ('w') ---")
try:
    with open("hello.txt", "w", encoding="UTF-8") as f_write:
        f_write.write("Hello, World!")
        # .flush() 方法可以强制将缓冲区的内容写入磁盘，
        # 但 with 语句在结束时会自动调用，通常无需手动操作。
    print("成功向 'hello.txt' 写入内容。")
except Exception as e:
    print(f"写入文件时发生错误: {e}")


# 'a' (append) 模式：追加模式
# - 如果文件存在，会在文件【末尾】添加新内容，不影响原有内容。
# - 如果文件不存在，会【创建】一个新文件。
print("\n--- 场景5：文件追加模式 ('a') ---")
try:
    with open("hello.txt", "a", encoding="UTF-8") as f_append:
        f_append.write("\nPython is awesome.") # 使用 \n 手动换行
    print("成功向 'hello.txt' 追加内容。")
except Exception as e:
    print(f"追加内容时发生错误: {e}")
print("-" * 30 + "\n")


# --- 6. 综合练习：文件备份与数据清洗 ---
print("--- 场景6：综合练习 - 文件备份与数据清洗 ---")
# 需求：读取一个账单文件 `bill.txt`，过滤掉其中类别为“测试”的记录，
#       然后将有效记录写入到一个备份文件 `bill.txt.bak` 中。

# 准备一个测试文件：
# 一个名为 `bill.txt` 的文件，内容如下：
# -------------------- bill.txt --------------------
# 2023-01-01,餐饮,午餐,25,支付宝
# 2023-01-01,交通,地铁,4,支付宝
# 2023-01-02,娱乐,电影,80,微信支付
# 2023-01-02,杂项,无,0,测试
# 2023-01-03,购物,衣服,300,信用卡
# 2023-01-04,杂项,坏账,0,测试
# --------------------------------------------------

try:
    # 同时打开读和写两个文件对象
    with open("bill.txt", "r", encoding="UTF-8") as fr, \
         open("bill.txt.bak", "w", encoding="UTF-8") as fw:
        
        # 逐行读取原始文件
        for line in fr:
            # 清理行末的换行符
            line = line.strip()
            
            # 分割字符串并检查第五个元素（索引为4）是否为“测试”
            if line.split(",")[4] == "测试":
                # 如果是，则跳过当前循环，不写入
                continue
            
            # 如果不是，则将该行内容写入备份文件
            fw.write(line)
            # 手动写入一个换行符，因为 .strip() 已经移除了它
            fw.write("\n")
            
    print("文件 'bill.txt' 已成功处理，结果已存入 'bill.txt.bak'。")
    print("请检查项目目录下的新文件。")

except FileNotFoundError:
    print("错误：请先创建 'bill.txt' 文件并填入示例内容。")
except Exception as e:
    print(f"处理文件时发生错误: {e}")