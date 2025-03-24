a, b = 0, 1

for i in range(101):
    print('{}th Fibonacci number is: {}'.format(i, a))
    a = b      
    b = a + b  
    
