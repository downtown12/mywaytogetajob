i#anagrams: 异序词. 字母成分完全相同但子母排列顺序不同的字符串。例: lives 是 Elvis 的一个异序词.
#The idea:
#1. create a Hash function strtoint for each node. This function can map a string to an integer number. 通过26进制
#    This is because compare integer numbers is faster than strings. (a decoded string can be seen as zero or more integers).
#2. create a dictionary that maps the integer number of each string to a list. 
#    This list record the indexes of the same interger numbers occur in the string list.
#3. find out the more-than-one-element lists in the dictionary's values. 
#   These lists is the indexes of anagrams
#
class Solution:
    #convert a string to a single integer
    def strtoint(self, str):
        #the character start from 1(a) to 26(z), 
        #the character not start from zero is important for cases like 'abuts, buts'
        int_list = [ord(c) - ord('a')+1 for c in str]
        int_list.sort();
        res = 0
        #calculate 
        for i in int_list:
            #a remaining question: Is res *= 25 (or any number that is not 26) ok for this problem?
            res *= 26
            res += i
        
        return res
    
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        int_strs_list = [self.strtoint(str) for str in strs]
        int2index = dict()
        
        for i in range(len(int_strs_list)):
            #search a key in a dictionary costs O(lg(n)) time complexity.
            #search all keys in a dictionary costs O(nlg(n)) time complexity
            #which equals common sort's time consuming.
            if not int_strs_list[i] in int2index:
                int2index[int_strs_list[i]] = [i]
            else:
                int2index[int_strs_list[i]].append(i)
        
        res = []
        for index_list in int2index.values():
            if len(index_list)>1:
              res += [strs[i] for i in index_list]
        
        return res
            
