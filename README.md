# Eluvio-challenge-1

# Find Longest Strand Bytes Among Two Files
- Use dynaminc programming
  - Assume inputs are bytes1 and bytes2
    - dp[i][j] means the length of the longest common suffix of bytes[:i] and bytes[:j]
    - dp relation:
      - If i = 0 or j = 0, then dp[i][j] = 0
      - Else
        - If bytes1[i-1] = bytes2[j-1], then dp[i][j] = dp[i-1][j-1] + 1
        - Else, dp[i][j] = 0
  - With the above DP, length of longest common suffix of bytes[:i] and bytes[:j] can be found with double for-loops
    - Use a variable, `longestStrandLen`, to record currently-found longest length of common suffix
      - If I find a new common suffix whose length is larger than `longestStrandLen`
        - Update `longestStrandLen`
        - Besides, I use `ofst1` and `ofst2` to keep offsets of common suffix in two inputs
  - Space optimization
    - Above algorithm description involves a 2d-matrix (size m*n) for DP
      - Where m is the length of bytes1 and n is the length of bytes2
    - Size of matrix can be further reduced to (2 * min(m, n))
      - Because DP only uses information in the previous row
    - In my implementation, I will switch files to make the second file smaller
  - Complexity
    - Time complexity: O(mn)
      - Where m is the length of bytes1 and n is the length of bytes2
    - Space complexity: O(1)

# Main Function
- Get the list of files whose names are "sample.*"
- For every two files, use above DP to find the longest strand bytes among them and get corresponding offsets

# Dealing with Multiple Answer
- As mentioned in the email, there may be multiple longest strand of bytes
  - Ex:
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
    - Key is longest strand bytes and value is (offset1, offset2)
    - If longer one is found, clear hashtable and add longer one
    - If current one is of the same length, add it to the hashtable
  - In main function, similar idea is adopted

- Results
  - Command to execute: `python3 sol.py`
  - Result:
    ```
    ----- result -----
    27648 {('sample.2', 3072), ('sample.3', 17408)}
    total time: 3578.6750869750977 sec
    ```