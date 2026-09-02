import discord
from discord.ext import commands
from discord import app_commands
import random

class CharlesBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

client = CharlesBot()

# --- FRASES DE CHARLES ---
FRASES_BROMAS_GENERALES = [
    "🤪 ¡Aburridoooo! ¿Por qué todos hablan tan en serio? ¡Hay que lanzar un pase bomba al área para ver quién se tropieza!",
    "🍬 *(Mascando chicle)* Oye, oye, ¿alguien tiene un dulce? Si no me dan uno, voy a enviar el balón a la tribuna a propósito.",
    "🚀 ¡Boring! Si la jugada no tiene magia ni caos, prefiero no dar el pase. ¡Hagamos una travesura!",
    "🎯 ¡Ups! Mi pase le dio en la cabeza a alguien... ¡pero admitan que la trayectoria fue hermosa, jajaja!"
]

RESPUESTAS_A_SHIDOU = [
    "🤪 ¡Shidou-san! ¡Ese tiro estuvo re loco! Si sigues saltando así vas a romper el techo, jajaja.",
    "💥 ¡Ahí va otro pase imposible, Shidou! Si no llegas a chilena, te toca pagar los postres.",
    "👅 ¡Shidou-san! Deja de gritarle a los demás, ¡mira cómo se ponen de rojos, jajaja!"
]

MOLESTAR_A_OTROS = [
    "😜 ¡Oigan! ¡Los de Ubers y Manshine parecen estatuas! ¿Por qué no le ponen un poco de diversión a la vida?",
    "🍬 *(Le tira la envoltura de un dulce a los demás)* ¡Reaccionen, aburridos!"
]

# --- COMANDOS SLASH ---

@client.tree.command(name="hablar", description="Habla con el niño prodigio y bromista de PxG, Charles Chevalier.")
@app_commands.describe(mensaje="Lo que quieres decirle a Charles")
async def hablar(interaction: discord.Interaction, mensaje: str):
    await interaction.response.send_message(f"🍬 **Charles:** {random.choice(FRASES_BROMAS_GENERALES)}")

@client.tree.command(name="trolear", description="Pide a Charles que organice una travesura en el chat.")
async def trolear(interaction: discord.Interaction):
    travesuras = [
        "🍬 **Charles:** ¡Lanzaré un pase a ciegas al azar en el chat a ver a quién le cae en la cara!",
        "🍬 **Charles:** ¡Cambiémosle los zapatos de fútbol a Barou por unos de tacón mientras no mira, jajaja!",
        "🍬 **Charles:** ¡Digámosle a Chris Prince que sus abdominales son de plástico!"
    ]
    await interaction.response.send_message(random.choice(travesuras))

# --- ESCUCHA DE MENSAJES ---

@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return

    contenido = message.content

    # Si habla Shidou
    if "🐉 **Shidou:**" in contenido:
        if random.random() < 0.8:
            await message.channel.send(random.choice(RESPUESTAS_A_SHIDOU))
    
    # Si habla cualquier otro bot (Ubers o Manshine)
    elif any(tag in contenido for tag in ["Barou", "Niko", "Aryu", "Snuffy", "Lorenzo", "Aiku", "Nagi", "Reo", "Chris"]):
        if random.random() < 0.25: # 25% de probabilidad de colarse a trolear
            await message.channel.send(random.choice(MOLESTAR_A_OTROS))

    await client.process_commands(message)

@client.event
async def on_ready():
    print(f'Bot conectado como {client.user} - ¡Charles listo para causar caos!')

if __name__ == "__main__":
    client.run('TU_TOKEN_AQUI')