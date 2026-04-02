# 💱 Conversor de Moedas CLI

## 📌 Descrição

Aplicação em Python executada via terminal (CLI) que permite converter valores entre moedas utilizando uma API externa.
O sistema também armazena um histórico de conversões, permitindo visualização, ordenação e filtragem.

---

## 🚀 Funcionalidades

### ✔ Conversão de moedas

* Entrada de moeda origem e destino (ex: USD, BRL, EUR)
* Validação de entrada
* Consumo de API para obter taxa de conversão
* Resultado exibido no terminal

---

### ✔ Histórico de conversões

* Armazena:

  * moeda de origem
  * moeda de destino
  * valor original
  * valor convertido
  * data/hora
* Persistência em arquivo (JSON)

---

### ✔ Listagem de moedas disponíveis

* Consulta API
* Exibe todas as moedas suportadas

---

### ✔ Ordenação do histórico

* Ordena do mais recente para o mais antigo
* Conversão de string → datetime para comparação

---

### ✔ Filtro de histórico

* Filtra por:

  * moeda de origem
  * moeda de destino
* Retorna apenas os registros correspondentes

---

### ✔ Limpeza de histórico

* Remove todos os registros
* Confirmação antes de apagar

---

## 🧠 Estrutura do Sistema

O sistema segue o fluxo:

Entrada → Validação → Processamento → Saída → Persistência

---

## 🧩 Organização do Código

### `main.py`

* Controle do sistema (menu)
* Entrada de dados
* Validação inicial
* Integração das funcionalidades

---

### `interface_cli.py`

* Exibição de dados
* Funções de UI (linha, cabeçalho)
* Visualização do histórico

---

### `conversor.py`

* Lógica de conversão de moedas
* Consumo da API

---

### `uteis.py`

* Funções auxiliares:

  * leitura de input
  * salvar/carregar dados
  * confirmação de ações

---

## 🧠 Conceitos Aplicados

* Manipulação de listas
* Uso de dicionários
* Tratamento de erros
* Conversão de datas (`datetime`)
* Ordenação com `sorted(key=...)`
* DRY (Don't Repeat Yourself)
* Separação de responsabilidades

---

## ⚠️ Validações Implementadas

* Moeda deve ter 3 caracteres
* Valor deve ser maior que zero
* Tratamento de falha da API
* Uso de `.get()` para evitar erros em dicionário

---

## ❌ Possíveis melhorias futuras

* Melhor tratamento de erros (mensagens mais específicas)
* Filtro mais flexível (campos opcionais)
* Interface gráfica (GUI)
* Versão web (API + frontend)
* Logs de erro
* Testes automatizados

---

## 🧪 Como executar

```bash
python main.py
```

---

## 📚 Aprendizados

Durante o desenvolvimento, foram praticados:

* Controle de fluxo
* Organização de código
* Debug de erros
* Reutilização de funções
* Estruturação de sistemas simples

---

## 💬 Conclusão

Este projeto consolidou fundamentos importantes de programação, principalmente:

* manipulação de dados
* estruturação de lógica
* organização de funções

Servindo como base para projetos mais avançados.

---




## 🔌 Integração com API (Exchange Rate)

O sistema utiliza uma API de taxas de câmbio para obter os valores atualizados das moedas.
Esta API requer uma **API Key gratuita**.

---

### 🔑 Como obter a API Key

1. Acesse o site da ExchangeRate API
2. Crie uma conta gratuita
3. Copie sua chave (API Key)

---

### 📡 Como funciona

1. O usuário informa:

   * moeda de origem (ex: USD)
   * moeda de destino (ex: BRL)
   * valor

2. O sistema faz uma requisição para a API com a chave:

```bash
https://v6.exchangerate-api.com/v6/SUA_API_KEY/latest/USD
```

3. A API retorna um JSON com as taxas:

```json
{
  "result": "success",
  "base_code": "USD",
  "conversion_rates": {
    "BRL": 5.23,
    "EUR": 0.92,
    "JPY": 150.10
  }
}
```

4. O sistema pega a taxa correspondente e calcula:

```text
valor * taxa
```

---

## 🧪 Exemplo prático

Conversão de 100 USD para BRL:

* Taxa: 5.23
* Resultado: 523.00 BRL

---

## ▶️ Como usar o sistema

### 1. Executar o programa

```bash
python main.py
```

---

### 2. Escolher opção no menu

```text
1 - Converter moeda
2 - Listar moedas disponíveis
3 - Ver histórico
4 - Limpar histórico
5 - Ver histórico ordenado
6 - Filtrar histórico
7 - Sair
```

---

### 3. Converter moeda

Digite:

```text
Moeda de origem: USD
Moeda de destino: BRL
Valor: 100
```

Saída:

```text
100 USD → 523.00 BRL (salvo no histórico ✅)
```

---

### 4. Ver histórico

Mostra todas as conversões realizadas.

---

### 5. Filtrar histórico

Digite uma moeda:

```text
USD
```

O sistema mostrará apenas registros com essa moeda.

---

## ⚠️ Observações importantes

* As moedas devem ter **3 letras** (ISO 4217)
* Ex: USD, BRL, EUR
* A API depende de conexão com a internet
* Caso a API falhe, o sistema exibirá erro
* A API possui limite de requisições no plano gratuito

---

## 🔑 Configuração da API Key (importante)

⚠️ **Nunca coloque sua API Key diretamente no código ao subir no GitHub**

Use variável de ambiente:

```bash
export API_KEY=sua_chave_aqui
```

Ou crie um arquivo `.env`:

```bash
API_KEY=sua_chave_aqui
```

---

## 🔑 Dependências

* Python 3.x
* Biblioteca `requests` (se usada)

Instalar:

```bash
pip install requests
```

---

## 💡 Nota

Este projeto utiliza uma API externa com autenticação via chave.
Para aplicações maiores, recomenda-se gerenciar credenciais com segurança (variáveis de ambiente).

