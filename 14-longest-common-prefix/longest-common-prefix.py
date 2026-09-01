class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1:
            return strs[0]
        strings=""
        count=0
        for i in range(len(strs[0])):
            letter=strs[0][:i+1]  
            count=0
            for j in range(1,len(strs)):
                
                if letter==strs[j][:i+1]:
                    count+=1
                    if count==len(strs)-1:
                       strings=letter
                else:
                    return strings
            
        return strings
            