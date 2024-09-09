/** @file list.c
 *  @brief Implementation of a linked list.
 *
 * Based on the implementation approach described in "The Practice
 * of Programming" by Kernighan and Pike (Addison-Wesley, 1999).
 *
 */
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "emalloc.h"
#include "list.h"

/**
 * Function:  new_node
 * -------------------
 * @brief  Allows to dynamically allocate memory for a new node to be added to the linked list.
 *
 * This function should confirm that the argument being passed is not NULL (i.e., using the assert library). Then,
 * It dynamically allocates memory for the new node using emalloc(), and assign values to attributes associated with the node (i.e., val and next).
 *
 * @param val The value to be associated with the node.
 *
 * @return node_t* A pointer to the node created.
 *
 */
node_t *new_node(char *val)
{   
    assert(val != NULL);

    node_t *temp = (node_t *)emalloc(sizeof(node_t));

    temp->word = strdup(val);
    temp->next = NULL;
    temp->count = 1; //since at least one has been added

    return temp;
}


/**
 * Function:  add_front
 * --------------------
 * @brief  Allows to add a node at the front of the list.
 *
 * @param list The list where the node will be added (i.e., a pointer to the first element in the list).
 * @param new The node to be added to the list.
 *
 * @return node_t* A pointer to the new head of the list.
 *
 */
node_t *add_front(node_t *list, node_t *new)
{
    new->next = list;
    return new;
}

/**
 * Function:  add_end
 * ------------------
 * @brief  Allows to add a node at the end of the list.
 *
 * @param list The list where the node will be added (i.e., a pointer to the first element in the list).
 * @param new The node to be added to the list.
 *
 * @return node_t* A pointer to the head of the list.
 *
 */
node_t *add_end(node_t *list, node_t *new)
{
    node_t *curr;

    if (list == NULL)
    {
        new->next = NULL;
        return new;
    }

    for (curr = list; curr->next != NULL; curr = curr->next)
        ;
    curr->next = new;
    new->next = NULL;
    return list;
}

/**
 * Function:  add_inorder
 * ----------------------
 * @brief  Allows to add a new node to the list respecting an order.
 *
 * @param list The list where the node will be added (i.e., a pointer to the first element in the list).
 * @param new The node to be added to the list.
 * Note: This function is not used in the implementation of route manager
 *
 * @return node_t* A pointer to the node created.
 *
 */
node_t *add_inorder(node_t *list, node_t *new)
{
    node_t *prev = NULL;
    node_t *curr = NULL;

    if (list == NULL)
    {
        return new;
    }

    for (curr = list; curr != NULL; curr = curr->next)
    {
        if (new->count < curr->count) //if (strcmp(new->word, curr->word) > 0), if new > word its more than 0
        {
            prev = curr;
        }
        else if (new->count == curr->count)
        {
            //implement sorting by alphabet
            // prev = curr;
        }
        else
        {
            break;
        }
    }

    new->next = curr;

    if (prev == NULL)
    {
        return (new);
    }
    else
    {
        prev->next = new;
        return list;
    }
}

/**
 * Function: addValue
 * ------------------
 * @brief Adds a value to a linked list or increments the count if the value already exists.
 *
 * This function traverses a linked list to find if a given value already exists in the list.
 * If the value is found, it increments the count of the corresponding node.
 * If the value is not found, it creates a new node with the given value and adds it to the end of the list.
 *
 * @param root The head of the linked list.
 * @param val The value to add to the linked list.
 * @return node_t* The head of the updated linked list.
 */
node_t *addValue(node_t *root, char val[]) 
{
    if (root == NULL) 
    {
        return new_node(val);
    }

    node_t *temp_root = root;
    while (root != NULL) 
    {
        if (strcmp(root->word, val) == 0) 
        {
            root->count++;
            return temp_root;
        }
        root = root->next;
    }

    node_t *tmp = new_node(val);
    temp_root = add_end(temp_root, tmp);
    return temp_root;
}


/**
 * Function:  peek_front
 * ---------------------
 * @brief  Allows to get the head node of the list.
 *
 * @param list The list to get the node from.
 *
 * @return node_t* A pointer to the head of the list.
 *
 */
node_t *peek_front(node_t *list)
{
    return list;
}

/**
 * Function:  remove_front
 * -----------------------
 * @brief  Allows removing the head node of the list.
 *
 * @param list The list to remove the node from.
 *
 * @return node_t* A pointer to the head of the list.
 *
 */
node_t *remove_front(node_t **list) {
    if (*list == NULL) {
        return NULL;
    }

    node_t *removed_node = *list;
    *list = (*list)->next;
    removed_node->next = NULL; // Isolate the removed node
    return removed_node;

    //deallocate the memory 
}

/**
 * Function: apply
 * --------------
 * @brief  Allows to apply a function to the list.
 *
 * Note: This function is not used in the implementation of route manager
 * @param list The list (i.e., pointer to head node) where the function will be applied.
 * @param fn The pointer of the function to be applied.
 * @param arg The arguments to be applied.
 *
 */
void apply(node_t *list,
           void (*fn)(node_t *list, void *),
           void *arg)
{
    for (; list != NULL; list = list->next)
    {
        (*fn)(list, arg);
    }
}

/**
 * Function: compare
 * -----------------
 * @brief Compares two nodes based on their count and word.
 *
 * This function compares two nodes of a linked list. It first compares the count of each node.
 * Then, if the counts are tied, it compares the name of each node.
 * It then returns 0, negative value, postive value according to the result.
 *
 * @param nodeOne The first node to compare.
 * @param nodeTwo The second node to compare.
 * @return int A comparison result indicating the order of the two nodes.
 */
int compare(node_t *nodeOne, node_t *nodeTwo) {
    if (nodeOne->count > nodeTwo->count)
    {
        return -1;
    }
    else if (nodeOne->count < nodeTwo->count) 
    {
         return 1;
    }
    else //0 if equal, negative if first strong < second string, pos if first > second
    {
        return strcmp(nodeOne->word, nodeTwo->word);
    }
}

/**
 * Function: sort
 * --------------
 * @brief Sorts a linked list in ascending order based on a comparison function.
 *
 * This function takes a pointer to the head of a linked list and sorts the list in ascending order.
 * The sorting is performed using insertion sort. The comparison function `compare` is used to
 * determine the order of the elements.
 *
 * @param list A pointer to the head of the linked list to be sorted.
 */
void sort(node_t **list) {
    node_t *sorted = NULL;
    node_t *head = *list;

    while (head != NULL) 
    {
        node_t *current = head;
        head = head->next;

        if (sorted == NULL || compare(current, sorted) < 0) 
        {
            current->next = sorted;
            sorted = current;
        }
        else 
        {
            node_t *temp = sorted;
            while (temp->next != NULL && compare(current, temp->next) >= 0) {
                temp = temp->next;
            }
            current->next = temp->next;
            temp->next = current;
        }
    }
    *list = sorted;
}