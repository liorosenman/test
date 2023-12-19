from comp import *
from simp import *
import sys
sys.path.append('../')
from col import *
was_simp_called = False

def main():
    print(add(10,50)) #60
    was_simp_called = True
    print(subtract(40,10)) #30
    if(was_simp_called):
        print(sumOfDigits(1234)) #10
    else: 
        raise Exception("A simp function was not called")   
    if(was_simp_called):
        print(isPal(42524)) #Is polyndrome
    else:
        raise Exception("A simp function was not called")
    if(was_simp_called):
        print(isPal(3456)) #Not polyndrome
    else:
        raise Exception("A simp function was not called")
    #len(l1) = len(l2)
    l1 = [4,5,6,7]
    l2 = ['a', 'b', 'c', 'd']
    #len(l1) > len(l2)
    l1 = [4,5,6,7,8,9]
    l2 = ['a', 'b', 'c', 'd']
    #len(l1) < len(l2)
    l1 = [4,5,6,7]
    l2 = ['a', 'b', 'c', 'd', 'e','f']
    t = myzip(l1,l2)
    print(t) #Result for all: ((4, 'a'), (5, 'b'), (6, 'c'), (7, 'd'))

if __name__ == "__main__":
    main()

