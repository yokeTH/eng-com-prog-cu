# 2565_1_Quiz_2_2

def match(word, pattern, include_chars, exclude_chars):
    if len(word) == len(pattern):
        questionPattern = []
        for i in range(len(word)):
            if pattern[i] == '?':
                questionPattern.append(word[i])
            elif pattern[i] != word[i]:
                return False
            
        for e in exclude_chars:
            if e in questionPattern:
                return False
            
        for e in include_chars:
            if e in questionPattern:
                questionPattern.remove(e)
            else:
                return False
        
        return True

    else:
        return False
    
exec(input())