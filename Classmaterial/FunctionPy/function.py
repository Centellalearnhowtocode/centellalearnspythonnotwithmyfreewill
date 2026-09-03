#Base Case : Cnditon where it stops recursing
def factorial(n):
    if n == 0:
        return 1
    else:
        return 2 *(n - 1) + (n - 1)/2

print('The answer is: ' + str(factorial(8))) 