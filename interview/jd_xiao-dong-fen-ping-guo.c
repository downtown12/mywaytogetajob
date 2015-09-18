
/****
 * 2016-09-19
 * 京东笔试：晓东分苹果问题， 与猴子猴子分桃问题一样：
 * 五只猴子分一堆桃。半夜，第一只猴子先起来，它把桃分成了相等的五堆，多出一只。于是，它吃掉了一个，拿走了一堆； 
 * 第二只猴子起来一看，只有四堆桃。于是把四堆合在一起，分成相等的五堆，又多出一个。于是，它也吃掉了一个，拿走了一堆；
 * ......其他几只猴子也都是 这样分的。问：这堆桃至少有多少个？
 * http://blog.csdn.net/ljsspace/article/details/6803632
 *
 * 只不过，现在桃子的数量不是5，而是任意的一个数N（N>=0），求桃子总数。
 *
 * 猴子分桃分析：
 *
 * 设第一只到第五只猴子分的每个堆的大小分别为a, b, c, d, e。那么满足如下的关系：
 * 4*a = 5*b+1  。。。。（1）//第一只猴子走后剩下的桃子数为4*a; 第二只猴子将这些桃分成5堆，每堆大小为b (以下关系式类似)
 * 4*b = 5*c+1  。。。。（2）
 * 4*c = 5*d+1  。。。。（3）
 * 4*d = 5*e+1  。。。。（4） //第五只猴子在第四只猴子走后的分法是5*e+1
 *
 * 消除中间变量(推导过程省略)，只保留a和e，得到关系式：
 * 4^4*a=5^4*e + 369
 * 
 * 求通解：
 * Say h[1] is the ammount of pearls the 1st monkey get.
 * h[n] is the the ammount of pearls the last monkey get.

 * Then the relationship between h[1] and h[n] is:
 *   (n-1)^(n-1) * h[1] = n^(n-1) * h[n] + constant
 *   And the constant is: constant = n^(n-2) * (n-1)^0 + n^(n-2-1) * (n-1)^1 + ... + n^0 * (n-1)^(n-2)
 *   That is n-2 is the max power of constant.
 
 * With the formulas above, we must make sure the h[n] can make h[1] an integer.
 * So we try h[n] from 1 to (n-1)^(n-1).
 * The last number: (n-1)^(n-1) absolutely can make h[1] an integer. So set it as the boundary.
 
 * Then the original sum of pearls is: sum = n*h[1]
 *
 * Now the problem solved.
****/
#include<stdio.h>
#include<stdlib.h>
#include<math.h>

//calculate the constant
//constant = n^(n-2) * (n-1)^0 + n^(n-2-1) * (n-1)^1 + ... + n^0 * (n-1)^(n-2)
int calConstant(n)
{
        int i=0;
        int constant = 0;
        for(i=0;i<=n-2;i++){
                constant+=(int)(pow(n-1,i) * pow(n,n-2-i));
        }
        //printf("constant: %d\n",constant);
        return constant;
}


int getSumPearls(int n){
        int i = 0;
        //the relationship formula is : (n-1)^(n-1) * h[1] = n^(n-1) * h[n] + constant
        //sum_right is the result right of the equation.
        int sum_right = 0;
        //sum_xd is h[1]
        int sum_xd = 0;
        int constant = calConstant(n);
        //w_xd: weight of xiaodong: (n-1)^(n-1)
        int w_xd = pow(n-1, n-1);
        
        //start trying...
        for(i=1;i<=w_xd;i++){
            sum_right = i*pow(n,n-1)+constant;
            if(sum_right%w_xd == 0){
                   sum_xd = sum_right/w_xd;
                   return sum_xd*n+1;
            }
        }
        return sum_right;
}

int main()
{
        printf("sum of pearls: %d\n", getSumPearls(5));
        return 0;
               
}




