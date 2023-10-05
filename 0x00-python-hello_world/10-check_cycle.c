#include "lists.h"
/**
 * check_cycle - function detect if a linked list contains a cycle.
 * @list: pointer to the beginning of the node
 * Return: 0 if no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
    listint_t *current, *check;

    /*If the list is empty or has only one node, there can be no cycle.*/
    if (list == NULL || list->next == NULL)
        return (0);

    /*Initialize two pointers, 'current' and 'check'.*/
    current = list;
    check = current->next;

    /*Iterate through the list with two pointers.*/
    while (current != NULL && check->next != NULL && check->next->next != NULL)
    {
        /*If 'current' and 'check' meet at the same node, a cycle is detected.*/
        if (current == check)
            return (1);

        /*Move 'current' one step at a time and 'check' two steps at a time.*/
        current = current->next;
        check = check->next->next;
    }

    /*If the loop terminates without a cycle, return 0 (no cycle found).*/
    return (0);
}
