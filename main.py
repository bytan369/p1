def add_two_numbers():
  while True:
      try:
          # 获取用户输入的两个数字
          num1 = float(input("请输入第一个数字: "))
          num2 = float(input("请输入第二个数字: "))

          # 计算两个数字的和
          result = num1 + num2

          # 打印结果
          print(f"{num1} + {num2} 的和是 {result}")

      except ValueError:
          # 处理非数字输入的情况
          print("请输入有效的数字！")
          continue

      # 询问用户是否想要继续
      another = input("您想要继续计算吗？(y/n): ")
      if another.lower() != 'y':
          break

# 调用函数
add_two_numbers()
