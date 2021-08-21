def solution(i):
    if(i < 0 or i > 10000):
        return;
    primeString = generatePrimeString(10005);
    return primeString[i:i+5]

def isPrime(n):
    if(n == 2):
        return True
    elif(n < 2 or not n & 1):
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def generatePrimeString(n):
    primeString = '2'
    iterator = 1
    while len(primeString) < n:
        if(isPrime(iterator)):
            primeString += str(iterator)
        iterator += 2
    return primeString