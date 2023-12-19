
def add(a ,b):
    global was_simp_called
    was_simp_called = True
    return a + b

def subtract(a,b):
    global was_simp_called
    was_simp_called = True
    return a - b
