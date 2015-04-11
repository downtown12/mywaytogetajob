/* The idea of this solution is that:
 * Firstly, sort the array "A" in O(nlgn) complexity, here i use merge sort algorithm.
 * Meanwhile, I create another array called "Order" to maps the the value to its orignal position during sorting.
 * 
 * Then, because the array is sorted, I can traverse the SORTED array "A" from begining to end. Once I find a element i and and another element j behind i that j == target -i, return the indices of i and j (of course make sure index1 is smaller than index2 before return).
 *
 * The time complexity: 
 * Sort: O(nlgn)
 * Traversing the Array and Binary Searches: maximun n-1 times of traversing * (lgn) for every binary searches. So the time complexity of this step is O(nlgn).
 * So the sum comlexity is 2*(O(nlgn)). Smaller than brute force search O(n^2)
 *
 * */

#include<stdio.h>
#include<stdlib.h>

void merge(int A[], int Order[], int p, int q, int r){
    int n1 = q-p+1;
    int n2 = r-q;
    int * A1 =NULL;
    int * Order1 =NULL;
    int * A2 =NULL; 
    int * Order2 =NULL; 
    int i = 0;
    int j = 0;
    int k = 0;
    
    if(n1>0){
    	A1 = (int*)malloc(sizeof(int) * n1);
    	Order1 = (int*)malloc(sizeof(int) * n1);
    }
    if(n2>0){
    	A2 = (int*)malloc(sizeof(int) * n2);
	Order2 = (int*)malloc(sizeof(int) * n2);
    }

    //initialize A1 and A2
    for(i=0;i<n1;i++){
        *(A1+i) = *(A+p+i);
        *(Order1+i) = *(Order+p+i);
    }
    for(i=0;i<n2;i++){
        *(A2+i) = *(A+q+1+i);
        *(Order2 + i) = *(Order+q+1+i);
    }
    //reset i
    i = 0;
    
    //if(p<q){
        while(j < n1 && k < n2){
            //put the smaller one into array A
            if( *(A1+j) < *(A2+k) ){
                A[p+i] = *(A1+j);
                Order[p+i] = *(Order1+j);
                j++;
            }
            else{
                A[p+i] = *(A2+k);
                Order[p+i] = *(Order2+k);
                k++;
            }
            i++;
        }
        
        while(j<n1){
            A[p+i] = *(A1+j);
            Order[p+i] = *(Order1+j);
            j++;
            i++;
        }
        while(k<n2){
            A[p+i] = *(A2+k);
            Order[p+i] = *(Order2+k);
            k++;
            i++;
        }
    //}
    
    if(A1)
    	free(A1);
    if(A2)
    	free(A2);
    if(Order1)
    	free(Order1);
    if(Order2)
    	free(Order2);
    
    return;
}

void mergesort(int A[], int Order[], int p, int r){
    if(r<=p)
	    return;

    int q = (p+r)/2;
    mergesort(A, Order, p, q);
    mergesort(A, Order, q+1, r);
    merge(A, Order, p,q,r);
}

/*
    二分查找数组A[]中是否存在val这个数，若存在，假设这个值在A中的下标是i，于是返回Order数组中下标是i的那个元素；
    若没有找到这个数，返回-1；
    Order数组表示的内容是：A数组在排序好之前时的数组元素顺序。
*/
int bisearch(int A[], int Order[], int p, int r, int val){
    int low = p;
    int high = r;
    int mid = (low + high)/2;
    
    if(low<=high){
        if(val == A[mid]){
            return Order[mid];
        }
        else if(val < A[mid]){
            bisearch(A, Order, p, mid-1, val);
        }
        else{//val > A[mid]
            bisearch(A, Order, mid+1, r, val);
        }
    }
    else{
        //can't find the val in array A
        return -1;
    }
}


int *twoSum(int numbers[], int n, int target) {
    int * Order = (int*)malloc(sizeof(int)*n);
    int i;
    for(i=0;i<n;i++)
        *(Order+i) = i+1;
    int * indices = NULL;
    
    mergesort(numbers, Order, 0, n-1);
    int ind1 = 0;
    
    for(i=0; i<n-1 ;i++){
        if( (ind1 = bisearch(numbers, Order, i+1 , n-1, target-numbers[i])) >=0){
            //Order[i] and ind1 is the indices
            indices = (int *)malloc(sizeof(int)*2);
	    //This if makes sure that the first indices is the smaller one
	    if(Order[i]<=ind1){
           	 *indices = Order[i];
            	 *(indices+1) = ind1;
	    }
	    else{
           	 *indices = ind1;
            	 *(indices+1) = Order[i];
	    }
            return indices;
        }
    }
}
