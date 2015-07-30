# Dynamic programming formula:  E(i,j) = min{E(i-1,j) + D, E(i, j-1) + A, E(i-1, j-1) + R };
# E(i, j) = edit distances to convert string1(length is i) to string2(length is j).
# D: cost of deleting.
# A: cost of adding a character.
# R: cost of replacing a character.R = 0 if string1[i-1] == string2[j-1], else 1.


class Solution:
    # @param word1, a string
    # @param word2, a string
    # @return an integer
    def minDistance(self, word1, word2):
        return self.simplified_solution(word1, word2)

    #complete_solution takes O(m*n) space complexity to record every edit distance
    #from E[0][0] to E[m][n].
    def complete_solution(self, word1, word2):
        len1 = len(word1)
        len2 = len(word2)
        #init the distance matrix
        #note how i init this matrix
        dstc_mtrx = [[-1]*(len2+1) for i in range(len1+1)]
        #the below init way is wrong cause every sub-list refers the same address,
        #if you change a element of one sub-list, every sub-list changes.
        #A WRONG WAY: dstc_mtrx = [[-1]*(len2+1)] * (len1+1)


        #init E(0,0), E(0, j) 
        for j in range(len2+1):
            dstc_mtrx[0][j] = j
        for i in range(len1+1):
            dstc_mtrx[i][0] = i

        for i in range(1,len1+1):
            for j in range(1,len2+1):
                left_is_del = dstc_mtrx[i][j-1] + 1
                up_is_add = dstc_mtrx[i-1][j] + 1
                corner_is_rep = dstc_mtrx[i-1][j-1] + (not word1[i-1] == word2[j-1])
                dstc_mtrx[i][j] = min(left_is_del, up_is_add, corner_is_rep)

        return  dstc_mtrx[-1][-1]

    #simplified_solution only uses O(n) space complexity.
    def simplified_solution(self, word1, word2):
        len1, len2 = len(word1), len(word2)
        dstc_list = [i for i in range(len2+1)]

        for i in range(1,len1+1):
            #init the corner and dstc_list[0] at the beging of each line
            corner_is_rep = dstc_list[0]
            dstc_list[0] = i

            for j in range(1,len2+1):
                #dstc_list[j] +1: E(i-1,j) +A , dstc_list[j-1]+1: E[i,j-1]+D,
                #corner_is_rep+ ...: E[i-1,j-1]+R
                corner_is_rep, dstc_list[j] =dstc_list[j], min(dstc_list[j]+1, dstc_list[j-1]+1, corner_is_rep + (not word1[i-1]==word2[j-1]))
                          
        return dstc_list[-1]
                        

