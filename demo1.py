name = "Nguyen Van An"
print(name)
age = 18
print(age)
max = 100
print(max-age)
x=10
y=3
print(x/y)
print(x//y)
print(x%y)

if age >= 18:
    print("Du 18 tuoi")
else:
    print("Chua du 18")
#  i=0;i<10;i++
for i in range(10): 
    print(i)
i=0
while i<5:
    print(i)
    i+=1

def hello():
    print("Hello world!")

hello()

def total(a,b):
    return a+b
c = total(5,10)
print(c)

numbers = [1,2,3,4]
print(numbers[3]) # 4
numbers.append(9)
print(numbers[4])

for n in numbers:
    print(n)

arr = range(1000)
for n in arr:
    print(n)

# viet ham cheeck SNT
def isPrime(p):
    if p < 2:
        return False
    else:
        if p < 4:
            return True
        else:
            for i in range(2,p//2):
                if p % i == 0:
                    return False
            return True

def demo(x="Goodmorning"): #default param
    print(x)

demo("Hello")    
demo()    

def sub(a,b=1):
    print(a/b)

sub(5)
sub(5,b=5)
sub(b=6,a=12)

user = { #dictionary
    "name":"Nguyen Van An",
    "age": 20
}
print(user["name"])

users= [
    {"name":"A","age":17},
    {"name":"B","age":20},
    {"name":"C","age":15}
]

def TBT(data):
    total = 0
    for i in data:
        total += i["age"]
    return total/len(data)

print("TBT:",TBT(users))