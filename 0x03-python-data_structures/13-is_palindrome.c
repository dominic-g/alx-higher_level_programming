#include <stdlib.h>
#include <stdio.h>
#include "lists.h"


/**
  * list_len -This Counts the number of elements in a linked list
  *
  * @sm_list: The linked list to count
  *
  * Return: Number of elements in the linked list
  */
size_t list_len(const listint_t *linked_list)
{
	int len = 0;

	while (linked_list != NULL)
	{
		++len;
		linked_list = linked_list->next;
	}

	return (len);
}

/**
  * get_nodeint_at_index - Gets a node from a linked list
  *
  * @head: The head of the linked list
  * @index: The index to find in the linked list
  *
  * Return: The specific node of the linked list
  */
listint_t *get_nodeint_at_index(listint_t *head, unsigned int index)
{
	listint_t *sm_curr = head;
	unsigned int iterator = 0;

	if (head)
	{
		while (sm_curr != NULL)
		{
			if (iterator == index)
				return (sm_curr);

			sm_curr = sm_curr->next;
			++iterator;
		}
	}

	return (NULL);
}



/**
  * is_palindrome - Checks if a given singly linked list is a palindrome
  *
  * @head: The head of the singly linked list
  *
  * Return: 0 if it is not a palindrome, 1 if it is a palindrome
  */
int is_palindrome(listint_t **head)
{
	listint_t *start = NULL, *end = NULL;
	unsigned int i = 0, len = 0, sm_len = 0, sm_lol = 0;

	if (head == NULL)
		return (0);

	if (*head == NULL)
		return (1);

	start = *head;
	len = list_len(start);
	sm_len = len * 2;
	sm_lol = sm_len - 2;
	end = *head;

	for (; i < sm_len; i = i + 2)
	{
		if (start[i].n != end[sm_lol].n)
			return (0);

		sm_lol = sm_lol - 2;
	}

	return (1);
}
