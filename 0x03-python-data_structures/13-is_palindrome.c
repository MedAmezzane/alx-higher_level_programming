#include <stddef.h>
#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome - Check if a singly linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 * Return: 1 if the list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head;
	int values[2048], i = 0, cLoop, limit;

	/*If the list is empty or has only one node, it's considered a palindrome.*/
	if (head == NULL || *head == NULL)
		return (1);

	/*Traverse the list and store its values in an array.*/
	while (tmp != NULL)
	{
		values[i] = tmp->n;
		i++;
		tmp = tmp->next;
	}

	/*Calculate the limit for comparison based on the list length.*/
	limit = (i % 2 == 0) ? i / 2 : (i + 1) / 2;

	/*Compare values from the start and end of the array.*/
	for (cLoop = 0; cLoop < limit; cLoop++)
	{
		if (values[cLoop] != values[i - 1 - cLoop])
			return (0);
	}

	/*If the loop completes, the list is a palindrome.*/
	return (1);
}

