def isPalindrome(x: int) -> bool:
        actual = []
        reverse= []
        if x <= 0:
            return False
        else:
            string = str(x)
            for ch in string:
                actual.append(ch)
            for i in reversed(string):
                reverse.append(i)
        print(actual)
        print(reverse)
        if actual  == reverse:
            return True
        else:
            return False
        
isPalindrome(10)

