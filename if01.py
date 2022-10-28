


def main(a,b,c):
    """
    Find the largest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a>b and b>c and c<a:
        return a
    if b>a and c<b and  a<c:
        return b
    if a<c and b<c and a<b:
        return c
print (main(1,4,2))