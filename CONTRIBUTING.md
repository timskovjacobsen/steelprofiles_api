# Contributing

Contributions to this repository are greatly appreciated.

Please follow these simple guidelines if you want to contribute:

1. **Fork the repo**

2. **Create a branch** whose name reflects the change you make. If it's tied to an issue, you could e.g. use `issue<issue_number>` or something like that as the branch name

    1. **(Optional) Create a virtual environment**
  
        Create a virtual environment, e.g. with Python's built-in `venv`

        Linux (and Mac):

            python3 -m venv .venv

        Windows:

            python -m venv .venv

        This will create a virtual environment in a directory named `.venv`. You can call it something else if you want.

        Activate the environment with

        Linux (and Mac):

            source .venv/bin/activate

        Windows:

            .venv/Scripts/activate

3. **Install requirements**

    All platforms:

        python -m pip install -r requirements.txt

4. **Run the FastAPI app locally**

        python main.py

    Then visit `localhost:4000`

5. **Do some commits** that address the change/additions/deletions you want to make

    * Write commit messages to the best of your ability summarizing the changes
  
6. **Open a Pull Request**

> The app was developed with Python 3.8 and has been tested with 3.9 as well.
