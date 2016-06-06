"""
Return the factorial of the provided integer. If the integer is represented
with the letter n, a factorial is the product of all positive integers less
than or equal to n.

Factorials are often represented with the shorthand notation n!

For example: 5! = 1 * 2 * 3 * 4 * 5 = 120
"""

def factorial(num):
    """Calculates the factorial for a given number"""
    total = 1

    for i in range(2, (num + 1)):
        total *= i

    return total
