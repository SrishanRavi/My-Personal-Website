Personal Website

This workspace contains a small Flask-backed website using Bootstrap for the frontend, featuring a dark theme and responsive design.

## Development

### GitHub Setup
1. Create a new repository at https://github.com/new
2. Initialize and push your local code:
```bash
# Initialize git repository
git init

# Add your files
git add .

# Make your first commit
git commit -m "Initial commit: Personal website with Flask"

# Add your GitHub repository as remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/personal-website.git

# Push your code
git push -u origin main
```

### Making Changes
- Edit locally in VS Code, then:
  ```bash
  git add .
  git commit -m "Description of changes"
  git push
  ```
- Or edit directly on GitHub.com by clicking the pencil icon on any file

## Structure

- templates/                — Jinja2 templates (index, about, projects, contact)
- static/css/styles.css     — custom styles
- static/js/main.js         — front-end JS
- server/flask_app.py       — Flask app (serves templates and a tiny API)
- server/app.py             — (placeholder) legacy HTTPServer example — removed/replaced by Flask
- requirements.txt          — Python dependencies

Quick start (macOS / zsh)

1. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3a. Run the Flask app directly

```bash
python3 server/flask_app.py
# visit http://localhost:8000
```

3b. Or run with flask CLI

```bash
export FLASK_APP=server/flask_app.py
export FLASK_ENV=development
flask run --host=0.0.0.0 --port=8000
```

API

- GET /api/hello — returns a small JSON message from the backend

Notes

- The Flask app now renders pages from `templates/`. I removed Bootstrap from the base template so you can implement the frontend however you like.
- `server/app.py` is no longer used (kept as a placeholder file). If you want it deleted entirely, tell me and I'll remove it.
- Replace placeholder content in the templates and `static/css/styles.css` to personalize the site.

Environment & packages — quick commands and troubleshooting

1) Create and activate a virtual environment (recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2) Install dependencies from `requirements.txt`:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

3) If you need to regenerate `requirements.txt` from the environment (use after you install packages you want to keep):

```bash
pip freeze > requirements.txt
```

4) Common package troubleshooting commands:

- List installed packages:

```bash
pip list
```

- Show dependency conflicts (useful when things don't import):

```bash
pip check
```

5) Running the Flask app and common Flask troubleshooting

- Make sure the venv is activated and you're in the project root. Then run:

```bash
python3 server/flask_app.py
```

- Or use the flask CLI (if FLASK_APP not set, set it first):

```bash
export FLASK_APP=server/flask_app.py
export FLASK_ENV=development
flask run --host=0.0.0.0 --port=8000
```

- If you see "ImportError: No module named flask" or similar:
	- Ensure your venv is activated (see step 1).
	- Install Flask inside the venv: `pip install Flask`.
	- Verify your interpreter/IDE is using the venv interpreter.

- Sanity check the app by hitting the API endpoint (from the same machine):

```bash
curl http://localhost:8000/api/hello
# expected: {"message":"Hello from Flask backend","status":"ok"}
```

6) If package versions are messy, one safe workflow:

- Create a clean venv, activate it, then re-install only what you need. Use `pip freeze > requirements.txt` to capture the exact set.

7) Want help moving to a dependency tool? I can help convert to `pip-tools` or `poetry` for reproducible installs.
