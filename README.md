# Top-Banks-Project

# How to setup the project:

### 1. Start by cloning the repo:

- Run `git@github.com:Nhlakanipho07/Top-Banks-Project.git` in a linux terminal (git bash for Windows).

### 2. Navigate to the project directory:

- On the local computer, using a code editor, navigate to the cloned repository folder and open it in the code editor. The folder should appear as follows: `Top-Banks-Project`

### 3. Set up a virtual environment:

- In the terminal (Command Prompt for Windows), navigate to the project directory and create a virtual environment

- To create and activate the virtual environment:
  - On Windows, run:
    - `python -m venv <virtual_environment>`
    - `<virtual_environment>\Scripts\activate` in the terminal.
  - On macOS/Linux, run:
    - `python3 -m venv <virtual_environment>`
    - `source <virtual_environment>/bin/activate` in the terminal.

### 4. Install top_banks:

- Run `pip install .` in the terminal.

- Then, run `pip -r requirements.txt` in the terminal.

- To verify that `top_banks` and other requirements are installed properly, run:

  `pip freeze`

- This should list all the packages installed in the virtual environment.

*The project should now be ready to run.*
*After running the project, deactivate the virtual environment to ensure a clean workspace.*
# How to deactivate the virtual environment:

- Run `deactivate` in the terminal (Command Prompt for Windows).