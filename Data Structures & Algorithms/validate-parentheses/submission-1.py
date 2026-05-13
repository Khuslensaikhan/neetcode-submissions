class Solution:
    def isValid(self, s: str) -> bool:
        # use stack
        stack = []
        # use dict to check the parentheses but how? 
        check = {")" : "(", "]" : "[", "}" : "{"}

        # add open parentheses to stack
        for char in s:
            if char in check: 
                #closing
                if stack and stack[-1] == check[char]:
                    stack.pop()
                else: 
                    return False
            else: 
                #opening
                stack.append(char)
        return not stack
