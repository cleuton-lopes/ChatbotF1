import os

#Variaveis de ambiente de configuracao:

TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
PORT = int(os.environ.get('PORT', '8443'))
WEBHOOK_URL = os.environ.get('TELEGRAM_WEBHOOK')

IAM_TOKEN = os.environ.get('WATSON_ASSISTANT_TOKEN')
ASSISTANT_URL = os.environ.get('WATSON_ASSISTANT_URL')
ASSISTANT_ID = os.environ.get('ASSISTANT_ID')

T2S_TOKEN = os.environ.get('T2S_TOKEN')
T2S_URL = os.environ.get('T2S_URL')
S2T_TOKEN = os.environ.get('S2T_TOKEN')
S2T_URL = os.environ.get('S2T_URL')

