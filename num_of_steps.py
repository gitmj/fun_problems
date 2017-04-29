def num_steps(n):
    if n < 0:
        return 0
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 3
    return num_steps(n - 1) + num_steps(n - 2)
    + num_steps(n - 3)

if __name__ == "__main__":
    var = raw_input("Please enter something: ")
    print "you entered", var
    print num_steps(int(var))   
    
