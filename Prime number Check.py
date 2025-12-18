n = int(input("Enter your number: "))
if n <= 1:
    print(False)
else:
    is_prime = "Prime"
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = "Not Prime"
            
    print(is_prime)