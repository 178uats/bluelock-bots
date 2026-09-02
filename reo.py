import discord
from discord.ext import commands
from discord import app_commands
import random

# Definición del cliente con los Intents necesarios para leer mensajes
class ReoBot(discord.Client):
    def __init__(self):
        # Habilitamos message_content para detectar cuando el bot de Nagi responde en el canal
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

client = ReoBot()

# --- BASE DE DATOS DE FRASES DE REO MIKAGE (MANSHINE CITY) ---
FRASES_NAGI_OBSESION = [
    "Nagi es mi tesoro. Yo fui quien descubrió su talento y juntos ganaremos la Copa del Mundo.",
    "No importa qué tan difícil sea la situación, si le pongo el balón perfecto a Nagi, sé que creará un milagro.",
    "A veces Nagi es demasiado perezoso, pero para eso estoy yo aquí: para llevarlo a la cima del fútbol mundial.",
    "¡Míralo! Con el entrenamiento de Manshine City, la dupla que hago con Nagi es invencible."
]

FRASES_CAMALEON_Y_ESTILO = [
    "Gracias a mi habilidad de Camaleón, puedo copiar cualquier técnica al 99% de precisión.",
    "Tengo el dinero, el talento y la visión para conseguir todo lo que me propongo en esta vida.",
    "Manshine City me enseñó a moldear mi cuerpo para ejecutar cualquier estilo de juego que la situación exija.",
    "No necesito ser un especialista en una sola cosa cuando puedo hacerlo todo al nivel de un élite."
]

FRASES_CHRIS_Y_MANSHINE = [
    "Chris Prince nos dio una preparación física científica impecable. Ahora mis pases tienen mucha más potencia y precisión.",
    "En Manshine aprendí que no solo debo asistir a Nagi, sino ser una amenaza de gol por mi propia cuenta."
]

# --- RESPUESTAS AUTOMÁTICAS A NAGI ---
REACCIONES_A_NAGI = [
    "💜 **Reo:** ¡No seas haragán, Nagi! Vamos, levántate que aún tenemos que entrenar con Chris.",
    "💜 **Reo:** Tranquilo Nagi, déjamelo a mí. Yo te prepararé el pase perfecto para que solo tengas que definir.",
    "💜 **Reo:** ¡Oye, Nagi! Deja ese teléfono un segundo, te compré la bebida que te gusta.",
    "💜 **Reo:** ¿Ves? ¡Ese es el genio de mi Nagi! Nadie más en el mundo puede amortiguar un balón así."
]

# --- COMANDOS SLASH (/) ---

@client.tree.command(name="hablar", description="Habla con Reo Mikage de Manshine City.")
@app_commands.describe(mensaje="Lo que quieres decirle a Reo")
async def hablar(interaction: discord.Interaction, mensaje: str):
    msg_lower = mensaje.lower()
    
    # Lógica de respuestas basada en palabras clave
    if any(p in msg_lower for p in ["nagi", "tesoro", "dupla", "promesa"]):
        respuesta = random.choice(FRASES_NAGI_OBSESION)
    elif any(p in msg_lower for p in ["camaleon", "copiar", "tecnica", "habilidad", "dinero", "rico"]):
        respuesta = random.choice(FRASES_CAMALEON_Y_ESTILO)
    elif any(p in msg_lower for p in ["manshine", "chris", "prince", "entrenar"]):
        respuesta = random.choice(FRASES_CHRIS_Y_MANSHINE)
    else:
        respuesta = random.choice(FRASES_NAGI_OBSESION + FRASES_CAMALEON_Y_ESTILO)

    await interaction.response.send_message(f"💜 **Reo:** {respuesta}")

@client.tree.command(name="tesoro", description="Pregúntale a Reo sobre su plan para ganar el mundial.")
async def tesoro(interaction: discord.Interaction):
    await interaction.response.send_message("💜 **Reo:** Mi plan no ha cambiado desde el primer día: ¡usaré todo mi talento y el de Nagi para conquistar el mundo!")

# --- EVENTO DE ESCUCHA DE MENSAJES (INTERACCIÓN CON NAGI) ---

@client.event
async def on_message(message: discord.Message):
    # Evita que el propio bot de Reo responda a sus propios mensajes
    if message.author == client.user:
        return

    # Si el mensaje proviene de Nagi (detecta si la respuesta empieza con el icono de Nagi "🎮 **Nagi:**")
    if "🎮 **Nagi:**" in message.content:
        # Hay un 70% de probabilidad de que Reo salga a responderle o complementarle
        if random.random() < 0.7:
            await message.channel.send(random.choice(REACCIONES_A_NAGI))

    await client.process_commands(message)

@client.event
async def on_ready():
    print(f'Bot conectado como {client.user} - ¡Reo Mikage listo para asistir a Nagi!')

# Reemplaza 'TU_TOKEN_AQUI' por el token del bot de Reo
if __name__ == "__main__":
    client.run('TU_TOKEN_AQUI')