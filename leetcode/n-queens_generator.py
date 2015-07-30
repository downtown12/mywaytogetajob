'''
关于递归层次的分析
调用顺序：
first layer，也就是最外围的queens()会首先生成第一行的皇后可能在的pos（通过conflict函数）；接着，pos值会追加到state元组 的后边，并把它作为参数，调用第二层的queens()（第14行）；在不久的将来接到第二层的返回结果后，通过第15行的yield把结果返回给上层调 用者，也就是主函数；

second layer: 会首先生成第2行的皇后可能在的pos；接着，pos值会追加到state元组的后边，并作为参数，调用第三层的queens()（第14行）；通过第15行的yield把结果返回给上层调用者，也就是第一层的queens()；

...

8th layer: 这是递归中最里边的一层调用，在找到not conflict的一个pos值后，由于len(state) == num-1 is True, 他会把该pos值yield给上一层的调用者，也就是第七层的queens()函数。


返回顺序：
在第七层中，收到第八层传出来的一个值会放在result里（14行），从而进入15行，将(pos,) + result yield给第六层；
第六层接着将收到的第七层传出来的结果放在result里， yield给第五层
...
直到第一层收到的第二层传出来的结果放在result里，这时(pos,) + result是8个位置的值，把它们yield给主函数



每个queens()函数中不服合要求的可能（conflict返回值是Ture的分支，或者第9行的for循环结束）都会触发StopIteration异常而结束，并不会产生yield值出来。
'''
def conflict (state, nextY):
    nextX = len (state)
    for i in range( len(state )):
        if abs( state[i ] - nextY) in ( 0, nextX -i):
            return True
    return False
   

def queens (num = 8 , state=()):
    for pos in range( num):
        if not conflict(state , pos):
            if len( state) == num- 1:
                yield ( pos,)
            else:
                for result in queens(num , state+( pos,)):
                    yield ( pos,) + result

ns=0
qs = queens ()
for i in qs:
    ns+=1
    print i
print 'number of solutions: ' , ns

