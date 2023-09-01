import datetime

# função para converter horário em timestamp 
def converte_timestamp(hour, minute):
    hoje = datetime.date.today() 
    dia_agendado = datetime.time(hour, minute)
    dia_convertido = datetime.datetime.combine(hoje, dia_agendado).timestamp()
    return dia_convertido


#+ datetime.timedelta(days=1)