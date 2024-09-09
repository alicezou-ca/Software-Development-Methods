/** @file route_manager.c
 *  @brief A small program to analyze airline routes data.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "list.h"
#include <yaml.h>
#include <ctype.h>

#define MAX_LINE_LEN 80

/**
 * Function: modify_arguements
 * --------------
 * @brief Modifies the arguments passed to the program by extracting the portion after '='.
 *
 * This function processes each argument in the list, finds the position of the '=' character,
 * and replaces the original argument with the portion of the argument that comes after '='.
 *
 * @param count The count of elements passed into CSV.
 * @param argv The list of arguments passed to the program.
 */
void modify_arguements(char count, char *argv[]) 
{
    
    for(int i= 1; i <=count; i++) 
    {
        // Find the position of the '=' character
        char *equal_sign = strchr(argv[i], '=');

        // If '=' is found, move the pointer to the character after '='
        if (equal_sign != NULL) 
        {
            equal_sign++;  // Move to the character after '='

            // Allocate memory for the new string
            char *array = (char *)malloc(sizeof(char) * (strlen(equal_sign) + 1));

            // Copy the content after '=' into the new array
            strcpy(array, equal_sign);

            // Replace the original data with the new array
            strcpy(argv[i], array);

            // Free the allocated memory
            free(array);
        }
    }
}

/**
 * Function: writeCSV
 * --------------
 * @brief Writes the content of a linked list to a CSV file.
 *
 * This function traverses a linked list and writes its content to a CSV file named "output.csv".
 * Each node in the linked list contains a word and its count, which are written as rows in the CSV file.
 * The function writes a maximum of `n` nodes to the file.
 *
 * @param head The head of the linked list to be written to the CSV file.
 * @param n The maximum number of nodes to write to the CSV file.
 */
void writeCSV(node_t *head, int n) 
{
    FILE *file;
    file = fopen("output.csv", "w");
    if (!file) 
    {
        perror("Failed to open file");
        exit(EXIT_FAILURE);
    }
    fprintf(file, "subject,statistic\n");
    for (int i = 0; i < n; i++) 
    {
        fprintf(file, "\"%s\",%d\n", head->word, head->count);
        head = head->next;
    }
}

/**
 * Function: formatString
 * --------------
 * @brief Removes all occurrences of the single quote character from a given string.
 *
 * This function iterates through the input string and removes all single quote characters ('').
 * It modifies the input string in place. Next, it takes this modified imput string and 
 * ensures there's no leading or ending whitespace.
 *
 * @param str The input string from which single quote characters will be removed.
 * @return char* A pointer to the modified string with single quote characters removed.
 */
char* formatString(char str[]) 
{
    int len = strlen(str);
    int j = 0;
    for (int i = 0; i < len; i++) 
    {
        if (str[i] != '\'') {
            str[j] = str[i];
            j++;
        }
    }
    str[j] = '\0';

    char *start = str;
    char *end;

    // Trim leading space
    while (isspace((unsigned char)*start)) start++;

    if (*start == 0) {  // All spaces
        return strdup("");
    }

    // Trim trailing space
    end = start + strlen(start) - 1;
    while (end > start && isspace((unsigned char)*end)) end--;

    // Set the new null terminator
    end[1] = '\0';

    return strdup(start);
}

/**
 * Function: caseOne
 * --------------
 * @brief Processes a YAML file and writes selected data to a CSV file.
 *
 * This function reads a YAML file containing airline route data, processes the data to extract
 * relevant information, and writes the selected information to a CSV file. The function gets the 
 * airlines that offer the greatest number of routes with destination country as Canada
 *
 * @param data The name of the input YAML file.
 * @param n The maximum number of entries to write to the CSV file.
 */
void caseOne(char data[], int n) 
{
    node_t *root = NULL;
    int count_ln = 0;
    FILE* file = fopen(data, "r");
    char line[MAX_LINE_LEN];
    char *airline_icao_unique_code = (char *)malloc(MAX_LINE_LEN * sizeof(char));
    char *airline_name = (char *)malloc(MAX_LINE_LEN * sizeof(char));
    char *dest_country = (char *)malloc(MAX_LINE_LEN * sizeof(char)); 

    //skip :route header
    fgets(line, MAX_LINE_LEN, file);

    while (fgets(line, MAX_LINE_LEN, file) != NULL) {
        line[strcspn(line, "\n")] = '\0';
        char *token = strtok(line, ":");
        char *tmp = (char *)malloc(sizeof(char) * strlen(token));
        if (count_ln%13 == 0) { 
            token = strtok(NULL, "");
            tmp = formatString(token);
            strcpy(airline_name, tmp);
        }
        else if (count_ln%13 == 1) {
            token = strtok(NULL, "");
            tmp = formatString(token);
            strcpy(airline_icao_unique_code, tmp);
        }
        else if (count_ln%13 == 10) {
            token = strtok(NULL, "");
            tmp = formatString(token);
            strcpy(dest_country, tmp);
            if (strcmp(dest_country, "Canada") == 0) {
                strcat(airline_name, " ("); 
                strcat(airline_icao_unique_code, ")");
                strcat(airline_name, airline_icao_unique_code);
                root = addValue(root, airline_name);

            }
        }
        free(tmp);
        count_ln ++;
    }
    free(dest_country);
    free(airline_name);
    free(airline_icao_unique_code);
    fclose(file);
    sort(&root);
    writeCSV(root, n);
}

/**
 * Function: caseTwo
 * --------------
 * @brief Processes a YAML file and writes selected data to a CSV file.
 *
 * This function reads a YAML file containing airline route data, processes the data to extract
 * relevant information, and writes the selected information to a CSV file. The function gets the
 * the top countries with least appearances as destination country on the routes data
 *
 * @param data The name of the input YAML file.
 * @param n The maximum number of entries to write to the CSV file.
 */
void caseTwo(char data[], int n) 
{
    node_t *root = NULL;
    int count_ln = 0;
    FILE* file = fopen(data, "r");
    char line[MAX_LINE_LEN];
    char *dest_country = (char *)malloc(MAX_LINE_LEN * sizeof(char));

    //skip :route header
    fgets(line, MAX_LINE_LEN, file);

    while (fgets(line, MAX_LINE_LEN, file) != NULL) 
    {
        line[strcspn(line, "\n")] = '\0';
        char *token = strtok(line, ":");
        char *tmp = (char *)malloc(sizeof(char) * strlen(token));
        if (count_ln%13 == 10) 
        {
            token = strtok(NULL, "");
            tmp = formatString(token);
            strcpy(dest_country, tmp);
            root = addValue(root, dest_country);
        }
        count_ln ++;
        free(tmp);
    }
    node_t *head = root;
    root = head;

    free(dest_country);
    fclose(file);
    while (root != NULL) //flip to negative value to sort descending
    {
        root->count *= -1;
        root = root->next;
    }
    root = head;
    sort(&root);
    head = root;
    while (root != NULL) 
    {
        root->count *= -1;
        root = root->next;
    }
    root = head;
    writeCSV(root, n);
}

/**
 * Function: caseThree
 * --------------
 * @brief Processes a YAML file and writes selected data to a CSV file.
 *
 * This function reads a YAML file containing airline route data, processes the data to extract
 * relevant information, and writes the selected information to a CSV file. The function gets the
 * top destination airports.
 *
 * @param data The name of the input YAML file.
 * @param n The maximum number of entries to write to the CSV file.
 */
void caseThree(char data[], int n) 
{
    node_t *root = NULL;
    int count_ln = 0;
    FILE* file = fopen(data, "r");
    char *to_airport_country = (char *)malloc(MAX_LINE_LEN * sizeof(char));
    char line[MAX_LINE_LEN];
    char *to_airport_name = (char *)malloc(MAX_LINE_LEN * sizeof(char));
    char *to_airport_city = (char *)malloc(MAX_LINE_LEN * sizeof(char));
    char *to_airport_icao_unique_code = (char *)malloc(MAX_LINE_LEN * sizeof(char));

    //skip :route header
    fgets(line, MAX_LINE_LEN, file);

    while (fgets(line, MAX_LINE_LEN, file) != NULL) 
    {
        line[strcspn(line, "\n")] = '\0';
        char *token = strtok(line, ":");
        char *tmp = (char *)malloc(strlen(token) * sizeof(char));
        if (count_ln%13 == 8) 
        {
            token = strtok(NULL, "");
            tmp = formatString(token);
            strcpy(to_airport_name, tmp);
        }
        else if (count_ln%13 == 9) 
        {
            token = strtok(NULL, "");
            tmp = formatString(token);
            strcpy(to_airport_city, tmp);
        }
        else if (count_ln%13 == 10) 
        {
            token = strtok(NULL, "");
            tmp = formatString(token);
            strcpy(to_airport_country, tmp);
        }
        else if (count_ln%13 == 11) 
        {
            token = strtok(NULL, "");
            tmp = formatString(token);
            strcpy(to_airport_icao_unique_code, tmp);
            strcat(to_airport_name, " (");
            strcat(to_airport_name, to_airport_icao_unique_code);
            strcat(to_airport_name, "), ");
            strcat(to_airport_name, to_airport_city);
            strcat(to_airport_name, ", ");
            strcat(to_airport_name, to_airport_country);
            root = addValue(root, to_airport_name);
        }
        count_ln ++;
    }
    free(to_airport_name);
    free(to_airport_city);
    free(to_airport_icao_unique_code);
    free(to_airport_country);
    fclose(file);
    sort(&root);
    writeCSV(root, n);
}

/**
 * Function: caseOne
 * --------------
 * @brief Processes a YAML file and writes selected data to a CSV file.
 *
 * This function 
 *
 * @param *argv The arguements from CLI
 */
void solve(char *argv[]) {
    if (strcmp(argv[2], "1") == 0) 
    {
        caseOne(argv[1], atoi(argv[3]));
    } 
    else if (strcmp(argv[2], "2") == 0) 
    {
        caseTwo(argv[1], atoi(argv[3]));
    } 
    else if (strcmp(argv[2], "3") == 0) 
    {
        caseThree(argv[1], atoi(argv[3]));
    }
}

/**
 * @brief The main function and entry point of the program.
 *
 * @param argc The number of arguments passed to the program.
 * @param argv The list of arguments passed to the program.
 * @return int 0: No errors; 1: Errors produced.
 *
 */
int main(int argc, char *argv[]) 
{
    //edit strings to be just data
    modify_arguements((argc-1), argv);
    solve(argv);
    exit(0);
}