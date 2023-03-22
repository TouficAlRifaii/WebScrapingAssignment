# Ethical Hacking and Websites Exploitation

## Description

The project's goal was to develop a
Python script that could find files,
folders, and subdomains connected to a
given website Address. This code might
be used to find hidden links that might
direct people to vulnerable pages. To find
possible subdomains and folders, the project
used two text files.

## Development

*1.* Import the necessary libraries at the top of your script. You will need the `requests`, `sys` and `re` libraries.

*2.* Define a request function that takes in a URL and uses the requests library to send an HTTP request to that URL. If
the initial request fails, try again with HTTPS. If both requests fail, pass.

*3.* Define a `getSubdomains` function that takes in a URL and reads from a dictionary file of possible subdomains. For
each potential subdomain, use the request function to send a request to that subdomain appended to the main URL. If the
request is successful, write the subdomain to an output file.

*4.* Define a `getDirectories` function that takes in a URL and reads from a dictionary file. For each potential
directory, use the request function to send a request to that directory appended to the main URL. If the request is
successful, write the directory to an output file.

*5.* Define a `getFiles` function that takes in a URL and searches for hidden files within the HTML content of that URL.
Use the `re` library to find all links that match the pattern for a file link. For each file link found, use the request
function to send a request to that file link appended to the main URL. If the request is successful and the file is
hosted on the same domain as the main URL, call the getFiles function again with the file URL. If the file is hosted on
a different domain, write the file URL to an output file.

*6.* Define a `checkDomain` function that takes in the main domain and a URL and checks if the URL is hosted on the same
domain as the main URL.

*7.* Finally, in the main body of your script, use the `request` function to send a request to the URL passed as an
argument in the command line. If the request is successful, call the `getSubdomains`, `getDirectories`, and `getFiles`
functions to search for subdomains, directories, and hidden files.

## Running the Script

To run the Script: Open the terminal in the directory where the script exist and run the following commands

````
python main.py <target url>
````

## Challenges

*1.* Cleaning the input files where we have for examples subdomains that starts wiht * or subdomains that end with .

*2.* Splitting the spaces using Regex

## Bonus

A password.py file that can be used to target a certain website and then bruteforce attack it to get the password of the
pre-defined username


