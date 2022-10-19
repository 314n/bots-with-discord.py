
import discord #importa a biblioteca discord

intents = discord.Intents.default()
clients = discord.Client(intents= intents) 
intents.message_content = True 

@clients.event 
async def on_ready():
    print(f'{clients.user} foi logado')

@clients.event 
async def on_message(message): 
    if message.author == clients.user:  # se a mensagem author for do bot, então retorne. 
        return     # Isso aqui é necessáro para que o bot não considere a mensagem dele mesmo. 
    if message.content.lower("!oi"): 
        await message.channel.send("Olá!!!")

clients.run('TOKEN') #coloque o token do seu bot aqui para rodar. 
