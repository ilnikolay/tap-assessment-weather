- [TAP Assessment](#tap-assessment)
    * [Overview](#overview)
        + [Example usage](#example-usage)
            - [Country endpoint](#country-endpoint)
            - [City endpoint](#city-endpoint)
            - [Weather endpoint](#weather-endpoint)
        + [Some useful information](#some-useful-information)
        + [Tasks](#tasks)

# TAP Assessment

Your task is to demonstrate your knowledge regarding python coding, git usage and setting up CI/CD processes. This is an
open book assessment, so you are free to use any resources available as long as you work on your own. Collaboration of
any kind is prohibited and results in a failed assessment.

This project is part of the Talent Accelerator Program at Infinite Lambda. Read more about the programme at
[the official website](https://infinitelambda.com/talent-accelerator/).

## Overview

The software is a REST API that helps you browse countries and cities, and shows you the weather of a provided city.

### Example usage

#### Country endpoint

- List all countries:
  ```shell
  curl http://localhost:5000/country
  ```

- Filter countries with `startsWith`:
  ```shell
  curl 'http://localhost:5000/country?startsWith=un'
  ```
  Returns countries starting with 'un', ignores case:
  ```shell
  ["United Arab Emirates","United Kingdom","United States"]
  ```

- Filter countries with `contains`:
  ```shell
  curl 'http://localhost:5000/country?contains=kingdom'
  ```
  Returns countries containing 'kingdom', ignores case:
  ```shell
  ["Hashemite Kingdom of Jordan","United Kingdom"]
  ```

- Combine filters:
  ```shell
  curl 'http://localhost:5000/country?startsWith=un&contains=kingdom'
  ```
  Filters are additive, so both of them apply:
  ```shell
  ["United Kingdom"]
  ```

#### City endpoint

- List all cities:
  ```shell
  curl 'http://localhost:5000/country/Bulgaria'
  ```
  Lists all cities of Bulgaria.

- The same `startsWith` and `contains` filters can be used

#### Weather endpoint

- Show weather for a city:
  ```shell
  curl 'http://localhost:5000/country/Hungary/city/Budapest'
  ```
  Shows weather for Budapest, by calling a remote weather API.

### Some useful information

- Read through the information and tasks before starting coding, so you have a better overview that allows better
  planning of tasks and time
- There are some tests created for the code, so you can check your progress anytime by running them. They should turn
  green once all the python-related tasks are sorted out (missing parts are implemented, syntax errors are fixed)
- Being stuck on some issue can be annoying. Be very mindful of your time:
    - If something is not clear, reach out to Miro or Gabor as soon as possible
    - If you cannot solve something, move on and get back later if you still have time
- You do NOT have to document your progress with screenshots and such, as the assessment will be done based on your
  repository and CI/CD processes. You have until end of LAB time to finish up everything, changes made after that time
  are not taken into consideration. Keep a steady pace, but do not stress about not finishing something, this is
  supposed to be challenging.
- Post your repository to #tap-devops-2021, and ask your questions in private messages to Miro and/or Gabor

### Tasks

- Fork this repository to create your own
- Merge the branch `add-changes` to your main
- Tag current commit with the content of `version.txt`
- Set up a branching strategy for different environments:
    - `dev` branch should be created from `main`
    - `staging` should be created from `main`
- Finish the missing parts in the python files, annotated with `# todo` and fix syntax errors in `app.py`
- Bump the version in `version.txt` (increment the minor version)
- Tag this commit with the new content of `version.txt`
- Set up a CI/CD pipeline on a selected platform that runs on each code change and:
    - build project
    - do a static check with mypy
    - lint code
    - run tests
    - and if it is running on `main` or `staging`, it also:
        - build a container of the app
        - deploy it to Docker Hub
- Keep your git history nice and tidy with meaningful commits all the way
