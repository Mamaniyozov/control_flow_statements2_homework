from operator import index


def main(n):
    """
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    x1=n%10
    n=n//10
    x2=n%10
    n=n//10
    x3=n%10
    n=n//10
    x4=n%10
    n=n//10
    x5=n%10
    n=n//10
    m=x1
    if m<x2:
        return x2
    if m<x3:
        return x3
    if m<x4:
        return x4
    if m<x5:
        return x5
print(main(23476))