
def is_even(x):
    
    if x % 2 == 0:
      return True
    else:
      return False
  
    
def main():
   for i in range(100):
      if is_even(i):
         print(i)
         
main()
