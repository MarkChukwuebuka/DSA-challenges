"""

https://www.hackerrank.com/challenges/mark-and-toys/problem

"""

def max_toys(prices:list, k:int) -> int:
    
    #sort the prices list
    prices.sort()

    total_price = 0
    toy_count = 0

    # iterate through the list
    for price in prices:
        # add each price to total sum
        total_price += price
        # if total_price isn't more than budget, update toy_count then add the next price 
        if total_price > k:
            return toy_count
            break
        else:
            toy_count += 1