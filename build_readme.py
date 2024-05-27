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
    content = '### Visual Studio Code Extensions\n'
    for repo in repos:
        content += f'- [{repo["name"]}]({repo["homepage"]})\n'
    return content

def add_technologies():
    content = '\n'
    content += '### Technologies\n\n'
    content += '| Backend  | Frontend | Database | Cloud & DevOps | Testing |\n'
    content += '| ------------- | ------------- | ------------- | ------------- | ------------- |\n'
    content += '|[![Backend](https://skillicons.dev/icons?i=py,django,java,spring&theme=light)](https://skillicons.dev)|[![Frontend](https://skillicons.dev/icons?i=js,ts,react,vite&theme=light)](https://skillicons.dev)|[![Database](https://skillicons.dev/icons?i=postgres,mongodb&theme=light)](https://skillicons.dev)|[![Cloud&DevOps](https://skillicons.dev/icons?i=aws,docker&theme=light)](https://skillicons.dev)|[![Testing](https://skillicons.dev/icons?i=selenium,cypress&theme=light)](https://skillicons.dev)|\n'

    return content

def update_readme(content):
    with open('README.md', 'w') as file:
        file.writelines(content)


if __name__ == "__main__":
    repos = fetch_all_repos()
    vscode_ext_repos = filter_vscode_extensions(repos)
    readme_content = add_vscode_ext_repos(vscode_ext_repos)
    readme_content += add_technologies()
    update_readme(readme_content)