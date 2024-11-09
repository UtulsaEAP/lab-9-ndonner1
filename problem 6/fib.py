# Noah Donnermeyer
# Th 8am
def fibonacci(n):
    if n < 0:
        return -1
    num1 = 0
    num2 = 1
    for i in range(n):
        num1, num2 = num2, num1+num2
        
      
    return num1

if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')