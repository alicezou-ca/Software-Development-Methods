/** @file route_manager.c
 *  @brief A pipes & filters program that uses conditionals, loops, and string processing tools in C to process airline routes.
 */
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_ARG 10 //max number of results possible
#define MAX_FIELD_LENGTH 1024

typedef struct {

    char airline_name[MAX_FIELD_LENGTH];
    char airline_icao_unique_code[MAX_FIELD_LENGTH];
    char airline_country[MAX_FIELD_LENGTH];
    char from_airport_name[MAX_FIELD_LENGTH];
    char from_airport_city[MAX_FIELD_LENGTH];
    char from_airport_country[MAX_FIELD_LENGTH];
    char from_airport_icao_unique_code[MAX_FIELD_LENGTH];
    char to_airport_name[MAX_FIELD_LENGTH];
    char to_airport_city[MAX_FIELD_LENGTH];
    char to_airport_country[MAX_FIELD_LENGTH];
    char to_airport_icao_unique_code[MAX_FIELD_LENGTH];

} FlightInfo;

typedef struct {

    char airline_name[MAX_FIELD_LENGTH];
    char airline_icao_unique_code[MAX_FIELD_LENGTH];
    char airline_country[MAX_FIELD_LENGTH];
    char from_airport_name[MAX_FIELD_LENGTH];
    char from_airport_city[MAX_FIELD_LENGTH];
    char from_airport_country[MAX_FIELD_LENGTH];
    char from_airport_icao_unique_code[MAX_FIELD_LENGTH];
    char to_airport_name[MAX_FIELD_LENGTH], to_airport_city[MAX_FIELD_LENGTH];
    char to_airport_country[MAX_FIELD_LENGTH];
    char to_airport_icao_unique_code[MAX_FIELD_LENGTH];

} MatchingFlights[MAX_ARG];

// Function prototype
void modify_arguments(int argc, char *argv[]);
void useCaseOne(char airline_icao_unique_code[MAX_FIELD_LENGTH], char to_airport_country[MAX_FIELD_LENGTH]);
void useCaseTwo(char from_airport_country[MAX_FIELD_LENGTH], char to_airport_city[MAX_FIELD_LENGTH], char to_airport_country[MAX_FIELD_LENGTH]);
void useCaseThree(char from_airport_city[MAX_FIELD_LENGTH], char from_airport_country[MAX_FIELD_LENGTH], char to_airport_city[MAX_FIELD_LENGTH], char to_airport_country[MAX_FIELD_LENGTH]);
void parseSingleLine(char buffer[MAX_FIELD_LENGTH], FlightInfo *flights);




/**
 * Function: main
 * --------------
 * @brief The main function and entry point of the program.
 *
 * @param argc The number of arguments passed to the program.
 * @param argv The list of arguments passed to the program.
 * @return int 0: No errors; 1: Errors produced.
 *
 */
int main(int argc, char *argv[]) {

    modify_arguments(argc, argv);

    //check which use case current program call is, and assign variable accordingly
    if (argc == 4) { //use case 1
        useCaseOne(argv[2], argv[3]);
    } else if (argc==5) { //use case 2
        useCaseTwo(argv[2], argv[3], argv[4]);
    } else { //use case 3
        useCaseThree(argv[2], argv[3], argv[4], argv[5]);
    }

    exit(0);
}


void useCaseOne(char airline_icao_unique_code[MAX_FIELD_LENGTH], char to_airport_country[MAX_FIELD_LENGTH]) {

    FILE *file = fopen("output.txt", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        exit(1);
    }

    FILE *CSVfile = fopen("airline-routes-data.csv", "r");
    if (!CSVfile) {
        printf("Error opening file");
        exit(1);
    }

    char buffer[1024];  // Buffer to hold each line
    int result = 0;
    FlightInfo flights;
    MatchingFlights matchingFlights;
    char airline_name[MAX_FIELD_LENGTH];


    // Skip the header line
    fgets(buffer, sizeof(buffer), CSVfile);

    // Read each line and parse the data
    while (fgets(buffer, sizeof(buffer), CSVfile) != NULL) { 
        parseSingleLine(buffer, &flights);
        if(strcmp(airline_icao_unique_code, flights.airline_icao_unique_code)==0 && strcmp(to_airport_country, flights.to_airport_country)==0) {
            result++;
            strcpy(airline_name, flights.airline_name);
            strcpy(matchingFlights[result].from_airport_icao_unique_code, flights.from_airport_icao_unique_code);
            strcpy(matchingFlights[result].from_airport_city, flights.from_airport_city);
            strcpy(matchingFlights[result].from_airport_country, flights.from_airport_country);
            strcpy(matchingFlights[result].to_airport_name, flights.to_airport_name);
            strcpy(matchingFlights[result].to_airport_icao_unique_code, flights.to_airport_icao_unique_code);
            strcpy(matchingFlights[result].to_airport_city, flights.to_airport_city);
        }
    }

    //prints results to file
    if(result == 0) fprintf(file, "NO RESULTS FOUND.\n");
    else {
        fprintf(file, "FLIGHTS TO %s BY %s (%s):\n", to_airport_country, airline_name, airline_icao_unique_code);
        for(int i=1; i<=result; i++) {
            fprintf(file, "FROM: %s, %s, %s TO: %s (%s), %s\n", 
                matchingFlights[i].from_airport_icao_unique_code, 
                matchingFlights[i].from_airport_city, 
                matchingFlights[i].from_airport_country, 
                matchingFlights[i].to_airport_name, 
                matchingFlights[i].to_airport_icao_unique_code, 
                matchingFlights[i].to_airport_city);
        }
    }

    fclose(CSVfile);
    fclose(file);
}


void useCaseTwo(char from_airport_country[MAX_FIELD_LENGTH], char to_airport_city[MAX_FIELD_LENGTH], char to_airport_country[MAX_FIELD_LENGTH]) {


    FILE *file = fopen("output.txt", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        exit(1);
    }

    FILE *CSVfile = fopen("airline-routes-data.csv", "r");
    if (!CSVfile) {
        printf("Error opening file");
        exit(1);
    }


    char buffer[1024];  // Buffer to hold each line
    int result = 0;
    FlightInfo flights;
    MatchingFlights matchingFlights;
    char airline_name[MAX_FIELD_LENGTH];


    // Skip the header line
    fgets(buffer, sizeof(buffer), CSVfile);

    // Read each line and parse the data
    while (fgets(buffer, sizeof(buffer), CSVfile) != NULL) { 
        parseSingleLine(buffer, &flights);
        if(strcmp(from_airport_country, flights.from_airport_country)==0 && strcmp(to_airport_city, flights.to_airport_city)==0 && strcmp(to_airport_country, flights.to_airport_country)==0) {
            result++;
            strcpy(matchingFlights[result].airline_name, flights.airline_name);
            strcpy(matchingFlights[result].airline_icao_unique_code, flights.airline_icao_unique_code);
            strcpy(matchingFlights[result].from_airport_name, flights.from_airport_name);
            strcpy(matchingFlights[result].from_airport_icao_unique_code, flights.from_airport_icao_unique_code);
            strcpy(matchingFlights[result].from_airport_city, flights.from_airport_city);
        }
    }

    //prints results to file
    if(result == 0) fprintf(file, "NO RESULTS FOUND.\n");
    else {
        fprintf(file, "FLIGHTS FROM %s TO %s, %s:\n", from_airport_country, to_airport_city, to_airport_country); //FIX LATER
        for(int i=1; i<=result; i++) {
            fprintf(file, "AIRLINE: %s (%s) ORIGIN: %s (%s), %s\n", 
                matchingFlights[i].airline_name, 
                matchingFlights[i].airline_icao_unique_code, 
                matchingFlights[i].from_airport_name, 
                matchingFlights[i].from_airport_icao_unique_code, 
                matchingFlights[i].from_airport_city);
        }
    }


    fclose(CSVfile);
    fclose(file);
}


void useCaseThree(char from_airport_city[MAX_FIELD_LENGTH], char from_airport_country[MAX_FIELD_LENGTH], char to_airport_city[MAX_FIELD_LENGTH], char to_airport_country[MAX_FIELD_LENGTH]) {


    FILE *file = fopen("output.txt", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        exit(1);
    }

    FILE *CSVfile = fopen("airline-routes-data.csv", "r");
    if (!CSVfile) {
        printf("Error opening file");
        exit(1);
    }

    char buffer[1024];  // Buffer to hold each line
    int result = 0;
    FlightInfo flights;
    MatchingFlights matchingFlights;
    char airline_name[MAX_FIELD_LENGTH];


    // Skip the header line
    fgets(buffer, sizeof(buffer), CSVfile);


    // Read each line and parse the data
    while (fgets(buffer, sizeof(buffer), CSVfile) != NULL) { 
        parseSingleLine(buffer, &flights);
        if(strcmp(from_airport_city, flights.from_airport_city) == 0 && strcmp(from_airport_country, flights.from_airport_country) == 0 && strcmp(to_airport_city, flights.to_airport_city) == 0 && strcmp(to_airport_country, flights.to_airport_country) == 0) {
            result++;
            strcpy(matchingFlights[result].airline_name, flights.airline_name);
            strcpy(matchingFlights[result].airline_icao_unique_code, flights.airline_icao_unique_code);
            strcpy(matchingFlights[result].from_airport_icao_unique_code, flights.from_airport_icao_unique_code);
            strcpy(matchingFlights[result].to_airport_icao_unique_code, flights.to_airport_icao_unique_code);
        }
    }

    //prints results to file
    if(result == 0) fprintf(file, "NO RESULTS FOUND.\n");
    else {
        fprintf(file, "FLIGHTS FROM %s, %s TO %s, %s:\n", from_airport_city, from_airport_country, to_airport_city, to_airport_country); //FIX LATER
        for(int i=1; i<=result; i++) {
            fprintf(file, "AIRLINE: %s (%s) ROUTE: %s-%s\n", 
                matchingFlights[i].airline_name, 
                matchingFlights[i].airline_icao_unique_code, 
                matchingFlights[i].from_airport_icao_unique_code, 
                matchingFlights[i].to_airport_icao_unique_code);
        }
    }


    fclose(CSVfile);
    fclose(file);
}


void parseSingleLine(char buffer[MAX_FIELD_LENGTH], FlightInfo *flights) {

        //using strtok to sort each comma separated string into its place
        char *token = strtok(buffer, ",");
         if (token != NULL) strcpy(flights->airline_name, token);

        token = strtok(NULL, ",");
         if (token != NULL) strcpy(flights->airline_icao_unique_code, token);

        token = strtok(NULL, ",");
        if (token != NULL) strcpy(flights->airline_country, token);

        token = strtok(NULL, ",");
        if (token != NULL) strcpy(flights->from_airport_name, token);

        token = strtok(NULL, ",");
        if (token != NULL) strcpy(flights->from_airport_city, token);

        token = strtok(NULL, ",");
        if (token != NULL) strcpy(flights->from_airport_country, token);

        token = strtok(NULL, ",");
        if (token != NULL) strcpy(flights->from_airport_icao_unique_code, token);

        token = strtok(NULL, ","); //to get rid of altitude

        token = strtok(NULL, ",");
        if (token != NULL) strcpy(flights->to_airport_name, token);

        token = strtok(NULL, ",");
        if (token != NULL) strcpy(flights->to_airport_city, token);

        token = strtok(NULL, ",");
        if (token != NULL) strcpy(flights->to_airport_country, token);

        token = strtok(NULL, ",");
        if (token != NULL) strcpy(flights->to_airport_icao_unique_code, token);


}


void modify_arguments(int argc, char *argv[]) {
    //only take the arguement after the = from the command line
    for (int i = 1; i < argc; i++) {
        char *arg = argv[i];
        char *equal_sign = strchr(arg, '=');

        if (equal_sign != NULL) {
            argv[i] = equal_sign + 1;
        }
    }
}
