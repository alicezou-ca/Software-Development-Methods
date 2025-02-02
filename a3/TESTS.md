# Tests for `SENG 265`, Assignment #3

## Requirements

* Pre-requisites
    * Configuration of required libraries (executed only once after connecting to Ref. Plat.): `setSENG265`
    * Compilation: `make` 
    * Enable the execution of tester: `chmod u+x tester`

## Tests

* Test 1
    * Input file: `routes-airlines-airports.yaml`
    * Inputs (arguments): `--DATA="routes-airlines-airports.yaml" --QUESTION=1 --N=10`
    * Expected output: `tests/test01.csv`
    * Test Command: `./tester 1`
    * Execution command run by `tester`:
      * `./route_manager --DATA="routes-airlines-airports.yaml" --QUESTION=1 --N=10`

* Test 2
    * Input file: `routes-airlines-airports.yaml`
    * Inputs (arguments): `--DATA="routes-airlines-airports.yaml" --QUESTION=1 --N=15`
    * Expected output: `tests/test02.csv`
    * Test Command: `./tester 2`
    * Execution command run by `tester`:
      * `./route_manager --DATA="routes-airlines-airports.yaml" --QUESTION=1 --N=15`

* Test 3
    * Input file: `routes-airlines-airports.yaml`
    * Inputs (arguments): `--DATA="routes-airlines-airports.yaml" --QUESTION=2 --N=15`
    * Expected output: `tests/test03.csv`
    * Test Command: `./tester 3`
    * Execution command run by `tester`:
      * `./route_manager --DATA="routes-airlines-airports.yaml" --QUESTION=2 --N=15`

* Test 4
    * Input file: `routes-airlines-airports.yaml`
    * Inputs (arguments): `--DATA="routes-airlines-airports.yaml" --QUESTION=2 --N=40`
    * Expected output: `tests/test04.csv`
    * Test Command: `./tester 4`
    * Execution command run by `tester`:
      * `./route_manager --DATA="routes-airlines-airports.yaml" --QUESTION=2 --N=40`

* Test 5
    * Input file: `routes-airlines-airports.yaml`
    * Inputs (arguments): `--DATA="routes-airlines-airports.yaml" --QUESTION=3 --N=5`
    * Expected output: `tests/test05.csv`
    * Test Command: `./tester 5`
    * Execution command run by `tester`:
      * `./route_manager --DATA="routes-airlines-airports.yaml" --QUESTION=3 --N=5`
