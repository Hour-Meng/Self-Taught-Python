class A:
    def __init__(self):
        print("A's __init__")

class B(A):
    def __init__(self):
        super().__init__()  # Calls A's __init__ following the MRO
        print("B's __init__")

class C(A):
    def __init__(self):
        super().__init__()  # Calls A's __init__ following the MRO
        print("C's __init__")

class D(B, C):
    def __init__(self):
        super().__init__()  # Calls B's __init__ which then calls C's __init__ and A's __init__ following the MRO
        print("D's __init__")

# Create an instance of D
D()
