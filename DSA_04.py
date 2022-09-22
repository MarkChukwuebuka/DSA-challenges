"""
https://www.hackerrank.com/challenges/two-strings/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=dictionaries-hashmaps
"""
def substring(s1, s2):

    s1 = set(list(s1))
    s2 = set(list(s2))
    if s1.intersection(s2):
        return ('YES')
    else:
        return ('NO')
