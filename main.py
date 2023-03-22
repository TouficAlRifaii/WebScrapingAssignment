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
        except requests.exceptions.InvalidURL:
            pass
    except requests.exceptions.InvalidURL:
        pass


def getSubdomains(url):
    with open("subdomains_dictionary.bat") as file:
        output_file = open("subdomains_output.bat", "w")
        for line in file:
            word = re.sub(r"^\s+|\s+$", "", line)
            target = word + "." + url
            subdomains_response = request(target)
            if subdomains_response:
                output_file.write(target + "\n")
        output_file.close()


def getDirectories(url):
    with open("dirs_dictionary.bat") as file:
        output_file = open("directories_output.bat", "w")
        for line in file:
            word = re.sub(r"^\s+|\s+$", "", line)
            target = url + "/" + word
            directories_response = request(target)
            if directories_response:
                output_file.write(target + "\n")
        output_file.close()


def getFiles(url):
    with open("files_output.bat", "a") as output_file:
        response = request(url)
        htmlContent = response.content.decode("utf-8")
        files_links = re.findall('(?:href=")(.*?)"', htmlContent)
        for file in files_links:

            testingResponse = request(file)
            if testingResponse:
                if testingResponse.status_code == 200:
                    testDomain = checkDomain(url, file)
                    if testDomain:
                        getFiles(file)
                    else:
                        continue
            else:
                try:
                    testingResponse = requests.get(file)
                    if not testingResponse:
                        link = url + "/" + file
                        output_file.write(link + "\n")
                except requests.exceptions.ConnectionError:
                    pass
                except requests.exceptions.InvalidURL:
                    pass
                except requests.exceptions.MissingSchema:
                    link = url + "/" + file
                    output_file.write(link + "\n")


def checkDomain(mainDomain, url):
    index = url.find(mainDomain)
    if index != -1:
        return True
    else:
        return False


url = sys.argv[1]
response = request(url)
if response:
    open("files_output.bat", "w").close()
    # getFiles(url)  #this is to get the files hidden inside the url
    # getSubdomains(url) # this is to get the subdomains
    getDirectories(url) # this is used to get the directories of the domain
    # with open("directories_output.bat" , "r") as file:  # this chunck of code is used to get the files
    #     for line in file:                               # hidden in the subdirectories of the domain
    #         directory = re.sub(r"^\s+|\s+$", "", line)
    #         getFiles(directory)
    #
else:
    print("invalid url!")
    sys.exit(0)
