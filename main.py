#!/usr/bin/env python3

from time import sleep
import requests
from bs4 import BeautifulSoup
from bs4.dammit import EncodingDetector
from rich.console import Console
from user_agent import generate_user_agent

console = Console()



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
    Sub Domian Finder --> subdomainfinder.c99.nl
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
    _urls = []
    ua = generate_user_agent(os=('linux', 'win'))
    console.print(f"\t[white bold]*[/white bold] [steel_blue1 bold]Checking Connection[/steel_blue1 bold]....")
    check_internet_conn()
    if check_internet_conn:
        console.print(f"\t[white bold]*[/white bold] [green bold]Connected: [cyan bold]subdomainfinder.c99.nl[/cyan bold][/green bold]\n")
    else:
        console.print(f"\t[yellow bold]*[/yellow bold] [red bold]Unable to connect to server: [cyan bold]subdomainfinder.c99.nl[/cyan bold][/red bold]")
        exit(1)
    user_input = str(input(f"""\t{bcolors.FAIL}┌──({bcolors.OKGREEN}Domain{bcolors.ENDC}{bcolors.FAIL}){bcolors.ENDC}  
      {bcolors.FAIL}  └─~/>> {bcolors.ENDC}"""))
    domain = user_input
    getLatestResults(user_input)
    console.print(f"\n\t[white bold]*[/white bold] [green bold]Scraping the Scan Timeline[/green bold]")
    sleep(2)
    console.print(f"\t[white bold]*[/white bold] [green bold]Scan Timeline Results: [white bold]{len(urls)}[/white bold][/green bold]")
    sleep(1)
    console.print(f"\t[white bold]*[/white bold] [green bold]Setting the latest Timeline: [/green bold][yellow bold]https:{top_t3n[0]}[/yellow bold]")
    sleep(3)
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
        console.print(f"\t[white bold]*[/white bold] [green bold]Fetched [dark_khaki bold]{len(_urls)}[/dark_khaki bold] Sub-Domains[/green bold]\n")
        sleep(3)
        console.print(f"\t[pale_turquoise1 bold]┌──([/pale_turquoise1 bold][steel_blue1 bold]{str(user_input)}[/steel_blue1 bold][pale_turquoise1 bold])─([green bold]Sub-Domain[/green bold] ㉿ [dark_khaki bold]{len(_urls)}[/dark_khaki bold])[/pale_turquoise1 bold]")  
        for dom in _urls:
            dom = str(dom).replace('//', '')
            console.print(f"      [pale_turquoise1 bold]  └───>[/pale_turquoise1 bold]\t[yellow bold]  {dom}[/yellow bold]")
    except Exception as err:
        console.print(err)
        exit(1)
    except KeyboardInterrupt as err:
        console.print(err)
        exit(1)




if __name__ == "__main__":
    try:
        banner()
        main()
    except Exception as err:
        console.print(err)
        exit(1)
    except KeyboardInterrupt as err:
        console.print(err)
        exit(1)
