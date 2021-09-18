# Using python inbuilt eval() to evaluate the expression
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        def recurse(i,s,prev):
            if i>N-1:
                if eval(s)==target:
                    ans.append(s)
                return
            
            if prev!='0': recurse(i+1,s+num[i],prev)
            recurse(i+1,s+"+"+num[i],num[i])
            recurse(i+1,s+"-"+num[i],num[i])
            recurse(i+1,s+"*"+num[i],num[i])
        
        ans = []
        N = len(num)
        recurse(1,num[0],num[0])
        
        return ans


# With custom implementation to evaluate the expression
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        def evaluate(s):
            # Converting the expression to proper integer values
            stack = []
            temp = ""
            operations = ['+','-','*']
            for c in s:
                if c not in operations:
                    temp+=c
                else:
                    stack.append(int(temp))
                    stack.append(c)
                    temp = ''
                
            stack.append(int(temp))
            
            # Evaluating the expression
            total,prev = stack[0],stack[0]
            for n in range(1,len(stack)):
                if stack[n]=='+':
                    total+=stack[n+1]
                    prev = stack[n+1]
                elif stack[n]=='-':
                    total-=stack[n+1]
                    prev = -stack[n+1]
                elif stack[n]=='*':
                    total = (total - prev) + (prev * stack[n+1])
                    prev = prev*stack[n+1]
            
            return total
                
                
            
        def recurse(i,s,prev):
            if i>N-1:
                if evaluate(s)==target:
                    ans.append(s)
                return
            
            if prev!='0': recurse(i+1,s+num[i],prev)
            recurse(i+1,s+"+"+num[i],num[i])
            recurse(i+1,s+"-"+num[i],num[i])
            recurse(i+1,s+"*"+num[i],num[i])
        
        ans = []
        N = len(num)
        recurse(1,num[0],num[0])
        
        return ans

                
        