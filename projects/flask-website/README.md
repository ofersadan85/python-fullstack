# Example website using Flask

This is an example website using Flask.

## Installation

To test this website on your local machine, follow these steps:

### Clone the repository

```bash
git clone https://github.com/ofersadan85/python-fullstack/
cd python-fullstack/projects/flask-website  # Go to the project directory
```

### Create a virtual environment (optional)

```bash
python -m venv .venv
```

If you created a virtual environment, make sure to activate it in VSCode, or use the `pip` executable in the virtual environment's `Scripts` directory for the following steps.

### Install the dependencies

```bash
pip install -r requirements.txt
# OR if you created a virtual environment:
.venv/Scripts/pip install -r requirements.txt
```

### Run the website

Run the flask server, either from VSCode (the main fail is called `main.py`) or from the command line:

```bash
python main.py
```

### Open the website

Open your browser and go to [http://localhost:5000](http://localhost:5000) or [http://127.0.0.1:5000](http://127.0.0.1:5000). This is just the default address, please check your terminal output for the actual address.

## Project structure

The project structure is as follows:

```text
.
├── main.py             # The main entry point of the website
├── data.db             # An sqlite DB file
├── README.md           # This guide you're reading right now
├── requirements.txt    # The list of dependencies
├── static              # Static files (images, CSS, JS, etc.)
│   ├── images          # Images
├── templates           # HTML templates (Jinja2)
├── sql                 # SQL files
```

## Features added / TODO

### Done

- [x] Structure: `static`, `views` and `templates` directories
- [x] Structure: `requirements.txt` file
- [x] Structure: `README.md` file
- [x] Pages / Logic: Login/logout
- [x] Pages / Logic: Register new user
- [x] Structure: Use a database instead of the `users.json` file

### TODO

- [ ] Add some javascript validation to the forms
