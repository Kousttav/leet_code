1/**
2 * Definition for singly-linked list.
3 * struct ListNode {
4 *     int val;
5 *     struct ListNode *next;
6 * };
7 */
8bool isPalindrome(struct ListNode* head) {
9    struct ListNode* rev = NULL;
10    struct ListNode* temp = head;
11
12    while (temp != NULL) {
13        struct ListNode* node =
14            (struct ListNode*)malloc(sizeof(struct ListNode));
15
16        node->val = temp->val;
17        node->next = rev;
18        rev = node;
19
20        temp = temp->next;
21    }
22
23    temp = head;
24    while (temp != NULL) {
25        if (temp->val != rev->val)
26            return false;
27
28        temp = temp->next;
29        rev = rev->next;
30    }
31
32    return true;
33}