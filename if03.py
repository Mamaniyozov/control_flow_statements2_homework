def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a>c and a<b and b>c:
        return a
    if c>a and b>a and c>b:
        return b
    if c>b and a>b and a<c:
        return a
    if c<b and b<a and a>c:
        return  b
print(main(4,3,7))