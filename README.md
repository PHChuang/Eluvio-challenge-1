# Eluvio-challenge-1

# Find Longest Strand Bytes Among Two Files
- Use dynaminc programming
  - Assume inputs are bytes1 and bytes2
    - dp[i][j] means the length of the longest common suffix of bytes[:i] and bytes[:j]
    - dp relation:
      - if i = 0 or j = 0, then dp[i][j] = 0
      - else
        - if bytes1[i-1] = bytes2[j-1], then dp[i][j] = dp[i-1][j-1] + 1
        - else, dp[i][j] = 0
  - with the above DP, length of longest common suffix of bytes[:i] and bytes[:j] can be found with double for-loops
    - use a variable, `longestStrandLen`, to record currently-found longest length of common suffix
      - if I find a new common suffix whose length is larger than `longestStrandLen`
        - update `longestStrandLen`
        - besides, I use `ofst1` and `ofst2` to keep offsets of common suffix in two inputs
  - Space optimization
    - Above algorithm description involves a 2d-matrix (size m*n) for DP
      - where m is the length of bytes1 and n is the length of bytes2
    - Size of matrix can be further reduced to (2 * min(m, n))
      - because DP only uses information in the previous row
    - In my implementation, I will switch files to make the second file smaller
  - Complexity
    - Time complexity: O(mn)
      - where m is the length of bytes1 and n is the length of bytes2
    - Space complexity: O(1)

# Main Function
- Get the list of files whose names are "sample.*"
- For every two files, use above DP to find the longest strand bytes among them and get corresponding offsets

# Dealing with Multiple Answer
- As mentioned in the email, there may be multiple longest strand of bytes
  - ex:
    ```
    inputs:
        file1: "abcxdef"
        file2: "abcyydef"
        file3: "abc"

    my outputs:
        LSBs = {
            "abc": [(file1, 0), (file2, 0), (file3, 0)]
            "def": [(file1, 4), (file2, 5)]
        }
    ```
- Method to Handle Multiple Answer
  - During DP, use a hashtable to store all longest strand bytes
    - key is longest strand bytes and value is (offset1, offset2)
    - if longer one is found, clear hashtable and add longer one
    - if current one is of the same length, add it to the hashtable
  - In main function, similar idea is adopted