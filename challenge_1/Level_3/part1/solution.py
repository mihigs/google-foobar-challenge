def solution(n):
    if(type(n) != str):
        return false;

    return organiseFuel(int(n))

def organiseFuel(input, counter = 0):
    print(input)
    if(input <= 1):
        return counter;

    if(input % 2 == 0):
        return organiseFuel(input / 2, counter + 1);
    else:
        if((input - 1) % 2 == 0):
            return organiseFuel((input - 1) / 2, counter + 1);
        else:
            return organiseFuel((input + 1) / 2, counter + 1);


print(solution('999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999931122332212313213231231231231231231231231231231293192391293192391293912391923912931923912931293192391293192319239123912939999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999'))