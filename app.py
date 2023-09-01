import os
from pathlib import Path
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from dotenv import load_dotenv
import re
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import logging
from mensagens import *
from conversor_timestamp import converte_timestamp

env_path = Path('.',) / '.env'
load_dotenv(dotenv_path=env_path)

# inicia o app 
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

client = WebClient(token=os.environ.get("SLACK_BOT_TOKEN"))
logger = logging.getLogger(__name__)

# Mensagem de rotina

# client.chat_scheduleMessage(
#     channel= 'C03FFAMKXK6',
#     text= rotina,
#     post_at = converte_timestamp(8,30),
#     )


#Mensagem de estudos

# client.chat_scheduleMessage(
#     channel= 'C03FFAMKXK6',
#     text= estudosMa,
#     post_at = converte_timestamp(12,0),
# )

# #Mensagem de escala

# client.chat_scheduleMessage(
#     channel= 'C03FFAMKXK6',
#     text= escala,
#     post_at = converte_timestamp(13, 0),
# )

#Mensagem de bom dia
@app.message(re.compile("(bom dia|bom diaa|bo dia|dia bom|Bom dia)"))
def say_hello_regex(say, context, message):
    greeting = context['matches'][0]
    user_id = message['user']
    say(f" Ótimo dia para você, <@{user_id}>! Não se esqueça de ligar o ramal 📞")


#Mensagem de almoço 
@app.message(re.compile("(almoço|Almoço)"))
def say_hello_regex(say, context, message):
    greeting = context['matches'][0]
    user_id = message['user']
    say(f" Bom almoço! Podem dar uma olhada nos retornos, por favor?")

#Mensagem de encerramento
@app.message(re.compile("(saindo|saindoo|encerrando|inté)"))
def say_descanso(say, context):
    greeting = context['matches'][0]
    say(f"Bom descanso! Não se esqueça de encerrar as conversas no chat 📲")

# @app.event("reaction_added")
# def reacao(event, say):
#     if event["reaction"] == 'calendar':
#         say("testando reação de emoji")
    
# inicia o app 
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()