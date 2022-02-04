def main():
    import glob
    from collections import defaultdict

    LSBs = defaultdict(set)
    currLSBLen = 0
    files = glob.glob("sample.*")
    for i in range(len(files)):
        for j in range(i + 1, len(files)):
            file1 = files[i]
            file2 = files[j]
            bytes1 = readBinaryFile(file1)
            bytes2 = readBinaryFile(file2)

            # make smaller one be the second one
            if len(bytes2) > len(bytes1):
                file1, file2 = file2, file1
                bytes1, bytes2 = bytes2, bytes1

            subLSBs = longestStrandByte(bytes1, bytes2)

            # deal with multiple answers
            for byteStrand, ofsts in subLSBs.items():
                if len(byteStrand) > currLSBLen:
                    currLSBLen = len(byteStrand)
                    LSBs.clear()
                    LSBs[byteStrand].add((file1, ofsts[0]))
                    LSBs[byteStrand].add((file2, ofsts[1]))
                elif len(byteStrand) == currLSBLen:
                    LSBs[byteStrand].add((file1, ofsts[0]))
                    LSBs[byteStrand].add((file2, ofsts[1]))
                else:
                    break

    print('----- result -----')
    for k, v in LSBs.items():
        print(len(k), v)

    return LSBs

def readBinaryFile(fileName):
    result = bytes()
    with open(fileName, "rb") as f:
        line = f.readline()
        while line:
            result += line
            line = f.readline()

    return result

def longestStrandByte(bytes1, bytes2):
    from collections import defaultdict

    m, n = len(bytes1), len(bytes2)
    dp = [[0 for j in range(n + 1)] for i in range(2)]
    longestStrandLen, ofst1, ofst2, LSBs = 0, None, None, defaultdict(tuple)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            currRow = i % 2
            if bytes1[i-1] == bytes2[j-1]:
                prevRow = (i - 1) % 2
                dp[currRow][j] = dp[prevRow][j-1] + 1
                if dp[currRow][j] > longestStrandLen:
                    longestStrandLen = dp[currRow][j]
                    ofst1, ofst2 = (i - longestStrandLen), (j - longestStrandLen)
                    LSBs.clear()
                    LSBs[bytes1[ofst1:ofst1+longestStrandLen]] = (ofst1, ofst2)
                elif dp[currRow][j] == longestStrandLen:
                    ofst1, ofst2 = (i - longestStrandLen), (j - longestStrandLen)
                    LSBs[bytes1[ofst1:ofst1+longestStrandLen]] = (ofst1, ofst2)
            else:
                dp[currRow][j] = 0

    return LSBs

if __name__ == "__main__":
    from time import time
    t1 = time()
    main()
    t2 = time()
    print(f'total time: {t2 - t1} sec')