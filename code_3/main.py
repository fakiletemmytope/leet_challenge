
def lengthOfLongestSubstring(s: str) -> int:
    list_of_substring= []    
    substring = []
    if len(s) <= 0:
        return 0
    else:
        for i in range(len(s)):
            #if ord(ch) >=97 or ord(ch) <=122:
                if s[i] not in substring:
                    print(s[i])
                    substring.append(s[i])
                elif s[i] in substring:            
                    #print(substring)
                    if s[i] != substring[-1]:
                        for j in range(len(substring)):
                            if substring[j] == [i]:
                                new_substring = substring[:j]
                                print(new_substring)
                                list_of_substring.append(len(substring))
                                substring = new_substring
                                #substring.append(value)
                                substring.append(s[i])
                                break
                    else:
                        list_of_substring.append(len(substring))            
                        substring = []
                        print(s[i])
                        substring.append(s[i])
                if i == len(s) - 1:
                    list_of_substring.append(len(substring))  
    print(f'updated list: {list_of_substring}')               
    if len(list_of_substring) == 0:
         return 0
    else:        
        list_of_substring.sort()
        value = list_of_substring[-1]
        return value

s = "ckilbkd"
print(lengthOfLongestSubstring(s))

s = "bbbbb"
print(lengthOfLongestSubstring(s))

s = "pwwkew"
print(lengthOfLongestSubstring(s))

s = ""
print(lengthOfLongestSubstring(s))

s = " "
print(lengthOfLongestSubstring(s))