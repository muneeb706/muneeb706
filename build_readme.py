import os
import requests

TOKEN = os.environ.get("MUNEEB706_TOKEN", "")

def fetch_all_repos():
    headers = {'Authorization': f'token {TOKEN}'}
    response = requests.get('https://api.github.com/users/muneeb706/repos', headers=headers)
    repos = []
    if response.status_code == 200:
        repos = response.json()

    return repos

def filter_vscode_extensions(repos):
    vscode_extensions = [repo for repo in repos if 'vscode-extension' in repo.get('topics', [])]
    return vscode_extensions

def add_vscode_ext_repos(repos):
    with open('README.md', 'r+') as f:
        contents = f.read()
        try:
            index = contents.index('### Visual Studio Code Extensions\n')
            print(f'Text already exists at index {index}')
        except ValueError:
            f.write('### Visual Studio Code Extensions\n')
    # with open('README.md', 'w') as f:
    #     f.write('### Visual Studio Code Extensions\n')
    #     for repo in repos:
    #         f.write(f'- [{repo["name"]}]({repo["homepage"]})\n')
                    
if __name__ == "__main__":
    repos = fetch_all_repos()
    vscode_ext_repos = filter_vscode_extensions(repos)
    add_vscode_ext_repos(vscode_ext_repos)