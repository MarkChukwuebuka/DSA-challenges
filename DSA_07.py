"""

https://www.hackerrank.com/challenges/greedy-florist/problem


"""

def get_minimum(k:int, c:list) -> int:
    # sort and reverse list
    l = sorted(c, reverse=True)
    # divide list into sublists containing k number of items except the last sublist for cases where length of l is not a multiple of k
    x = [l[i:i + k] for i in range(0, len(l), k)]
    total = 0
    # loop through x(list of sublists) len(x) number of times
    for i in range(1,len(x)+1):
        # 
        total += (i) * sum(x[i-1])