# for i in range (1, 100 ,2) :
#     print(i)
# l1 = [1,2,3,4,5,6,7,8,9,10]
# print(max(l1))
# s1= "abcdefghikjlmnopqrstuvwxyz"
# max(s1)
# print(max(s1))
# l1 = [1,2,3,4,5,6,7,8,9,10]
# print(max(l1))
# s1= "abcdefghikjlmnopqrstuvwxyz"
# max(s1)
# print(max(s1))
# print(min(s1))
# def num_add(num1, num2) :
#     num1 = ("Enter the first number : ")
#     num2 = ("Enter the second number : ")
#     return = num1 + num2
#     print(num1 + num2)
# num1 = input("Enter the first number : ")
# num2 = input("Enter the second number : ")
# num_add(num1, num2)
def num_add() :
    num1 = float(input("Enter the first number : "))
    num2 = float(input("Enter the second number : "))
    return num1 + num2
    print(num1 + num2)
if __name__ == "__main__" :
    result = num_add()
    print(result)