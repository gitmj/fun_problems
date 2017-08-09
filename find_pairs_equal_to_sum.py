"""
write a program to find all pairs of integers whose sum is equal to a given
number. For example if input integer array is {2, 6, 3, 9, 11} and given sum is
9, output should be {6,3}.
"""

def brute_force(arr, sum):
    '''
    Compare each possible pair. O(n^2)
    Args:
        arr: list of numbers.
        sum: sum for which pairs to be found.
    Returns: 
        A list of tuples.
    '''
    pairs = []
    for i in range(len(arr)):
        for j in xrange(i, len(arr)):
            if arr[i] + arr[j] == sum:
                pairs.append((arr[i], arr[j]))
    return pairs

def one_pass_sol(arr, sum):
    '''
    Takes extra O(n) space but time complexity is O(n) because only one pass
    over array.
    '''
    num_set = set()
    pairs = []
    for n in arr:
        target = sum - n
        if target in num_set:
            pairs.append((n, target))
        else:
            num_set.add(n)
    return pairs

def in_place_with_sort(arr, sum):
    '''
    in place solution with sorting. O(nlogn)
    '''
    arr.sort()
    left = 0
    right = len(arr) - 1
    pairs = []
    while (left < right):
        current_sum = arr[left] + arr[right]
        if sum == current_sum:
            pairs.append((arr[left], arr[right]))
            left += 1
            right -= 1
        elif current_sum  < sum:
            left += 1
        elif current_sum > sum:
            right -= 1
    return pairs

def main():
    default_arr = [2, 6, 3, 9, 11]
    arr = raw_input('Enter array or empty to use default array:').strip().split()
    arr = [int(a) for a in arr]
    sum = int(raw_input('Enter sum to be found:').strip())
    if len(arr) == 0:
        arr = default_arr
    print 'Input arr: %s' % arr

    print brute_force(arr, sum)

if __name__ == '__main__':
    main()

