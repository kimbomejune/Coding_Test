# DetermineIfStringHalvesAreAlike

# You are given a string [s] of even length. Split this string into two halves of equal lengths, and let [a] be the first half and [b] be the second half.
# 임의의 문자열 s(짝수)를 반으로 나누어 a(처음부터 반까지 문자열), b(반부터 끝까지 문자열)로 구분한다
# Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.
# 두개의 문자열은 동일한 수의 모음을 가질때 같다. s에는 대문자 및 소문자가 포함되어있다.
# Return true if a and b are alike. Otherwise, return false.
# 반환값은 a, b가 같다면 true 아니라면 false


"""
EX)
Input: s = "book"
Output: true
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.
"""

"""
Constraints)
2 <= s.length <= 1000
s.length is even.
s consists of uppercase and lowercase letters.
"""

# ==========================================
#                 START !!!
# ==========================================

def DetermineIfStringHalvesAreAlike(s: str) -> bool:
    a_vowels = 0
    b_vowels = 0
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    s_length = len(s)
    
    if((s_length % 2) == 0 and 2 <= s_length <= 1000):
        s_half_index = int(s_length/2)
        a = s[0:s_half_index]
        b = s[s_half_index:s_length]
        for i in vowels:
            a_vowels = a_vowels + a.count(i)
            b_vowels = b_vowels + b.count(i)
        if(a_vowels == b_vowels):
            return True
        else:
            return False
    else:
        print(s_length)
        return False


print(DetermineIfStringHalvesAreAlike("book"))