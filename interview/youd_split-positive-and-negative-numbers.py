#!encoding=utf-8
# 将一个数组里面的正数和负数分开，数组里原来的正数的顺序和负数的顺序不能打乱
# 比如 给一个数组 3 -4 2 6 -7 8 -9,
# 输出的是 3 2 6 8 -4 -7 -9
# 
# 要求: 空间复杂度为常数级

def PositiveNegative(array):
        positive_end = -1 #End position of positive numbers.
        tmp = 0

        #traverse the array once
        for cur_pos in range(len(array)):
            if array[cur_pos]>0:
                    #meet one positive number
                    tmp = array[cur_pos]
                    #move every element backward one position from positive_end to cur_pos
                    for i in range(cur_pos-1, positive_end, -1):
                            array[i+1] = array[i]
                    
                    positive_end+=1
                    array[positive_end] = tmp

        return array

a = [3, -4, 2, 6, -7, 8, -9]
a = [-4, -8, -6, 4, -9, 3,2,1]
print PositiveNegative(a)
