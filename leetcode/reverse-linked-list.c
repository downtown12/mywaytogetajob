/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
 
struct ListNode* reverseItr(struct ListNode* head){
    struct ListNode* cur = head;
    struct ListNode* nex = NULL;
    struct ListNode* tmp = NULL;
    
    if(!head || !head->next)
        return head;
    
    nex = head->next;
    while(nex){
        tmp = nex->next;
        
        nex->next = cur;
        cur = nex;
        nex = tmp;
    }
    head->next = NULL;
    return cur;
}

struct ListNode* reverseRcsv(struct ListNode* cur, struct ListNode* nex){
    struct ListNode* tmp= nex;
    //struct ListNode* tail = NULL;
    if(!nex)
        return cur;
    else{
        tmp = nex->next;
        nex->next = cur;
        return reverseRcsv(nex, tmp);
    }
}

struct ListNode* reverseList(struct ListNode* head) {
/*
    struct ListNode* tail = NULL;
    if(!head)
        return head;
    
    tail = reverseRcsv(head, head->next);
    head->next = NULL;
    return tail;
*/
    return reverseItr(head);
}
