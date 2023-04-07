# README FIRST INSTRUCTIONS

* Make a python virtual environment. It will put python and pip in those environments first in the env PATH variable.
* Then, activate it.
* Then, install and packages listed in the `requirements_PYTHON_VERSION.txt` file (eg. `requirements_3.10.txt`, `requirements_3.txt`, etc.) 
* Use the following commands as a general structure:

```
## Create virtual environment
python_version -m venv venvPYTHON_VERSION
## Activate virtual environment
## (this will put this python's path as first entry in PATH env variable so that all packages will be installed here)
source ./venvPYTHON_VERSION/bin/activate
## Install required packages
pip3 install -r requirements_PYTHON_VERSION.txt
```

* As examples for specific python versions, use the following commands on any new computer ...
```
###############
## For python3
python3 -m venv venv3
source ./venv3/bin/activate
pip3 install -r requirements_3.txt
###############
## For python3.10
python3.10 -m venv venv3.10
source ./venv3.10/bin/activate
pip3.10 install -r requirements_3.10.txt
###############
## etc.
```

* Once done, then deactivate venv
```
deactivate
```
