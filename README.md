# Contributor Reformatter
A Reformatter for GitHub APIs [Repository Contributors endpoint](https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28#list-repository-contributors) which **returns the username and name associated with each contributor.**

### Dependencies
* requests

## Installation via GitHub
#### Setting up a virtual environment (optional)
```
virtualenv [environment name]
source [environment name]/bin/activate
```

### Clone the repository (Developers)
```
git clone https://github.com/terminal-overflow/contributor-formatter.git
```

### Change directory to the project root
```
cd path/to/contributor-formatter
```

### Install requirements
```
pip3 install -r requirements.txt
```

### Run
```
python3 reformatter.py
```

## How it Works
### Prerequisites
This reformatter reads from a JSON file which should already contain results from a call to the Contributors endpoint.
Rename your JSON input file to `contributors.json`.

This example can be used for reference.
```zsh
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer AUTH_TOKEN" \ Only if needed for accessing private repositories
  -H "X-GitHub-Api-Version: 2022-11-28" \
  --url "https://api.github.com/repos/OWNER/REPO/contributors" >> contributors.json
```

### Running
Move your output/response file into the base directory of this repository.
Run the program and enter the file name of the output file you have just moved in to the repository.

> [!note]
> The program will return an error if the file `contributors.json` is not found and is not in the base directory.

### The Process
Each contributor will be looped over and the user will be queried. The username and name associated with the account will be returned.

### Output
A file called `reformatted.json` will be created in the base directory once all users have been accessed.

### Output Format
```json
[
  {
    "username": "example_username",
    "name": "example name"
  }
]
```
