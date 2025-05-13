import discord
from discord.ext import commands
import random
import os
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def en_linea():
    print(f'Tu bot {bot.user} esta en linea!')


@bot.command()
async def info(ctx,*, mensaje:str):
    mensaje = mensaje.lower().strip()
    if mensaje == 'como podes ayudar al medio ambiente':
        await ctx.send('1. Reducir, reutilizar y reciclar, 2. Usar transporte sostenible, 3. Ahorrar energía, 4. Participar en campañas ambientales, 5. Consumir responsablemente, 6. Cuidar el agua, 7. Usar redes sociales para crear conciencia')
    elif mensaje == "que es el cambio climatico":
        await ctx.send("🌍Es el calentamiento de la Tierra debido a la acumulación de gases en la atmósfera que atrapan el calor del sol. Esto provoca que las temperaturas aumenten y se alteren los patrones del clima, como lluvias, sequías y tormentas.")
    elif mensaje == "por que ocurre":
        await ctx.send("🌡️Las actividades humanas, como quemar combustibles fósiles (petróleo, gas, carbón), talar bosques y la agricultura, liberan gases como el dióxido de carbono (CO₂) y el metano (CH₄). Estos gases forman una "manta" que atrapa el calor, elevando la temperatura global.")
    elif mensaje == "que efectos tiene":
        await ctx.send("🌪️El cambio climático provoca fenómenos extremos como huracanes, sequías, inundaciones y olas de calor. También afecta la biodiversidad, los ecosistemas y la salud humana. Además, puede causar el derretimiento de glaciares y el aumento del nivel del mar.")
    
    
@bot.command()
async def enferma(ctx):
    with open('img/enferma.jpg', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
        # A continuación, podemos enviar este archivo como parámetro.
        await ctx.send(file=picture)
        
@bot.command()
async def sana(ctx):
    with open('img/sana.jpg', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
        # A continuación, podemos enviar este archivo como parámetro.
        await ctx.send(file=picture)        
        
token = ' Aca va tu token '
bot.run(token)