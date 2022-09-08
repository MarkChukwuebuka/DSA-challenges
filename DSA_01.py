"""
Link to DSA challenge - https://www.hackerrank.com/challenges/2d-array/problem?filter=python3&filter_on=language&h_l=interview&isFullScreen=true&page=1&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

"""


row0 = list(map(int, input().split(" ")))
row1 = list(map(int, input().split(" ")))
row2 = list(map(int, input().split(" ")))
row3 = list(map(int, input().split(" ")))
row4 = list(map(int, input().split(" ")))
row5 = list(map(int, input().split(" ")))

arr = [row0, row1, row2, row3, row4, row5]

def hour_glass(arr):

    max_arr = []


    for x in range(0,4):
        for y in range(0,4):
            total = 0
            total += arr[x][y] + arr[x][y+1] + arr[x][y+2]
            total += arr[x+1][y+1]
            total += arr[x+2][y] + arr[x+2][y+1] + arr[x+2][y+2]
            max_arr.append(total)

    return max(max_arr)