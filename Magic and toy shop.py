
solve a question using python3

Geek goes to a toy shop having N toys, the prices of these toys are given as price array. He wants to buy all the N toys, but he has only M rupees to spend. He has a magical Trident which reduces the price of each toy. This reduced price for each toy is given in magical_price array. That is for ith toy (0<i<N-1) price[i] is the original price and magical_price[i] is the price after applying magic. Since applying magic reduces the power of Trident, he wants to apply it as minimum times as possible.

Find the minimum number of toys on which he should apply this magic so as to buy all the N toys for atmost M rupees. If it is not possible for Geek to buy the toys even after applying the magic on all the toys the return -1.

Example 1:

Input:
N = 5, M = 13 
price = {3,4,6,2,4}
magical_price = {1,2,5,1,3}
Output:
4
Explanation:
Geek can apply the magic on first four toys so as to buy all the toys for 13. He will require minimum 4 magical operations.
Example 2:

Input:
N = 3, M = 6 
price = {4,3,4}
magical_price = {2,2,3}
Output:
-1
Explanation:
Even after applying the maigc on all the toys, he cannot buy all the toys at rupees 6.
Your task:
You don't need to read input or print anything. Your task is to complete the function minimumMagic() which takes four arguments N, M, price, and magical_price. It returns an integer that is minimum magical operations required or -1, if not possible.

Constraints:
1 <= N <= 105
1 <= M <= 109
1 <= magical_price[i] <= price[i] <= 104





SOlution:
def minimumMagic(N, M, price, magical_price):
    # Create a list of tuples (original_price, magical_price)
    toys = list(zip(price, magical_price))
    
    # Sort the toys based on their original prices
    toys.sort()
    
    # Initialize the count of magical operations and remaining budget
    magic_count = 0
    remaining_budget = M
    
    # Iterate over the toys
    for i in range(N):
        original_price, magical_price = toys[i]
        
        # Apply magic on the current toy
        updated_price = min(original_price - magical_price, remaining_budget)
        
        # If the updated price is within the budget, decrement the remaining budget
        if updated_price >= 0:
            remaining_budget -= updated_price
            magic_count += 1
        else:
            # If the updated price exceeds the budget, stop the iteration
            break
    
    # Check if all toys were purchased within the budget
    if remaining_budget >= 0:
        return magic_count
    else:
        return -1

# Time Complexity: O(N*log(N))
# Space Complexity: O(N)

# Driver code
if __name__ == '__main__':
    N = 5
    M = 13
    price = [3, 4, 6, 2, 4]
    magical_price = [1, 2, 5, 1, 3]
    print(minimumMagic(N, M, price, magical_price))

# Output:
# 4
