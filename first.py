
#this is a comment:
a, b, c = 5, 10, None

A, B, C = 20, 30, 40


print("Hello, World!")

print(f"hello a: {a} b: {b}")

if(a < b):
    print("A is less than B")
elif(a > b):
    print("A is greater than B")
else:
    print("A is is equal to B")

count = 0
while count < 10:
    print(count)
    count+=1

myArray = [1, 3, 5, 7, 9]

for element in myArray:
    print(element)

weekDays = ["Sunday", "Monday", "Tuesday"]

for day in weekDays:
    print(day)

print()
print(weekDays[0])



def sayHello():
    print()
    print("hello world!")
sayHello()


       
