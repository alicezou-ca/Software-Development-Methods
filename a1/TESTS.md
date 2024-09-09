# Tests for `SENG 265`, Assignment #1

* Pre-requisites
    * Configuration of required libraries (executed only once after connecting to Ref. Plat.): `setSENG265`
    * Compilation: `gcc route_manager.c -std=c99 -o route_manager` 
    * Enable the execution of tester: `chmod u+x tester`

* Test 1
    * Input: `airline-routes-data.csv`
    * Expected output: `test01.txt`
    * Test: `./tester 1`
    * Command automated by tester: `./route_manager --DATA="airline-routes-data.csv" --AIRLINE="SWR" --DEST_COUNTRY="Argentina"`


* Test 2
    * Input: `airline-routes-data.csv`
    * Expected output: `test02.txt`
    * Test: `./tester 2`
    * Command automated by tester: `./route_manager --DATA="airline-routes-data.csv" --AIRLINE="ETH" --DEST_COUNTRY="Egypt"`

* Test 3
    * Input: `airline-routes-data.csv`
    * Expected output: `test03.txt`
    * Test: `./tester 3`
    * Command automated by tester: `./route_manager --DATA="airline-routes-data.csv" --AIRLINE="ACA" --DEST_COUNTRY="Bahamas"`

* Test 4
    * Input: `airline-routes-data.csv`
    * Expected output: `test04.txt`
    * Test: `./tester 4`
    * Command automated by tester: `./route_manager --DATA="airline-routes-data.csv" --SRC_COUNTRY="Australia" --DEST_CITY="Zurich" --DEST_COUNTRY="Switzerland"`

* Test 5
    * Input: `airline-routes-data.csv`
    * Expected output: `test05.txt`
    * Test: `./tester 5`
    * Command automated by tester: `./route_manager --DATA="airline-routes-data.csv" --SRC_COUNTRY="India" --DEST_CITY="Tokyo" --DEST_COUNTRY="Japan"`

* Test 6
    * Input: `airline-routes-data.csv`
    * Expected output: `test06.txt`
    * Test: `./tester 6`
    * Command automated by tester: `./route_manager --DATA="airline-routes-data.csv" --SRC_COUNTRY="Panama" --DEST_CITY="New York" --DEST_COUNTRY="United States"`

* Test 7
    * Input: `airline-routes-data.csv`
    * Expected output: `test07.txt`
    * Test: `./tester 7`
    * Command automated by tester: `./route_manager --DATA="airline-routes-data.csv" --SRC_CITY="Victoria" --SRC_COUNTRY="Canada" --DEST_CITY="Cancun" --DEST_COUNTRY="Mexico"`

* Test 8
    * Input: `airline-routes-data.csv`
    * Expected output: `test08.txt`
    * Test: `./tester 8`
    * Command automated by tester: `./route_manager --DATA="airline-routes-data.csv" --SRC_CITY="Toronto" --SRC_COUNTRY="Canada" --DEST_CITY="Cancun" --DEST_COUNTRY="Mexico"`

* Test 9
    * Input: `airline-routes-data.csv`
    * Expected output: `test09.txt`
    * Test: `./tester 9`
    * Command automated by tester: `./route_manager --DATA="airline-routes-data.csv" --SRC_CITY="Paris" --SRC_COUNTRY="France" --DEST_CITY="Dubai" --DEST_COUNTRY="United Arab Emirates"`
