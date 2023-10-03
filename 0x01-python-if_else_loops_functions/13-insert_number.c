#include "lists.h"
/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 *
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 *
 * Return: If the function fails - NULL.
 *         Otherwise - a pointer to the new node.
 * Author - Med.AMEZZANE
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number; /*Set the value of the new node to the given number.*/

	if (node == NULL || node->n >= number)
	{
		/*If the list is empty or the new node should be inserted at the beginning*/
		new->next = node;/*Set the next pointer of the new node to the current head*/
		*head = new; /*Update the head pointer to the new node.*/
		return (new); /*Return the new node.*/
	}

	while (node && node->next && node->next->n < number)
		node = node->next; /*Traverse the list to find the correct position.*/

	new->next = node->next; /*Insert the new node by updating next pointers.*/
	node->next = new;

	return (new); /*Return the new node.*/
}
