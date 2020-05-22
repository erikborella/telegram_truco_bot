# telegram_truco_bot
Um bot para jogar truco no Telegram

## Configuração de variaveis
Crie um arquivo chamado ".env" no diretorio raiz, e defina as variaveis:

    TOKEN = {Seu token telegram}
    NGROK_URL = {Seu endereço do NGROK}
    
### Token
Para conseguir seu token, basta acessar o Telegram e procurar pelo **@BotFather**, configurar o seu bot e ele automaticamente te dara um token

### URL Ngrok
Basta intalar o Ngrok em sua distribuição e executar o comando:

    $ ngrok http 5000
    
E copiar a URL https mostrada no console
    
### Dependencias e execução
Crie um ambiente virtual(env) e na pasta raiz execute o seguinte comando:

    $ pip install -r requirements.txt
    
E todas as dependencias serão instaladas.
Para executar basta executar:

    $ python app.py
