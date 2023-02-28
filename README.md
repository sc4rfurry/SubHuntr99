[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
##
# SubHuntr99
Hunting Sub-Domain(s) by scraping *subdomainfinder.c99.nl*.
##

## Table of contents
* [General info](#general-info)
* [Github Info](#github-info)
* [Technologies](#technologies)
* [Usage/Examples](#usage/examples)
* [Contributing](#contributing)
* [Contributors](#contributors)
* [License](#license)
* [Feedback](#feedback)

#

# General info
` SubHuntr99 ` is a python script that scrapes subdomains from *subdomainfinder.c99.nl* and saves them in a file. It also supports `Docker` for easy deployment.
</br>

  ##  Github Info :-
</br>

  <img src="https://i.ibb.co/F0RgV5R/sub.png" alt="sub" border="0">

#

### 🔧 Technologies & Tools

![](https://img.shields.io/badge/OS-Linux-informational?style=flat-square&logo=kali-linux&logoColor=white&color=5194f0&bgcolor=110d17)
![](https://img.shields.io/badge/Editor-VS_Code-informational?style=flat-square&logo=visual-studio&logoColor=white&color=5194f0)
![](https://img.shields.io/badge/Language-python-informational?style=flat-square&logo=python&logoColor=white&color=5194f0&bgcolor=110d17)
![](https://img.shields.io/badge/Python_Version-3.10-informational?style=flat-square&logo=python&logoColor=white&color=5194f0&bgcolor=110d17)

##

### 📚 Requirements
> - Python 3.9+
> - pip3

##
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
    
## Usage/Examples

```bash
python3 main.py
```

## Docker
```bash
# Build the docker image
docker build -t subhuntr99 .

# Run the docker image
docker run -it subhuntr99

# Run the docker image with a argument
docker run -it subhuntr99 -d example.com
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

#
## Contributors
Special Thanks goes to :-
- [@cosad3s](https://github.com/cosad3s)
#
## License

[MIT](https://choosealicense.com/licenses/mit/)

## Feedback

If you have any feedback, please reach out to us at akalucifr@protonmail.ch