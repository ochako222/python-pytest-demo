# Initialization python project

First of all, we need to update our global python files 

```bash
brew update
brew install pyenv
brew install python

brew info python
```

Now we need to activate a virtual environment
```bash
python3 -m venv env
source env/bin/activate.fish
```

In case to deactivate python environment, type:

```bash
deactivate
```

Create project structure
```bash
mkdir -p config source test utils && touch main.py requirements.txt config/__init__.py source/__init__.py test/__init__.py utils/__init__.py
```

Now we have the project structure and we can install the first libraries
```bash
echo -e "requests\npytest" > requirements.txt
pip install -r requirements.txt
```
We installed `request` inside the Python virtual environment

Now to launch existed tests we can run command:

```bash
python -m pytest
```

or use existed `Makefile` script:

```bash
make foo
```
