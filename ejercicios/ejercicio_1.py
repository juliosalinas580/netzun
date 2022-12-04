def Fibonacci(n,count=0):
    count=count+1
    if n < 0:
        print("error")
    elif n == 0:
        count_total=count
        return [0,count_total]
    elif n == 1 or n == 2:
        count_total=count
        return [1,count_total]
    else:
        fib_a=Fibonacci(n-1,count)
        fib_b=Fibonacci(n-2,count)
        numero_fibonacci=fib_a[0]+fib_b[0]
        count_total=fib_a[1]+fib_b[1]
        respuesta=[numero_fibonacci,count_total]
        return respuesta

n=input('n=')
value,n_call=Fibonacci(int(n))
value_str='fib('+str(n) +') = '+ str(value)
n_str='calls = '+str(n_call)
print(value_str)
print(n_str)