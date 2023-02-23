#!/usr/bin/env python3

import requests
import sys
import os
from bs4 import BeautifulSoup
from bs4.dammit import EncodingDetector
from rich.console import Console
from user_agent import generate_user_agent
from time import sleep
from os import getcwd, name as nm, path, makedirs
from tld import get_tld
from validators import domain as vdm
import argparse

console = Console()
cwd = getcwd()
get_os = str(nm)


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



def banner():
    banner = """
   _____       __    __  __            __       ____  ____ 
  / ___/__  __/ /_  / / / /_  ______  / /______/ __ \/ __ \\
  \__ \/ / / / __ \/ /_/ / / / / __ \/ __/ ___/ /_/ / /_/ /
 ___/ / /_/ / /_/ / __  / /_/ / / / / /_/ /   \__, /\__, / 
/____/\__,_/_.___/_/ /_/\__,_/_/ /_/\__/_/   /____//____/ 
    """
    _desc = """
    Sub Domain Finder --> subdomainfinder.c99.nl
    """
    _info = """
        [cyan bold]Author[/cyan bold]:     [green bold]Sc4rfurry[/green bold]
        [cyan bold]version[/cyan bold]:    [green bold]0.1[/green bold]
        [cyan bold]github[/cyan bold]:     [green bold]https://github.com/sc4rfurry[/green bold]
    """
    console.print(f"\t\t\t[red bold]{banner}[/red bold]\n" + f"[gray37 bold]{_desc}[/gray37 bold]" + f"\t{_info}")
    console.print(f"[blue bold]=[/blue bold]" * 80 + "\n")




def check_internet_conn():
    try:
        host = "https://subdomainfinder.c99.nl"
        s = requests.Session()
        s.get(host, timeout=10)
    except Exception as err:
        console.print(f"\t[yellow bold]*[/yellow bold] [red bold]Unable to connect to server: [cyan bold]{host}[/cyan bold][/red bold]")
        exit(1)


def validateDomain(domain):
    global vdom
    console.print(f"\n\t[white bold]*[/white bold] [green bold]Validating Domain: [/green bold]{domain}...")
    sleep(2)
    if vdm(str(domain)):
        if str(domain).startswith("http:") or str(domain).startswith("https:"):
            _fld = get_tld(domain, as_object=True)
            vdom = str(_fld.fld)
            console.print(f"\t[white bold]*[/white bold] [green bold]Domain is Valid[/green bold]...")
            return vdom
        else:
            console.print(f"\t[white bold]*[/white bold] [green bold]Domain is Valid[/green bold]...")
            vdom = domain
            return vdom
    else:
        console.print(f"\t[yellow bold]*[/yellow bold] [red bold]Invalid Domain Name(ex: example.com):[cyan bold]{domain}[/cyan bold][/red bold]")
        exit(1)


def ioFunc(domain, urls):
    global file_path
    folder_name = str(domain)
    subs = urls
    filename =  "sub-domains.log"
    if get_os == "nt":
        wd = cwd + "\\" + "Output" + "\\" + f"{folder_name}" + "\\" 
        try:
            if path.exists(wd) and path.isdir(wd):
                file_path = wd + filename
                for url in subs:
                    with open(file_path, "a+") as handler:
                        handler.write(url + "\n")
                return file_path
            else:
                try:
                    makedirs(wd)
                    file_path = wd + filename
                    for url in subs:
                        with open(file_path, "a+") as handler:
                            handler.write(url + "\n")
                    return file_path
                except Exception as err:
                    console.print(err)
                    exit(1)
                except KeyboardInterrupt as err:
                    console.print(err)
                    exit(1)
        except Exception as err:
            console.print(err)
            exit(1)
        except KeyboardInterrupt as err:
            console.print(err)
            exit(1)
    else:
        wd = cwd + "/" + "Output" + "/" + f"{folder_name}" + "/"
        try:
            if path.exists(wd) and path.isdir(wd):
                file_path = wd + filename
                for url in subs:
                    with open(file_path, "a+") as handler:
                        handler.write(url + "\n")
                return file_path
            else:
                try:
                    makedirs(wd)
                    file_path = wd + filename
                    for url in subs:
                        with open(file_path, "a+") as handler:
                            handler.write(url + "\n")
                    return file_path
                except Exception as err:
                    console.print(err)
                    exit(1)
                except KeyboardInterrupt as err:
                    console.print(err)
                    exit(1)
        except Exception as err:
            console.print(err)
            exit(1)
        except KeyboardInterrupt as err:
            console.print(err)
            exit(1)
    


def getLatestResults(dm):
    global urls, top_t3n
    urls = [] 
    top_t3n = []
    ua = generate_user_agent(os=('linux', 'win'))
    domain = str(dm)
    url = f"https://subdomainfinder.c99.nl/search.php?domain={domain}"
    s = requests.Session()
    s.headers.update({
            "user-agent": f"{ua}",
            "Accept-Encoding": "*",
            "Connection": "keep-alive"
        })
    try:
        resp = s.get(url)
        http_encoding = resp.encoding if 'charset' in resp.headers.get('content-type', '').lower() else None
        html_encoding = EncodingDetector.find_declared_encoding(resp.content, is_html=True)
        encoding = html_encoding or http_encoding
        soup = BeautifulSoup(resp.content, 'html5lib', from_encoding=encoding)
        for link in soup.find_all('a', href=True):
            if f"/{domain}" in str(link):
                domm = str(link['href'])
                if domm not in urls:
                    urls.append(domm)
                else:
                    pass
    except Exception as err:
        console.print(err)
        exit(1)
    except KeyboardInterrupt as err:
        console.print(err)
        exit(1)
    
    if len(urls) > 0:
        if len(urls[0:10]) == 10:
            top_t3n = urls[0:10]
        else:
            top_t3n = urls
    else:
        console.print(f"\n\t[yellow bold]*[/yellow bold] {len(urls)} Sub-Domain(s) Found Please Try Again...")
        exit(1)
    
    return top_t3n,urls


def main():
    global sub_domains
    sub_domains = []
    _urls = []
    
    parser = argparse.ArgumentParser(description='SubHuntr99')
    parser.add_argument('-d', type=str, required=False, dest='domain', help = "Domain")
    parser.add_argument('-u', type=str, required=False, dest='useragent', help = "User-Agent")
    parser.add_argument('-q', required=False, dest='quiet', help = "Quiet mode", action='store_true')
    args = parser.parse_args()

    if (args.quiet):
        sys.stdout = open(os.devnull, 'w')

    banner()
    
    ua = ""
    if (args.useragent):
        ua = args.useragent
    else:
        ua = generate_user_agent(os=('linux', 'win'))

    console.print(f"\t[white bold]*[/white bold] [steel_blue1 bold]Checking Connection[/steel_blue1 bold]....")
    check_internet_conn()
    if check_internet_conn:
        console.print(f"\t[white bold]*[/white bold] [green bold]Connected: [cyan bold]subdomainfinder.c99.nl[/cyan bold][/green bold]\n")
    else:
        console.print(f"\t[yellow bold]*[/yellow bold] [red bold]Unable to connect to server: [cyan bold]subdomainfinder.c99.nl[/cyan bold][/red bold]")
        exit(1)

        
    user_input = ""
    if (args.domain):
        user_input = args.domain    
    else:
        user_input = str(input(f"""\t{bcolors.FAIL}┌──({bcolors.OKGREEN}Domain{bcolors.ENDC}{bcolors.FAIL}){bcolors.ENDC}  
          {bcolors.FAIL}  └─~/>> {bcolors.ENDC}"""))
    domain = str(user_input)
    validateDomain(domain)
    
    getLatestResults(vdom)
    console.print(f"\t[white bold]*[/white bold] [green bold]Scraping the Scan Timeline[/green bold]")
    console.print(f"\t[white bold]*[/white bold] [green bold]Scan Timeline Results: [white bold]{len(urls)}[/white bold][/green bold]")
    console.print(f"\t[white bold]*[/white bold] [green bold]Setting the latest Timeline: [/green bold][yellow bold]https:{top_t3n[0]}[/yellow bold]")
    url = "https:" + top_t3n[0]
    s = requests.Session()
    s.headers.update({
            "user-agent": f"{ua}",
            "Accept-Encoding": "*",
            "Connection": "keep-alive"
        })
    try:
        console.print(f"\t[white bold]*[/white bold] [green bold]Fetching Information[/green bold]...")
        resp = s.get(url)
        sleep(2)
        http_encoding = resp.encoding if 'charset' in resp.headers.get('content-type', '').lower() else None
        html_encoding = EncodingDetector.find_declared_encoding(resp.content, is_html=True)
        encoding = html_encoding or http_encoding
        soup = BeautifulSoup(resp.content, 'html5lib', from_encoding=encoding)
        for link in soup.find_all('a', href=True):
            if f".{domain}" in str(link):
                _domain = str(link['href'])
                _urls.append(_domain)
        if len(_urls) > 0:
            console.print(f"\t[white bold]*[/white bold] [green bold]Fetched [dark_khaki bold]{len(_urls)}[/dark_khaki bold] Sub-Domains[/green bold]\n")
            sleep(3)
        else:
            console.print(f"\t[yellow bold]*[/yellow bold] [red bold]No Sub-Domain Found for: [cyan bold]{domain}[/cyan bold][/red bold]")
            exit(1)
        console.print(f"\t[pale_turquoise1 bold]┌──([/pale_turquoise1 bold][steel_blue1 bold]{str(user_input)}[/steel_blue1 bold][pale_turquoise1 bold])─([green bold]Sub-Domain[/green bold] ㉿ [dark_khaki bold]{len(_urls)}[/dark_khaki bold])[/pale_turquoise1 bold]")  
        for dom in _urls:
            dom = str(dom).replace('//', '')
            console.print(f"      [pale_turquoise1 bold]  └───>[/pale_turquoise1 bold]\t[yellow bold]  {dom}[/yellow bold]")
            sub_domains.append(dom)
        console.print(f"[blue bold]=[/blue bold]" * 80 + "\n")
        console.print(f"\t[white bold]*[/white bold] [green bold]Saving Sub-Domains...[/green bold]\n")
        ioFunc(str(user_input), sub_domains)
        sleep(2)
        console.print(f"\t[white bold]*[/white bold] [green bold]File Saved: [dark_khaki bold]{file_path}[/dark_khaki bold] ![/green bold]\n")
    except Exception as err:
        console.print(err)
        exit(1)
    except KeyboardInterrupt as err:
        console.print(err)
        exit(1)




if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        console.print(err)
        exit(1)
    except KeyboardInterrupt as err:
        console.print(err)
        exit(1)