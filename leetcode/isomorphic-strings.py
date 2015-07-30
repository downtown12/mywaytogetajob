'''
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.o
'''

'''
    Here I come up with two different solutions, which are in different thoughts of map.
    The easyToThinkOutSolution uses two dictionary to map from string s to string t as well as from string t to string s.
    
    The subtleSolution is just like it's name, it's SUBTLE!!!
    "The main idea is to store the last seen positions of current (i-th) characters in both strings. 
    If previously stored positions are different then we know that the fact they're occuring in the current i-th position simultaneously is a mistake. 
    We could use a map for storing but as we deal with chars which are basically ints not bigger than 255 and can be used as indices we can do the whole thing with an array."
    The value of the one index of the array is the last seen position(starts from 1) of current character. 0 if current character has not occured till now.
    
    ord('s'): transfer a character to ASCII value(int)
    chr(115): transfer a ASCII value(int) to a one-charater-string.
'''

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        return self.subtleSolution(s,t)
    
    def subtleSolution(self, s, t):
        pos_s = [0]*256
        pos_t = [0]*256
        
        for i in range(len(s)):
            if not pos_s[ord(s[i])] == pos_t[ord(t[i])]:
                return False
            pos_s[ord(s[i])] = i+1
            pos_t[ord(t[i])] = i+1
        
        return True

            
    def easyToThinkOutSolution(self, s, t):
        stot = dict()
        ttos = dict()
        #replist = []
        for i in range(len(s)):
            if not s[i] in stot:
                stot[s[i]] = t[i]
            if not t[i] in ttos:
                ttos[t[i]] = s[i]
            
            #replist.append(chdict[s[i]])
            if not stot[s[i]] == t[i] or not ttos[t[i]] == s[i]:
                return False
        
        return True
