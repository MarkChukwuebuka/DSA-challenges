"""
https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

"""

# a => list to be shifted
# d => integer representing number of times the list is to be shifted

def shift_list(a:list, d:int) -> list:
    
    for i in range(0,d):
        a.append(a.pop(0))

    return a