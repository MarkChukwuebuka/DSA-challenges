"""
Link to challenge - https://www.hackerrank.com/challenges/2d-array/problem?filter=python3&filter_on=language&h_l=interview&isFullScreen=true&page=1&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

"""

#collects user input
arr = input()
# changes the user input into a list
arr = list(map(int, arr.split(" ")))
# divides the list into equal smaller lists
arr = [arr[i:i + 6] for i in range(0, len(arr), 6)]

# empty list to hold sums of each array   
sums = []


for x in range(0,4):
    for y in range(0,4):
        total = 0
        total += arr[x][y] + arr[x][y+1] + arr[x][y+2]
        total += arr[x+1][y+1]
        total += arr[x+2][y] + arr[x+2][y+1] + arr[x+2][y+2]
        sums.append(total)

print(max(sums))