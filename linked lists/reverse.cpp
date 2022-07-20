struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
    public:
        ListNode* reverse(ListNode* head) {
            if (head == nullptr || head->next == nullptr) {
                return head;
            }
            ListNode* prev = nullptr;
            ListNode* cur = head;
            
            while (cur != nullptr) {
                ListNode* tmp = cur->next;
                cur->next = prev;
                prev = cur;
                cur = tmp;
            }

            return prev;
        }
};
