/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool isPalindrome(struct ListNode* head) {
    struct ListNode* rev = NULL;
    struct ListNode* temp = head;

    while (temp != NULL) {
        struct ListNode* node =
            (struct ListNode*)malloc(sizeof(struct ListNode));

        node->val = temp->val;
        node->next = rev;
        rev = node;

        temp = temp->next;
    }

    temp = head;
    while (temp != NULL) {
        if (temp->val != rev->val)
            return false;

        temp = temp->next;
        rev = rev->next;
    }

    return true;
}