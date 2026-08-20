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
#include <unordered_set>

class Solution {
public:
    bool hasCycle(ListNode* head) {
        std::unordered_set<ListNode*> visited;
        ListNode* curr = head;
        while (curr != nullptr) {
            if (visited.count(curr) > 0) {
                return true;
            }
            visited.insert(curr);
            curr = curr->next;
        }
        return false;
    }
};
