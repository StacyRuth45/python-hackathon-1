def generate_fibonacci(n):
    fibonacci_sequence = [0, 1] 
    
    for i in range(2, n):
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)  
    
    return fibonacci_sequence[:n]  
n = int(input("Enter the number of terms for Fibonacci sequence: "))

fibonacci_sequence = generate_fibonacci(n)
print("Fibonacci sequence up to term", n, ":", fibonacci_sequence)


age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")