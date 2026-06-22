#  Desafio Supabase + Z-API (Python Project)

Este projeto foi desenvolvido como parte de um desafio prático de integração automatizada de sistemas. A aplicação conecta-se a um banco de dados do **Supabase**, extrai contatos cadastrados e realiza o envio automático de mensagens personalizadas no WhatsApp utilizando o **Z-API**.

Toda a lógica e os scripts foram estruturados para rodar de maneira segura e eficiente no ambiente do plano gratuito de ambas as plataformas.

---

## ️ Tecnologias Utilizadas

* **Python 3.x**: Linguagem base do projeto.
* **Supabase Python Client**: Para comunicação direta e segura com o banco de dados PostgreSQL.
* **Z-API**: Plataforma de integração com a API do WhatsApp.
* **Requests**: Para o envio das requisições HTTP POST à API de mensagens.
* **Python-Dotenv**: Para gerenciar variáveis de ambiente locais com segurança.

---

##  Estrutura do Diretório

Dentro da pasta `PythonProject`, o repositório conta com os seguintes arquivos principais:

*   **`main.py`**: Arquivo principal com a regra de negócio que executa a busca de dados no Supabase e gerencia o disparo sequencial das mensagens no Z-API.
*   **`teste.py`**: Script auxiliar utilizado para validar de forma isolada a conexão e o status da sua instância Z-API ou credenciais do banco.
*   **`requirements.txt`**: Arquivo de definição que contém todas as dependências do ecossistema Python necessárias para a execução do app.
*   **`.env`**: *(Importante)* Arquivo onde ficam armazenadas as chaves secretas. **Este arquivo não deve ser enviado ao GitHub.**

---

##  Pré-requisitos e Configuração

Siga os passos abaixo para clonar e rodar o projeto localmente na sua máquina:

### 1. Clonar e Acessar o Projeto
No seu terminal, clone o repositório e navegue até a pasta correta do código:
```bash
git clone https://github.com
cd desafio-supabase-zapi/PythonProject
```

### 2. Criar e Configurar Variáveis de Ambiente
Por motivos de segurança, você precisará recriar o arquivo `.env` localmente. Crie um arquivo com o nome exato de `.env` na raiz da pasta `PythonProject` e preencha-o da seguinte forma:

```env
# Credenciais do Supabase
SUPABASE_URL="https://supabase.co"
SUPABASE_KEY="sua-chave-anon-public-aqui"

# Credenciais do Z-API
ZAPI_INSTANCE_ID="seu-id-da-instancia"
ZAPI_TOKEN="seu-token-da-instancia"
ZAPI_CLIENT_TOKEN="seu-client-token-de-seguranca"
```

### 3. Instalar as Dependências
Instale todos os pacotes requeridos listados no arquivo `requirements.txt`:
```bash
pip install -r requirements.txt
```

---

##  Como Executar o Projeto

1. **Garantir Conectividade**: Certifique-se de que sua instância no painel do Z-API está ativa e com o status de "Conectada" (QR Code escaneado).
2. **Preparar Banco**: Verifique se a sua tabela do Supabase contém os registros de teste cadastrados com as colunas `nome` e `telefone` (incluindo DDI e DDD, ex: `5511999999999`).
3. **Executar**: Execute o arquivo principal da aplicação:
```bash
python main.py
```

---

##  Segurança (LGPD / Chaves de API)

Este projeto segue boas práticas de segurança:
* O arquivo `.env` foi incluído nas regras do `.gitignore` para assegurar que nenhuma chave de acesso restrita seja vazada em repositórios públicos.
* O disparo respeita intervalos de segurança (delays) recomendados para evitar o bloqueio ou uso indevido da conta de WhatsApp vinculada.
