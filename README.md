# Authentication-Bypass-Script-using-SQL-Injection
This Python script demonstrates a simple SQL injection attack to bypass authentication on a web application that is vulnerable to such attacks.


Usage
Environment Setup: Ensure Python 3.x and the requests library are installed. This script is tested on various websites sourced from [phpgurukul](https://phpgurukul.com/)

Script Execution:

1) Run the script and enter the target URL when prompted.

2) The script sends a crafted payload to attempt authentication bypass.

3) It checks the response for indications of successful bypass.


Script Details

Script File: auth_bypass_sqli.py


Dependencies: requests, re (built-in)


Payload Used: ' or '1'='1'# (username=%27+or+%271%27%3D%271%27%23&password=asdasd&login=)

Breakdown of the Payload ' or '1'='1'#


1) Single Quotes ('):


In SQL syntax, single quotes are used to denote string literals. They encapsulate text values in SQL queries.
Logical Condition ('1'='1'):


2) '1'='1' is a logical condition that always evaluates to true in SQL.


In SQL, = is the equality operator. So, '1'='1' means the string literal '1' is equal to itself, which is always true.
Comment (# or --):


3) The # symbol or -- (double hyphen) is used in SQL to indicate a comment. Anything following # or -- on the same line is ignored by the SQL parser.
How It Exploits SQL Injection


Context:

Imagine a login form where the application constructs an SQL query to check the credentials provided (username and password) against a database.


SELECT * FROM users WHERE username='input_username' AND password='input_password';


Injection Point: If the application is vulnerable to SQL injection and does not properly sanitize input, an attacker can manipulate the query structure.


Injected Payload: If the attacker inputs ' or '1'='1'# as the username, the resulting query would be modified to something like:


SELECT * FROM users WHERE username='' or '1'='1'#' AND password='input_password';


Effect:


The injected payload ' or '1'='1'# causes the WHERE clause to always evaluate to true ('1'='1' is true for all rows).


The # at the end comments out the rest of the original query, effectively bypassing the password check (AND password='input_password').

Documentation
URL: Enter the target URL of the vulnerable login page.
Headers: Custom headers are set for the HTTP request.
Payload: SQL injection payload used for the username field.
Response Handling: Checks if the response contains a specific pattern (Dashboard) indicating successful login.

Notes
This script is for educational purposes only and should not be used maliciously.
Always ensure you have permission to test on the target application.
Use responsibly and follow ethical guidelines when testing or demonstrating vulnerabilities.
