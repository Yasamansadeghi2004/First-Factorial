
def FirstFactorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i



  
    return fact

# keep this function call here 
x = int(input("_"))
print(FirstFactorial(x))
