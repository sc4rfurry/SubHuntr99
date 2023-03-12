[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

# SubHuntr99

Hunting Sub-Domain(s) by scraping *subdomainfinder.c99.nl*.

## Table of Contents

- [SubHuntr99](#subhuntr99)
  - [Table of Contents](#table-of-contents)
    - [📝 Description](#-description)
    - [🔧 Technologies & Tools](#-technologies--tools)
  - [📚 Requirements](#-requirements)
  - [Installation](#installation)
    - [Usage](#usage)
      - [Help Menu](#help-menu)
    - [Docker](#docker)
    - [Repo Info ](#repo-info-)
  - [Contributing](#contributing)
  - [Todo](#todo)
  - [Contributors](#contributors)
  - [License](#license)
  - [Feedback](#feedback)

#

## 📝 Description

SubHuntr99 is a python script that scrapes the subdomainfinder.c99.nl website to find sub-domains of a domain. I/O is done using the requests and BeautifulSoup libraries.
Also, it is possible to use a custom user-agent.

#

## 🔧 Technologies & Tools

![](https://img.shields.io/badge/OS-Linux-informational?style=flat-square&logo=kali-linux&logoColor=white&color=5194f0&bgcolor=110d17)
![](https://img.shields.io/badge/Editor-VS_Code-informational?style=flat-square&logo=visual-studio&logoColor=white&color=5194f0)
![](https://img.shields.io/badge/Language-python-informational?style=flat-square&logo=python&logoColor=white&color=5194f0&bgcolor=110d17)
![](https://img.shields.io/badge/Python_Version-3.10-informational?style=flat-square&logo=python&logoColor=white&color=5194f0&bgcolor=110d17)

## 📚 Requirements

- Python 3.9+
- pip3

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.
if not installed, install it using the following command.

```bash
sudo apt-get install python3-pip
```

> It is advised to install the python requirements in a virtual environment, for that install the venv package.

```bash
python3 -m pip install venv
cd SubHuntr99
python3 -m venv env
source env/bin/activate
```

After that run the following commands:

```bash
python3 -m pip install -r requirements.txt
```

## Usage
```console
1) python3 main.py -d example.com
2) python3 main.py
```

### Help Menu

```bash
                        
   _____       __    __  __            __       ____  ____ 
  / ___/__  __/ /_  / / / /_  ______  / /______/ __ \/ __ \
  \__ \/ / / / __ \/ /_/ / / / / __ \/ __/ ___/ /_/ / /_/ /
 ___/ / /_/ / /_/ / __  / /_/ / / / / /_/ /   \__, /\__, / 
/____/\__,_/_.___/_/ /_/\__,_/_/ /_/\__/_/   /____//____/ 
    

    Sub Domian Finder --> subdomainfinder.c99.nl
        
        Author:     Sc4rfurry
        version:    0.1
        github:     https://github.com/sc4rfurry
    
================================================================================

usage: main.py [-h] [-d DOMAIN] [-u USERAGENT]

SubHuntr99

options:
  -h, --help    show this help message and exit
  -d DOMAIN     Domain
  -u USERAGENT  User-Agent
```

## Docker
</br>

```bash
# Build the docker image
docker build -t subhuntr99 .

# Run the docker image
docker run -it subhuntr99

# Run the docker image with a argument
docker run -it subhuntr99 -d example.com
```

#

</br>

## Repo Info

</br>
<img src="https://i.ibb.co/TMJswzK/sub.png" alt="sub" border="0">

#

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

#

## Todo
- [ ] Clean Up the Code.
- [ ] Optimize the workflow.
- [ ] More bugs to fix. :\XD


#

## Contributors
> Special thanks to the following people who have contributed to this project:
- [@cosad3s](https://github.com/cosad3s)

Please make sure to update tests as appropriate.


#
## License

[MIT](https://choosealicense.com/licenses/mit/)

#
## Feedback

If you have any feedback, please reach out to us at akalucifr@protonmail.ch