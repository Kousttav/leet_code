/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head) {
    struct ListNode *start = head, *temp;

    while (start != NULL && start->next != NULL) {
        if (start->val == start->next->val) {
            temp = start->next;
            start->next = start->next->next;
            free(temp);
        } else {
            start = start->next;
        }
    }
    return head;
}