# examined-life
Because, you know... the life worth living.

## Setup
```bash
./create_virtualenv.sh
``` 
sets up the virtual environment and installs the python dependencies in it. It requires that you
have Python 2.7 and pip installed.

```bash
. venv/bin/activate
```
switches your current terminal session to the virtual environment.

## Running the Development Backend
```bash
./services/run.py
```
Starts up the development backend for local use at http://127.0.0.1:5000
