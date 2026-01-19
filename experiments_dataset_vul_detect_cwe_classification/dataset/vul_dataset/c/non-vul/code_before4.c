// From cwe-snippets, ./snippets_1/compliant/C/0172.c

int size(struct node* head) {
    struct node* current = head;
                      int count = 0;
                      while (current != NULL) {
        count++;
                           current = current->next;
    }
                      return count;
}