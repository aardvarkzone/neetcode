/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* prev = nullptr; 
        ListNode* curr = head; 
        ListNode* temp = nullptr;

        while (curr) { 
            //store the next node
            temp = curr->next;
            //make the next node the previous one
            curr->next = prev; 
            //make the previous node the next
            prev = curr; 
            curr = temp;
        }
        return prev;
    }
};
