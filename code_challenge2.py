dell = eval(input("Enter amount to deposit: "))

n1 = dell // 1000
dell = dell % 1000

n2 = dell // 500
dell = dell % 500

n3 = dell // 200
dell = dell % 200

n4 = dell // 100
dell = dell % 100

n5 = dell // 50
dell = dell % 50

n6 = dell // 20
dell = dell % 20

n7 = dell // 10 
dell = dell % 10

n8 = dell // 5 
dell = dell % 5

n9 = dell // 1
dell = dell % 1

print("Here is Breakdown")
print("Ph", n1)
print("Ph", n2)
print("Ph", n3)
print("Ph", n4)
print("Ph", n5)
print("Ph", n6)
print("Ph", n7)
print("Ph", n8)
print("Ph", n9)