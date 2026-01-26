class A:
    def __init__(self):
        print("A's __init__")  # 1


class B(A):
    def __init__(self):
        A.__init__(self)  # Explicitly calling A's __init__
        print("B's __init__")  # 2


class C(A):
    def __init__(self):
        A.__init__(self)  # Explicitly calling A's __init__
        print("C's __init__")


class D(B, C):
    def __init__(self):
        B.__init__(self)  # Explicitly calling B's __init__
        C.__init__(self)
        # What if B's __init__ also calls A's __init__? This might lead to issues
        print("D's __init__")


# Create an instance of D

D()
