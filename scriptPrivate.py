import requests

# Seu token de acesso pessoal
TOKEN = ''
# Seu nome de usuário do GitHub
USERNAME = ''

# Cabeçalhos para a autenticação
headers = {
    'Authorization': f'token {TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

# Pega todos os repositórios do usuário
repos_url = 'https://api.github.com/user/repos'
params = {'visibility': 'all', 'affiliation': 'owner'}
response = requests.get(repos_url, headers=headers, params=params)

if response.status_code == 200:
    repos = response.json()

    for repo in repos:
        repo_name = repo['name']
        repo_url = f'https://api.github.com/repos/{USERNAME}/{repo_name}'

        # Torna o repositório privado
        update_response = requests.patch(
            repo_url, headers=headers, json={'private': True})

        if update_response.status_code == 200:
            print(f'Repositório {repo_name} agora é privado.')
        else:
            print(f'Falha ao atualizar o repositório {repo_name}. Status: {
                  update_response.status_code}, Erro: {update_response.json()}')
else:
    print(f'Falha ao buscar os repositórios. Código de status: {
          response.status_code}')
