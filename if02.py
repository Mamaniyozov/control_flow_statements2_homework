def main(a,b,c):
    """
    Find the smallest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a<c and a<b and c<b:
        return a
    if a>c and b>c and a>b:
        return c
    if a>b and c>b and a>c:
        return b
print (main(1,4,2))