## Requisitos

- [Python 3.7+](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/docs/#installation) (ferramenta de gerenciamento de dependências e ambiente virtual)


## Instalação das Dependências

Depois de instalar o Poetry, siga os passos abaixo para configurar o ambiente do projeto:

1. Clone o repositório do projeto:

    ```sh
    git clone https://github.com/Pedro-Tuto/petshop-server.git
    cd petshop
    ```

2. Instale as dependências do projeto:

    ```sh
    poetry install
    ```

## Executando a Aplicação

Para rodar a aplicação, utilize os seguintes comandos:

1. Inicie o servidor FastAPI:

    ```sh
    poetry run fastapi dev petshop/app.py
    ```

2. Acesse a aplicação no navegador:

    Abra o navegador e vá para `localhost:8000/`.

## Comandos Úteis do Poetry

Aqui estão alguns comandos úteis do Poetry para gerenciar o projeto:

- Atualizar dependências:

    ```sh
    poetry update
    ```

- Adicionar uma nova dependência:

    ```sh
    poetry add <nome_da_dependencia>
    ```

- Remover uma dependência:

    ```sh
    poetry remove <nome_da_dependencia>
    ```

- Ativar o ambiente virtual:

    ```sh
    poetry shell
    ```

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---
