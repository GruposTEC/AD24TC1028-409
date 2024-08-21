def menor3(m1,m2,m3):
    """Metodo que encuntra el menor de tres numeros

    Args:
        m1 (int): valor monetario de la moneda 1
        m2 (int): valor monetario de la moneda 2
        m3 (int): valor monetario de la moneda 3

    Returns:
        int: el menor de los 3 valores
    """
    x = 0;
    z = 0;

    if m1> m2:
        x = m1
    else:
        x = m2
    if(m3 > x):
        z = m3
    else:
        z = x

    return z;

def main():
    """_summary_
    """
    print(menor3(1,10,2))
    print(menor3(1,5,2))

main()