# API para Avaliação de Qualidade de Metadados

## Descrição
Esse projeto tem como objetivo fornecer uma ferramenta para avaliar a qualidade dos metadados de datasets apresentados de acordo com o formato DCAT-AP. A metodologia de pontuação é explicada nessa página: [https://data.europa.eu/mqa/methodology?locale=pt](https://data.europa.eu/mqa/methodology?locale=pt).

## Instalação
Instruções passo a passo para instalar e configurar o projeto:

1. Clone o repositório:
   ```
   git clone https://github.com/gscerveira/mvp-pos-api.git
   ```
2. Entre no diretório do projeto:
   ```
   cd mvp-pos-api
   ```
3. Crie um ambiente virtual:
   ```
   python3 -m venv venv
   ```
4. Ative o ambiente virtual:
   ```
   source venv/bin/activate
   ```
5. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```
6. Execute o Flask
    ```
    flask run
    ```
7. Acesse a API em [http://127.0.0.1:5000/], onde você encontrará a documentação da API.