"""
You are given an array of 0s and 1s in random order. Segregate 0s on left side
and 1s on right side of the array. Traverse array only once.

Input array   =  [0, 1, 0, 1, 0, 0, 1, 1, 1, 0] 
Output array =  [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
"""

def count_0(input_arr):
    zero_cnt = 0
    for x in input_arr:
        if x == 0:
            zero_cnt += 1
    output_arr = []
    for i in range(zero_cnt):
        output_arr.append(0)
    for j in xrange(len(output_arr), len(input_arr)):
        output_arr.append(1)
    return output_arr 

def two_index(input_arr):
    left = 0
    right = len(input_arr) - 1
    while left < right:
        if input_arr[left] == 0:
            left += 1
        if input_arr[right] == 1:
            right -= 1;
        if input_arr[left] == 1 and input_arr[right] == 0:    
            input_arr[left] = 0
            left += 1
            input_arr[right] = 1
            right -= 1
    return input_arr

def main():
    input_arr = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
    output_arr = count_0(input_arr)
    print output_arr
    output_arr = two_index(input_arr)
    print output_arr

if __name__ == '__main__':
    main()

