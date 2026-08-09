class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        ans=[]
        for i in tokens:
            if i.lstrip('-').isdigit():
                ans.append(int(i))

            elif i == '+':
                b=ans.pop()
                a=ans.pop()
                ans.append(a+b)
            elif i == '-':
                b=ans.pop()
                a=ans.pop()
                ans.append(a-b)
            elif i == '*':
                b=ans.pop()
                a=ans.pop()
                ans.append(a*b)
            elif i == '/':
                b=ans.pop()
                a=ans.pop()
                ans.append(int(a/b))


        return ans[-1]

    


        


        