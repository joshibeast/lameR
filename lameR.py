import requests
import sys
import time

"""
This script will check R package or list of R pakages on ossindex.sonatype.org
It will report if a package has vulnerabilities, regardless of the version.
Inspired by oysteR but slower and lamer way to do the same thing
The only advantage is that we don't have to install R or any of the packages to
perform these checks.
We don't have to sign up for the ossindex.sonatype.org because we're taking it slow
"""
print("""\

  _                      _____  
 | |                    |  __ \ 
 | | __ _ _ __ ___   ___| |__) |
 | |/ _` | '_ ` _ \ / _ |  _  / 
 | | (_| | | | | | |  __| | \ \ 
 |_|\__,_|_| |_| |_|\___|_|  \_\
 \n
Usage:
    -Run R vuln check for a single package: python lameR.py package_name
    -Run R vuln check for a list of packages: python lameR.py -f /path/to/file

I'm now running, don't worry, I'm just very slow.                            
Here are the results:
""")



def is_vulnerable(package):
    # This is the lamest REST API I've encountered so far
    # Documentation is useless
    # It won't respond with 404 for a package that doesn't exist
    # However it will return json element "description" for the one that does exist
    # But it won't do that in a reliable manner
    # Web endpoint will respond with 404
    # So we need to check the web, but when we hit a pretty restrictive rate limiting
    url_web = f"https://ossindex.sonatype.org/component/pkg:cran/{package}"
    url_api = f"https://ossindex.sonatype.org/api/v3/component-report/pkg:cran/{package}@1.0.0"
    r_api = requests.get(url=url_api)
    if r_api.status_code != 200:
        time.sleep(2)
        is_vulnerable(package)
    elif "description" not in r_api.text:
        r_web = requests.get(url=url_web)
        if r_web.status_code == 404:
            print(
                f"Package {package} is not in ossindex DB. Check manually: https://google.com?s={package}+vulnerability")
        else:
            if "No vulnerabilities detected" in r_web.text:
                print(f"Package {package} found and it doesn't contain any vulnerabilities")
            else:
                print(f"Potentially vulnerable package found = {package}. Check manually: {url_web}")
    else:
        r_web = requests.get(url=url_web)
        if "No vulnerabilities detected" in r_web.text:
            print(f"Package {package} found and it doesn't contain any vulnerabilities")
        else:
            print(f"Potentially vulnerable package found = {package}. Check manually: {url_web}")
        time.sleep(2)


if sys.argv[1] == "-f":
    with open(sys.argv[2]) as filename:
        for line in filename:
            line = line.strip()
            is_vulnerable(line)
else:
    package = sys.argv[1]
    is_vulnerable(package)
