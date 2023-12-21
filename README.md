# Contributor Reformatter
A Reformatter for GitHub APIs [Repository Contributors endpoint](https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28#list-repository-contributors) which **returns the user and username associated with each contributor.**

## Cloning
Clone this repository using the command `git clone https://github.com/terminal-overflow/contributor-formatter.git`.

## How it Works
### Prerequisites
This reformatter takes in a JSON file with results from a call to the Contributors endpoint.

This example can be used for reference.
```zsh
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer AUTH_TOKEN" \ Only if needed for accessing private repositories
  -H "X-GitHub-Api-Version: 2022-11-28" \
  --url "https://api.github.com/repos/OWNER/REPO/contributors" >> contributors.json
```

### Run
Move your output/response file (in the example above it would be the `contributors.json` file) into the base directory of this repository.
Run the program and enter the file name of the output file you have just moved in to the repository.

> [!note]
> The input is _technically_ the filename. It will return an error if the file is not found.

### The Process
Each contributor will be looped over and the user will be queried. The username and name associated with the account will be recorded.

### Output
A file called `reformatted.json` will be created in the base directory.

### Output Format
```json
[
  {
    "name": "example name",
    "username": "example_username"
  }
]
```
