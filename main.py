import pandas as pd
from twilio.rest import Client
      openpyxl

account_sid = "AC5ee7982a4a9df2487fec7ef045a60d7c"
auth_token  = "868621c938ee9f180bcb26924b7fe3e5"
client = Client(account_sid, auth_token)


lista_meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho"]

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f"{mes}.xlsx")
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mes de {mes} alguem bateu a meta. vendedor:{vendedor}, Vendas:{vendas}')
        message = client.messages.create(
            to="+5541995357517",
            from_="+12028738352",
            body=f'No mes de {mes} alguem bateu a meta. vendedor:{vendedor}, Vendas:{vendas}')
        print(message.sid)


