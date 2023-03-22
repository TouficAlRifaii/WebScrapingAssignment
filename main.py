import requests
import sys



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
            response = request(target)
            if response:
                print(target)
                output_file.write(target + "\n")
        output_file.close()


def getDirectories(url):
    with open("dirs_dictionary.bat") as file:
        output_file = open("directories_output.bat", "w")
        for line in file:
            word = line.strip()
            target = url + "/" + word
            response = request(target)
            if response:
                print(target)
                output_file.write(target + "\n")
        output_file.close()

url = sys.argv[1]
print("url: " + url)
response = request(url)

if response:
    getDirectories(url)
else :
    print("invalid url!")
