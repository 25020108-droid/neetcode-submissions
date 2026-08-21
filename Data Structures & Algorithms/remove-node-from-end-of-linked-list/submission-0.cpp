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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* temp = head;
        int length = 1;
        while (temp->next != nullptr) {
            length++;
            temp = temp->next;
        }
        int node = length - n + 1;
        if (node == 1) {
            return head->next;
        }
        temp = head;
        for (int i = 0; i < node - 2; ++i) {
            temp = temp->next;
        }
        temp->next = temp->next->next;
        return head;
    }
};
