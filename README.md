# On-Screen Keyboard

A simple Orinted Objected Programming virual keyboard using Python and Tkinter graphics module.

## Demo

![project](https://user-images.githubusercontent.com/34337622/72948133-900d7580-3d84-11ea-904e-5c3aafc43090.gif)

## Technologies

-   Python 3.7
-   Tkinter module

## Prerequisites

-   [Python](https://www.python.org/downloads/)
-   [pip](https://pip.pypa.io/en/stable/installing/)
-   [pipenv](https://pipenv.readthedocs.io/en/latest/install/#make-sure-you-ve-got-python-pip)

## Installation

-   [Clone](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository) this repo to your local machine using:

```
$ git clone https://github.com/tarnowski-git/On-Screen_Keyboard.git
```

-   Setup your [local environment](https://thoughtbot.com/blog/how-to-manage-your-python-projects-with-pipenv):

```
# Spawn a shell with the virtualenv activated
$ pipenv shell

# Install dependencies
$ pipenv install

# Run script into local environment
$ pipenv run python keyboard.py
```

-   Compile with Pyinstaller to exectutable file:

```
# Windows
pyinstaller --onefile --windowed keyboard.py
```

## Sources

This project is based on [CID An Education Hub](https://www.youtube.com/watch?v=d5s1l8rd6rY) Tutorial.

## License

This project is licensed under the terms of the [**MIT**](https://github.com/tarnowski-git/On-Screen_Keyboard/blob/master/LICENSE) license.
