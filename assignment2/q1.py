#hill climbing algorithm is used to find the peak instead of a simple linear search

def query(x):
    return -1 * (x - 7)**2 + 49  #Sample unimodal or quadratic function with peak at x = 7

def find_peak(N):
    low = 0
    high = N

    while low < high:
        mid = (low + high) // 2
        if query(mid) < query(mid + 1):
            #ascending slope so we are on left side so climb right
            low = mid + 1
        else:
            #descending the slope so we are on the right side so descend to the left
            high = mid

    return low  #or high, since low == high

N = 15
peak_index = find_peak(N)
print("Peak found at index:", peak_index)
print("Elevation at peak:", query(peak_index))
