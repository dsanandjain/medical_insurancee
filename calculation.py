
def get_Addition(a,b):
    """
    This is Addition Function
    """
    add = a + b
    # print(f"Addition of {a} and {b} is {add}")
    return add

def get_Multiplication(a,b):
    """
    This is Multiplication Function
    """
    mult = a * b
    return mult


if __name__ == "__main__":
    get_Addition(3,4)
    print(get_Addition.__doc__)