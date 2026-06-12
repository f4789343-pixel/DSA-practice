sliding window

problems solved

1. Maximum Average subarray(fixed window):
   - window size remain constant.
   - sum the elements in window length.
   - remove the element leaving the window.
   - divide window sum by window size.
   - track maximum average subarray.

what I learned:
   - how fixed-size windows avoid recalculating sums.
   - how to remove leaving character.

2. Longest Substring without reapting characters(variable window):
    - Expand the window using right pointer.
    - if a reapted character appears, shrink the window from left.
    - Track the maximum length.

what I learned:
   - difference between fixed and variable window.
   - why to move left pointer.
   - using hashmap to track characters.

key Takeaways:
  - Fixed windows have constant size
  - Variable window expand and shrink based on a condition.
  - fixed window reduce time complexity O(n^2) to O(n).

   
