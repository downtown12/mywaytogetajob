#include<stdio.h>
#include<stdlib.h>

int merge(int *a,int left_end, int right_end){
	int * l = NULL;
	int * r = NULL;

	int i=0,j = 0,k=0;

	l = (int*)malloc(sizeof(int)*(left_end+1));
	r = (int*)malloc(sizeof(int)*(right_end-left_end));
	if(!l || !r){
		fprintf(stderr, "malloc error for pointer l or r");
		//-1 means returning unproperly
		return -1;
	}

	//init l and r
	for(i=0;i<=left_end;i++)
		*(l+i) = *(a+i);
	for(j=left_end+1;j<=right_end;j++)
		*(r+j-left_end-1) = *(a+j);
	

	i=0;
	j=0;
	k=0;
	while(i<=left_end && j<=right_end-left_end-1){
		if(*(l+i) <= *(r+j))
			*(a+k++) = *(l+i++);
		else
			*(a+k++) = *(r+j++);

	}

	//append the rest of the element
	for(;i<=left_end;)
		*(a+k++)  = *(l+i++);
	for(;j<=right_end - left_end - 1;)
		*(a+k++)  = *(r+j++);

	free(l);
	free(r);
	return 0;

}

void mergeSort(int a[], int len){
		int l_len = len/2;

		//extreme condition
		if(len<=1)
			return;
		mergeSort(a,l_len);
		mergeSort(&(a[l_len]),len-l_len);
		merge(a,l_len-1,len-1);

		return;

}

void printArray(int A[], int n)
{
    int i;
    printf("The array is : \n");
    for(i=0;i<n;i++)
        printf("%d ", A[i]);
    printf("\n");
}


int main()
{
	int a[] = {4,6,7,3,0,8,9,1};
	int b[] = {1};
	mergeSort(a,8);

	printArray(a,8);

	mergeSort(b,1);
	printArray(b,1);

	return 0;
}
