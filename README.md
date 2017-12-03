# Advent of Code Solutions

My solutions to the 2017 [Advent of Code](http://adventofcode.com/) problems.

## Setup

1. Create a `.env` file:
  ```sh
  cp template.env .env
  ```
2. Log in to <http://adventofcode.com/>, go to developer tools in your browser, and copy the value of the `session` cookie. Paste this into `.env` as the value of `SESSION_ID`.
3. Install [pipenv](https://docs.pipenv.org/):
  ```sh
  pip install pipenv
  ```
4. Install dependencies:
  ```sh
  pipenv install
  ```

### VS Code

If using [VS Code](https://code.visualstudio.com/), modify the value of `python.pythonPath` in `.vscode/settings.json` to your virtualenv's Python path, which can be determined by running

```sh
pipenv --venv
```

and appending `/bin/python` to the result.

## Usage

**Note**: The `.vscode` directory is pre-configured for running solutions and tests in VS Code.

## Running final solutions

```sh
pipenv run python solutions/inverse_captcha.py # (For example)
```

## Running tests

```sh
make tests
```
