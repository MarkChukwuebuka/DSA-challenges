"""
Link to challenge: https://www.hackerrank.com/challenges/arrays-ds/problem?isFullScreen=false

"""

def reversedlist(a:list) -> list:
    
    reversedlist = []

    for i in a:
        reversedlist.insert(0, i)

    return reversedlist