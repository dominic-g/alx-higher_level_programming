#include <stdlib.h>
#include <stdio.h>
#include "lists.h"


/**
  * list_len -This Counts the number of elements in a linked list
  *
  * @_list: The linked list to count
  *
  * Return: Number of elements in the linked list
  */
size_t list_len(const listint_t *_list)
{
	int len = 0;

	while (_list != NULL)
	{
		++len;
		_list = _list->next;
	}

	return (len);
}

/**
  * is_palindrome - Checks if a given singly linked list is a palindrome
  *
  * @first: The head of the singly linked list
  *
  * Return: 0 if it is not a palindrome, 1 if it is a palindrome
  */
int is_palindrome(listint_t **first)
{
	listint_t *first = NULL, *last = NULL;
	unsigned int i = 0, len = 0, _len = 0, lol = 0;

	if (first == NULL)
		return (0);

	if (*first == NULL)
		return (1);

	start = *first;
	len = list_len(start);
	_len = len * 2;
	lol = _len - 2;
	last = *first;

	for (; k < _len; k = k + 2)
	{
		if (start[k].n != last[lol].n)
			return (0);

		lol = lol - 2;
	}

	return (1);
}
