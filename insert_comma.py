
# Given a string made of opening and closing braces, insert a comma when 
# opening and closing brace matches.
# Example: input : () , output: ()
# input: ()(), output: (),()
# input: (()), output: (())
# input: ((()())(()())) output: (((),()),((),()))

def output(input_str):
    s = []
    prev_c = ''
    for c in input_str:
        if c == '(' and prev_c == ')':    
            s.append(',')
        s.append(c)
        prev_c = c    
    s = ''.join(s)
    print s
    return

if __name__ == "__main__":
    input_str = raw_input("Please enter string:")
    output(input_str)
