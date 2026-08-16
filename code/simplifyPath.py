class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for comp in path.split('/'):
            if comp == '' or comp == '.':
                continue
            elif comp == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(comp)
        return '/' + '/'.join(stack)
