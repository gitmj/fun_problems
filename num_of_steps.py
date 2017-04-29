"""
A child is running up a staircase with n steps and can hop either 1 step or 2
steps or 3 steps at a time. How many possible ways chile can run up the N
stairs.
"""
def book_sol(n):
    if n < 0:
        return 0
    if n == 0:
        return 1; 
    return book_sol(n - 1) + book_sol(n - 2) + book_sol(n - 3)

# Recursive version
def num_steps(n):
    if n <=  0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    return (num_steps(n - 1) + num_steps(n - 2)
            + num_steps(n - 3))

def num_steps_mem(n, cache):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    if n in cache:
        return cache[n]
    else:
        cache[n] = (num_steps_mem(n - 1, cache) + num_steps_mem(n - 2, cache)
        + num_steps_mem(n - 3, cache))
        return cache[n]

if __name__ == "__main__":
    var = raw_input("Please enter something: ")
    print "book sol: ", book_sol(int(var))
    print num_steps(int(var))   
    cache = dict()
    print num_steps_mem(int(var), cache)
