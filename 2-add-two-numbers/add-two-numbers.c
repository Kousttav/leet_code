struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {

    struct ListNode* start1 = l1;
    struct ListNode* start2 = l2;

    struct ListNode* head = NULL;
    struct ListNode* tail = NULL;

    int carry = 0;

    while (start1 != NULL || start2 != NULL) {

        int sum = carry;

        if (start1 != NULL) {
            sum += start1->val;
            start1 = start1->next;
        }

        if (start2 != NULL) {
            sum += start2->val;
            start2 = start2->next;
        }

        struct ListNode* nw = (struct ListNode*)malloc(sizeof(struct ListNode));
        nw->val = sum % 10;
        nw->next = NULL;

        carry = sum / 10;

        if (head == NULL) {
            head = nw;
            tail = nw;
        } else {
            tail->next = nw;
            tail = nw;
        }
    }

    if (carry) {
        struct ListNode* nw = (struct ListNode*)malloc(sizeof(struct ListNode));
        nw->val = carry;
        nw->next = NULL;
        tail->next = nw;
    }

    return head;
}
