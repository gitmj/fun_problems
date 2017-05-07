"""
Write a function to generate all possible n pairs of balanced parentheses.

For example, if n=1
{}
for n=2
{}{}
{{}}

Input: 1 Ouput: ()
Input: 2 Outut: ()(), (())
Input: 3 Output: ((())), (()()), ()()(), ()(()), (())()
and so on

Sol:
1) Keep track of open and close brackets.
2) Start from zero.
3) If open_bracket is less than N then recursively call by incrementing
open_bracket count and adding open bracket to string.
4) Once open_bracket reaches the value of N then go for closing bracket.
5) if open_bracket is greater than close_bracket counter then add close 
bracket to string, bump up the counter for close bracket and call recursively.
6) Once, the close bracket counter reaches N then print the damn string.

Purpose of recursive calls:
    Highlevel: Recursive call allows for all possiblities for string.
    For each increment of open bracket counter with recursive calls, 
    close bracket counter also get incremented when original call returns.
    This way all possible combination of open and close gets cycled through.

    Detail: For N = 2, first count is open counter and second is close counter.
        First deep dive:
            ( 1 0
            (( 2 0
            (() 2 1
            (()) 2 2
        Once call start to return, it will fork off and replace last open
        bracket with close bracket. Like this:
            ( 1 0
            (( 2 0
            (() 2 1
            (()) 2 2
            (()) <<<<< Second deep dive after this.
            () 1 1
            ()( 2 1
            ()() 2 2
 """


def evalAll(n, s, open_brackets, close_brackets):
    print s, open_brackets, close_brackets
    if close_brackets == n:
        print s
    else:
        if open_brackets < n:
            evalAll(n, s+'(', open_brackets + 1, close_brackets)
        if open_brackets > close_brackets:
            evalAll(n, s+')', open_brackets, close_brackets + 1)
if __name__ == "__main__":
    n = int(raw_input("Please enter string:"))
    s = ""
    evalAll(n, s, 0, 0)
