from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        n = len(words)
        i = 0

        res = []
        currLine = []
        counter = 0

        while i < n:
            currLine.append(words[i])
            counter += len(words[i])

            if counter + (len(currLine) - 1) > maxWidth:
                del currLine[(len(currLine) - 1)]
                counter -= len(words[i])
                i -= 1
                
                totalSpaces = maxWidth - counter
                numGap = len(currLine) - 1
                if numGap == 0:
                    line = currLine[0]
                    line += " " * (maxWidth - len(currLine[0])) 
                else:
                    base = totalSpaces // numGap
                    remainder = totalSpaces % numGap
                    line = ""
                    for j in range(numGap):
                        line += currLine[j]
                        spaces = base + (1 if j < remainder else 0)
                        line += " " * spaces
                    line += currLine[-1]

                res.append(line)
                currLine = []
                counter = 0

            i += 1

        lastLine = " ".join(currLine)
        lastLine += " " * (maxWidth - len(lastLine))
        res.append(lastLine)
        return res