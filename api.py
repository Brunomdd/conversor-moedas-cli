import requests

def api_moeda(origem):
    try:
        response = requests.get(f"https://v6.exchangerate-api.com/v6/44d6878ce80641a9ce9ee3eb/latest/{origem}", timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.ConnectionError:
        print('A API não conseguiu se conectar')
    except requests.exceptions.Timeout:
        print('Tempo de resposta expirou!')
    except requests.exceptions.InvalidURL:
        print('URL inválida!')
    except requests.exceptions.HTTPError as error:
        print(f'Erro: {error}')
    except ValueError:
        print('formato de dados inválido!')
        return None

