/*
 * https://leetcode.com/problems/sort-list/
 *
 * Sort a linked list in O(n log n) time using constant space complexity.
 *
 * Here is a merge sort solution.
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

class Solution {
public:
            ListNode *sortList(ListNode *head) {
                head = MergeSort(head,0,GetLength(head)-1);
            return head;
        }

        ListNode * MergeSort(ListNode *head, int p, int r)
        {
                if(r<=p) return head;
                //Get the partition boundary
                int q = (p+r)/2;

                ListNode * L_ptr = GetItem(head, p);
                ListNode * L_end_ptr = GetItem(L_ptr, q-p);

                ListNode * R_ptr = NULL;
                if(L_end_ptr != NULL)
                        R_ptr = L_end_ptr->next;
                L_end_ptr->next = NULL;
                ListNode * R_end_ptr = GetItem(R_ptr, r-q-1);
                R_end_ptr->next = NULL;

                L_ptr = MergeSort(L_ptr,p,q);
                R_ptr = MergeSort(R_ptr,0,r-(q+1));

                head = Merge(L_ptr, R_ptr);
                return head;
        }
        
                ListNode * Merge(ListNode * L_ptr, ListNode * R_ptr)
        {
                //GetItem 
                ListNode * newhead = new ListNode(-1);

                ListNode * cur_ptr = newhead;
                //Merge it.
                while(L_ptr!=NULL && R_ptr!=NULL){
                        if(L_ptr->val <= R_ptr->val){
                                cur_ptr->next = L_ptr;
                                cur_ptr = cur_ptr->next;
                                L_ptr = L_ptr ->next;
                        }
                        else{
                                cur_ptr->next = R_ptr;
                                cur_ptr = cur_ptr->next;
                                R_ptr = R_ptr->next;
                        }
                }
                if(L_ptr != NULL)
                        cur_ptr->next = L_ptr;
                else cur_ptr->next = R_ptr;

                ListNode * tmphead = newhead;
                newhead = newhead->next;
                tmphead->next = NULL;
                delete(tmphead);

                return newhead;
        }

        ListNode * GetItem(ListNode * head, int index)
        {
                ListNode * tmp = head;
                for(int i=0;i<index;i++){
                        if(tmp == NULL) return NULL;
                        tmp = tmp->next;
                }
                return tmp;
        }

        int GetLength(ListNode * head)
        {
                int i = 0;
                ListNode * tmp = head;
                for(i=0;tmp!=NULL;i++)
                        tmp = tmp->next;
                return i;
        }

};
