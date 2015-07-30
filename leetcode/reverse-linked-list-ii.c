#include<stdio.h>
#include<stdlib.h>


//Definition for singly-linked list.
struct ListNode {
    int val;
    struct ListNode *next;
};

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseBetween(struct ListNode* head, int m, int n) {
    struct ListNode* hoh = NULL;//, tot = NULL;
    struct ListNode* cur = NULL;
    struct ListNode* nex = NULL;
    struct ListNode* tmp = NULL;
    int i=1;
    
    //extreme condition
    if(!head || !head->next || m==n)
        return head;
        
    //now definitely m<n
    for(i=1;i<m;i++){
        if(!hoh)
            hoh = head;
        else
            hoh = hoh->next;
    }
    if(!hoh)
        cur = head;
    else
        cur = hoh->next;

    if(!cur || !cur->next){
        return head;
    }
    nex = cur->next;
    i = m;
    while(i<n && nex){
        tmp = nex->next;
        nex->next = cur;
        cur = nex;
        nex = tmp;
        i++;
    }
    if(!hoh){
        head->next = nex;
        return cur;
    }
    else{
        hoh->next->next = nex;
        hoh->next = cur;
        return head;
    }
    
}
 
/* Codes below is for testing instead of for leetcode's solution */
struct ListNode* createList(int * array, int size){
        struct ListNode* head = NULL;
        struct ListNode* tmp = NULL;
        int i=0;
        if(size<=0)
                return NULL;
        
        head = (struct ListNode*)malloc(sizeof(struct ListNode));
        //head->val = array[0];
        tmp = head;
        for(i=0;i<size-1;i++){
            //tmp->val = *(array+i);
            tmp->val = array[i];
            tmp->next = (struct ListNode*)malloc(sizeof(struct ListNode));
            tmp = tmp->next;
        }
        //tmp->val = *(array+size-1);
        tmp->val = array[size-1];
        tmp->next = NULL;

        return head;
}

void printList(struct ListNode* head){
        if(!head)
                return;
        printf("%d", head->val);

        head = head->next;
        while(head){
                
                printf(" --> %d", head->val);
                head = head->next;
        }
        printf("\n");
}


int main(){
    int l[] = {1,2,3,4,5};
    int size = 5;
    struct ListNode* head = createList(l, size);
    printList(head);
    head = reverseBetween(head, 2, 5);
    printList(head);

    return 0;
}
