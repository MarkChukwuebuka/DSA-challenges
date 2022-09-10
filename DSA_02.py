"""
Link to challenge: https://www.hackerrank.com/challenges/arrays-ds/problem?isFullScreen=false

"""

def reversedlist(a:list) -> list:
    
    newlist = []

    for i in a:
        newlist.insert(0, i)

    return newlist