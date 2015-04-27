#include<stdio.h>

//function partition returns the pivot's index
int partition(int A[], int p, int q)
{
	//note that the smaller group of numbers starts from -1
	int small_end = p-1;
	int j;
	int pivot = A[q];
	int temp;
	
	for(j=p;j<=q-1;j++){
		if(A[j]<= pivot){
			small_end++;
			//switch A[small_end] with A[j]
			temp = A[small_end];
			A[small_end] = A[j];
			A[j] = temp;
		}
	}

	//put the pivot into the right place,
	//that is switch A[q] with A[small_end+1].
	A[q] = A[small_end+1];
	A[small_end+1] = pivot;

	return small_end+1;
}


void quicksort(int A[], int p, int q)
{
	int k;

	//extreme condition: only one element or less than one elemernt
	if(q-p <= 0)
		return;

	k = partition(A, p, q);
	quicksort(A, p, k-1);
	quicksort(A, k+1, q);
}

void printarray(int A[], int n)
{
	int i;
	printf("The array is : \n");
	for(i=0;i<n;i++)
		printf("%d ", A[i]);
	printf("\n");
}

int main(){
         int A1[] = {}; 
         int A2[] = {3}; 
         int A3[] = {2,1}; 
         int A4[] = {5,4,2,8,7,1,6,3};
	
	 quicksort(A4, 0, 7);
	 printarray(A4,8);

	 quicksort(A3,0,1);
	 printarray(A3,2);
	 return 0;
}
