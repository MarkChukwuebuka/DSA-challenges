"""

https://www.hackerrank.com/challenges/new-year-chaos/problem?filter=python3&filter_on=language&h_l=interview&h_r=next-challenge&h_v=zen&isFullScreen=true&page=1&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

"""

def FindPos(data, val):
    for i in range(len(data)):
        if val == data[i]:
            return i
    return -1        

def Process(q):
    data = list(range(1, len(q)+ 1))
    # your code goes here
    move = 0
    for i in range(len(q)):
        pos = FindPos(data, q[i])
        data.pop(pos)
        if pos > 2:
            return("Too chaotic")
        move += pos
    return move
