import discord
from discord.ext import commands
from discord import app_commands
import random

class ShidouBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

client = ShidouBot()

# --- FRASES DE SHIDOU ---
FRASES_LOCURA_Y_DOPAMINA = [
    "🐉 ¡BOOOOOOM! ¡Siento cómo explota la biología en mis venas! ¡Ese gol fue puro orgasmo futbolístico!",
    "💥 ¡Ja, ja, ja! ¿Estrategias? ¿Tácticas? ¡Basura! El fútbol es la explosión pura de los instintos en el área.",
    "🔥 ¡Si no estás dispuesto a romperte la espalda dando una chilena en el aire, no tienes derecho a hablarme!",
    "😈 ¡Ese pase tuvo demasiada dopamina! ¡Voy a destruir esa portería de un zapatazo salvaje!"
]

RESPUESTAS_A_CHARLES = [
    "🐉 ¡Ese es mi chico Charles! ¡Ponme otro pase de esos en el cielo para volver a volar!",
    "💥 ¡Ja, ja, ja! ¡Eres un enano travieso, Charles! ¡Dámela más alto la próxima vez!",
    "😈 ¡Charles, no te comas mis dulces o te mando volando de un cabezazo!"
]

BROMAS_A_OTROS = [
    "💥 ¡Oigan, manga de zombies aburridos! ¡Dejen de hablar de estrategia y pónganse a volar como yo!",
    "😈 ¡A ver quién de ustedes tiene los pantalones para intentar bloquear una chilena mía directita a la cara! ¡Ja, ja, ja!"
]

# --- COMANDOS SLASH ---

@client.tree.command(name="hablar", description="Habla con el demonio indomable de Blue Lock, Ryusei Shidou.")
@app_commands.describe(mensaje="Lo que quieres decirle a Shidou")
async def hablar(interaction: discord.Interaction, mensaje: str):
    await interaction.response.send_message(f"🐉 **Shidou:** {random.choice(FRASES_LOCURA_Y_DOPAMINA)}")

@client.tree.command(name="chilena", description="Pide a Shidou que haga un tiro imposible en el chat.")
async def chilena(interaction: discord.Interaction):
    await interaction.response.send_message("🐉 **Shidou:** ¡Miren arriba! *(Se lanza de espaldas al aire y clava una chilena al ángulo)* ¡EXPLOSIÓN TOTAL! 💥")

# --- ESCUCHA DE MENSAJES ---

@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return

    contenido = message.content

    # Si habla Charles
    if "🍬 **Charles:**" in contenido:
        if random.random() < 0.8:
            await message.channel.send(random.choice(RESPUESTAS_A_CHARLES))
    
    # Si habla cualquier otro bot
    elif any(tag in contenido for tag in ["Barou", "Niko", "Aryu", "Snuffy", "Lorenzo", "Aiku", "Nagi", "Reo", "Chris"]):
        if random.random() < 0.25: # 25% de probabilidad de meterse a provocar
            await message.channel.send(random.choice(BROMAS_A_OTROS))

    await client.process_commands(message)

@client.event
async def on_ready():
    print(f'Bot conectado como {client.user} - ¡Ryusei Shidou listo para hacer explotar todo!')

if __name__ == "__main__":
    client.run('TU_TOKEN_AQUI')