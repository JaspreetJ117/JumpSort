"""

Jump Sort  
@sayanwala117 / Jaspreet Jawanda  
Date Modified: 2025 - 04 - 29  

Back story:  
Created this sorting algorithm after reflecting on the pain Juggle Sort caused me (and possibly others).  
This time, I actually decided to be efficient. No recursion. No remove(). Just pure, direct placement.  
Jump Sort was born while realizing you can just bucket values into their rightful place instead of doing all that  
fancy comparing. It’s like sorting, but with commitment issues — values jump straight to their spots and refuse  
to interact.

what does it do?  
Splits the list into negatives and non-negatives.  
Then for each number, it jumps into the correct index (like, literally).  
Negatives are placed in reverse using abs(), and positives go to their number-indexed position.  
After the values settle in their respective buckets, we flatten and concatenate both sides.  
Done. Sorted. With no comparisons. Honestly, it's kind of smart.  
Calling it Jump Sort because the values just leap into place.  
No drama. Just vibes.  
And if you're wondering "what’s going through this guy’s head now?" — the winter semester depression is over.  
We’re sorting smarter now.
 
"""

import random

random.seed(42)  # Ensures same list every time
unsorted = [random.randint(-250, 250) for _ in range(500)]


# Separate into negatives and non-negatives
unsorted_negatives = [x for x in unsorted if x < 0]
unsorted = [x for x in unsorted if x >= 0]

# Handle negatives 
if unsorted_negatives:
    max_neg = abs(min(unsorted_negatives))
    neg_list = [[] for _ in range(max_neg)]  # Use buckets

    for num in unsorted_negatives:
        index = abs(num) - 1
        neg_list[index].append(num)

    # Flatten and reverse (since more negative numbers go earlier)
    neg_list = [num for sublist in reversed(neg_list) for num in sublist]
else:
    neg_list = []

# Handle non-negatives 
if unsorted:
    max_nonneg = max(unsorted)
    pos_list = [[] for _ in range(max_nonneg + 1)]  # Include index for zero

    for num in unsorted:
        index = num
        pos_list[index].append(num)

    # Flatten
    pos_list = [num for sublist in pos_list for num in sublist]
else:
    pos_list = []

# Combine
unsorted = neg_list + pos_list
print(neg_list + pos_list)
