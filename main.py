import requests
import sys
import re


def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        try:
            return requests.get("https://" + url)
        except requests.exceptions.ConnectionError:
            pass


def getSubdomains(url):
    with open("subdomains_dictionary.bat") as file:
        output_file = open("subdomains_output.bat", "w")
        for line in file:
            word = line.strip()
            target = word + "." + url
            subdomains_response = request(target)
            if subdomains_response:
                print(target)
                output_file.write(target + "\n")
        output_file.close()


def getDirectories(url):
    with open("dirs_dictionary.bat") as file:
        output_file = open("directories_output.bat", "w")
        for line in file:
            word = line.strip()
            target = url + "/" + word
            directories_response = request(target)
            if directories_response:
                print(target)
                output_file.write(target + "\n")
        output_file.close()

# def getFiles(url):
#     response = request(url)
#     htmlContent = response.content.decode("utf-8")
#     files_links = re.findall('(?:href=")(.*?)"', htmlContent)
#     for file in files_links:
#         testingResponse = request(file)
#         if testingResponse.status_code == 200:

def checkDomain(mainDomain , url):
    index = url.find(mainDomain)
    if index != -1:
        return True
    else:
        return False


url = sys.argv[1]
print("url: " + url)
response = request(url)

if response:
    getSubdomains(url)
else:
    print("invalid url!")
