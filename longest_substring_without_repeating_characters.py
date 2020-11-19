class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        time: O(n) - длина строки
        space: O(k) - число уникальных символов в строке

        1 - Solution
        substr = []
        maxLength = 0
        for char in s:
            if char in substr:
                substr = substr[substr.index(char) + 1:]
            substr.append(char)
            maxLength = max(len(substr), maxLength)
        return maxLength

        2 - Solution
        lst = list()
        for c in s:
            lst.append(c)
            if len(set(lst)) < len(lst):
                lst.pop(0)
        return len(lst)
        '''
        #3 - Solution

        start = -1
        max = 0
        dict = {}

        for i, val in enumerate(s):
            if val in dict and dict[val] > start:
                start = dict[val]
                dict[val] = i
            else:
                dict[val] = i
                if i - start > max:
                    max = i - start
        return max
