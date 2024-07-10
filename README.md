# Authentication-Bypass-Script-using-SQL-Injection
This Python script demonstrates a simple SQL injection attack to bypass authentication on a web application that is vulnerable to such attacks.


Usage
Environment Setup: Ensure Python 3.x and the requests library are installed. This script is tested on various websites sourced from [phpgurukul](https://phpgurukul.com/)

Script Execution:

1)Run the script and enter the target URL when prompted.

2)The script sends a crafted payload to attempt authentication bypass.

3)It checks the response for indications of successful bypass.


Script Details
Script File: auth_bypass_sqli.py
Dependencies: requests, re (built-in)
Payload Used: ' or '1'='1'# (username=%27+or+%271%27%3D%271%27%23&password=asdasd&login=)

Documentation
URL: Enter the target URL of the vulnerable login page.
Headers: Custom headers are set for the HTTP request.
Payload: SQL injection payload used for the username field.
Response Handling: Checks if the response contains a specific pattern (Dashboard) indicating successful login.


Example Output
Copy code
Enter URL: http://example.com/login
[+] Authentication bypassed using the following payload: username=%27+or+%271%27%3D%271%27%23&password=asdasd&login=


Notes
This script is for educational purposes only and should not be used maliciously.
Always ensure you have permission to test on the target application.
Use responsibly and follow ethical guidelines when testing or demonstrating vulnerabilities.
