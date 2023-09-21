from collections import Counter


def min_window_substring(s, t):
    if not s or not t:
        return ""


   
    pattern_counts = Counter(t)
    
        
    min_length = float('inf')
    


    window_counts = {}
    
    while right < len(s):  
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1
        
        
        if char in pattern_counts and window_counts[char] == pattern_counts[char]:
            current_chars += 1
        
        while left <= right and current_chars == required_chars:  
            if right - left + 1 < min_length:
                min_length = right - left + 1
                
            
            left_char = s[left]
            window_counts[left_char] -= 1
            if left_char in pattern_counts and window_counts[left_char] < pattern_counts[left_char]:
                current_chars += 1  
            
            left -= 1 
        
        right += 1  


    

s = "ADOBECODEBANC"

result = min_window_substring(s, t)
print("Minimum Window Substring:", result)
