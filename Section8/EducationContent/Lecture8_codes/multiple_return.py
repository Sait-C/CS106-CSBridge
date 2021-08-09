def sum_square_cube (a,b):
    
    result1=a**2+b**2
    result2=a**3+b**3
    
    return result1,result2



def main():
    num1= float(input("Enter a number1: "))
    num2= float(input("Enter a number2: "))
    
    r1,r2=sum_square_cube (num1,num2)
    
    print()
    
    print("Sum squares: ", r1)
    print("Sum cubes: ", r2)
    
    
main()