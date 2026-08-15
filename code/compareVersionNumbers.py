class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        split1 = version1.split(".")
        split2 = version2.split(".")

        lenv1 = len(split1)
        lenv2 = len(split2)

        if lenv1 < lenv2:
            diff = lenv2 - lenv1
            while diff > 0:
                split1.append("0")
                diff -= 1
        elif lenv1 > lenv2:
            diff = lenv1 - lenv2
            while diff > 0:
                split2.append("0")
                diff -= 1

        for i in range(0, len(split1)):
            if int(split1[i]) < int(split2[i]):
                return -1
            elif int(split1[i]) > int(split2[i]):
                return 1
        return 0
