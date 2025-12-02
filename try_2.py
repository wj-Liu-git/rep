# 1. 问候用户（输入输出示例）
# 获取用户输入的姓名
name = input("请输入你的名字：")
# 打印问候语（字符串拼接）
print(f"你好，{name}！欢迎学习 Python～")

# 2. 计算两个数的和（变量 + 基本运算）
# 获取用户输入的两个数字（转换为浮点数，支持小数）
num1 = float(input("\n请输入第一个数字："))
num2 = float(input("请输入第二个数字："))

# 计算和
sum_result = num1 + num2

# 输出结果（格式化打印）
print(f"\n{num1} + {num2} 的结果是：{sum_result}")
