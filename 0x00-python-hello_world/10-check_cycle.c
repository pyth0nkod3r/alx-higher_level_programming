#include "lists.h"

/**
 * check_cycle - Checks if there's a cycle in the linked list or not
 * @list: List to be checked
 *
 * Return: 0 if there's no cycle, 1 otherwise.
 */

int check_cycle(listint_t *list)
{
	listint_t *current_node, *next_node;

	current_node = list;
	next_node = list->next;

	while (current_node != NULL && next_node != NULL && next_node->next)
	{
		if (current_node == next_node)
		{
			return (1);
		}
		current_node = current_node->next;
		next_node = next_node->next->next;
	}
	return (0);
}
