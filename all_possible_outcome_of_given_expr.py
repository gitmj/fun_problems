"""
Given an arithmetic expression, find all possible outcomes of this expression.
Different outcomes are evaluated by putting brackets at different places.

We may assume that the numbers are single digit numbers in given expression.

Input:  1+3*2
Output: 8  7
Explanation
(1 + 3)*2     = 80
(1 + (3 * 2)) = 70

Input:  1*2+3*4
Output: 14 20 14 20 20
 (1*(2+(3*4))) =  14
  (1*((2+3)*4)) =  20 
   ((1*2)+(3*4)) =  14
    ((1*(2+3))*4) =  20
     ((1*2)+3)*4)  =  20
Sol:
1) Initialize result 'res' as empty.
2) Do following for every operator 'x'.
    a) Recursively evaluate all possible values on left of 'x'.
       Let the list of values be 'l'.  
    a) Recursively evaluate all possible values on right of 'x'.
       Let the list of values be 'r'.
    c) Loop through all values in list 'l'  
           loop through all values in list 'r'
               Apply current operator 'x' on current items of 
               'l' and 'r' and add the evaluated value to 'res'   
3) Return 'res'.
 
 """

def eval(a, oper, b):
    a = int(a)
    b = int(b)
    if oper == '+':
        return a + b
    if oper == '-':
        return a - b
    if oper == '*':
        return a * b

def evalAll(expr, low, high):
    val = []
    low = int(low)
    high = int(high)
    if low == high:
        val.append(int(expr[low]))
    if low == (high - 2) : 
        num = eval(expr[low], expr[low + 1], expr[high])
        val.append(num)
     
    for i in xrange(low+1, high, 2):
        l = evalAll(expr, low, i - 1)
        r = evalAll(expr, i + 1, high);
        for l1 in l:
            for r1 in r:
                num = eval(l1, expr[i], r1)
                val.append(num)
    return val

if __name__ == "__main__":
    expr = raw_input("Please enter string:") 
    val = evalAll(expr, 0, len(expr) - 1)
    for v in val:
        print v
