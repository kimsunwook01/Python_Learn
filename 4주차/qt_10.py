num = int(input("정수 = "))
numAdd = num//1000 + (num%1000//100) + (num%1000%100/10) + (num%1000%100%10)
print(int(numAdd))