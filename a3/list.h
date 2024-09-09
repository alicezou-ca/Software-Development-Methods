/** @file listy.h
 *  @brief Function prototypes for the linked list.
 */
#ifndef _LINKEDLIST_H_
#define _LINKEDLIST_H_

#define MAX_WORD_LEN 50

/**
 * @brief An struct that represents a node in the linked list.
 */
typedef struct node_t
{
    char *word;
    int count;
    struct node_t *next;
} node_t;

/**
 * Function protypes associated with a linked list.
 */
node_t *new_node(char *val);
node_t *add_front(node_t *, node_t *);
node_t *add_end(node_t *, node_t *);
node_t *add_inorder(node_t *, node_t *);
node_t *peek_front(node_t *);
node_t *addValue(node_t *head, char info[]);
node_t *remove_front(node_t **list);
void apply(node_t *, void (*fn)(node_t *, void *), void *arg);
int compare(node_t *route1, node_t *route2);
void sort(node_t **list);

#endif
