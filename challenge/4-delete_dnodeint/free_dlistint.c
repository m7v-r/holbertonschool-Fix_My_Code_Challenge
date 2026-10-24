#include <string.h>
#include <stdlib.h>
#include "lists.h"

/**
 * free_dlistint - Free a list
 * @head: Address of the first element of the list
 */
void free_dlistint(dlistint_t *head)
{
	dlistint_t *p;

	while (head)
	{
		p = head;
		head = head->next;
		free(p);
	}
}
