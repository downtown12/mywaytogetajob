/*
 * This is an implementation of heap sort algorithm in iterative way, which is not recursive.
 * */
#include<stdio.h>

inline int PARENT(i){
	return (i-1)/2;
}

inline int LEFT(int i){
	return 2*i+1;
}

inline int RIGHT(int i){
	return 2*i+2;
}

void printArray(int a[],int len)
{
	int i;
	for(i=0;i<len;i++)
		printf("%d ",a[i]);
	putchar('\n');
}

//maxHeapify: make the heap roots from idx a maxified heap.
void maxHeapify(int heap[] , int len, int idx){
	int l;
	int r;
	int largest;

	int temp;

	//len/2-1: leaf nodes of the heap do not need to be maxified.
	while(idx <= len/2-1){
			l = LEFT(idx);
			r = RIGHT(idx);			
			largest = idx; 			
			
			//maybe l<=len-1 is useless
			if(l<=len-1 && heap[l]>heap[largest]){
				largest = l;
			}
			if(r<=len-1 && heap[r]>heap[largest]){
				largest = r;
			}
			if(largest != idx){
				//swap
				temp = heap[idx];
				heap[idx] = heap[largest];
				heap[largest] = temp;

				idx = largest;
			}
			else{
				//already a maxified heap
				return;
				//idx++;
			}
	}
	return;

}

//Build a max heap
void buildMaxHeap(int heap[] , int len){
	int i;
	for(i=len/2-1;i>=0;i--){
		maxHeapify(heap,len,i);
	}
}

//heap sort main procedures
void heapSort(int heap[] , int len){
	int i = len-1;
	int temp;

	buildMaxHeap(heap,len);

	for(i=len-1;i>=1;i--){
		//switch the heap's root (the biggest element) with its last element
		temp = heap[0];
		heap[0] = heap[i];
		heap[i] = temp;

		//put the new root to the right place
		//notice that the size of the heap is shrinking
		maxHeapify(heap, i, 0);
	}
}

int main()
{
	int a[] = {4,3,1,6,5,2,7};
	int len = 7;
	int b[]={3,3,3,3,1};

	printArray(a,len);
	printArray(b,2);

	heapSort(a,len);
	heapSort(b,5);

	printf("after sorted:");
	printArray(a,len);
	printArray(b,5);
	return 0;
}

