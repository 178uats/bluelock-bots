import discord
from discord.ext import commands
from discord import app_commands
import random

# Definición del cliente y árbol de comandos slash
class AryuBot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

client = AryuBot()

# --- BASE DE DATOS DE FRASES DE ARYU (UBERS) ---
FRASES_GLAM = [
    "Eso que acabas de decir... ¡no tiene nada de Glam!",
    "Mi presencia en el campo de Ubers no es solo defensiva, es una pasarela de elegancia.",
    "No importa cuán difícil sea la jugada, si la intercepto con elegancia, se vuelve Glam.",
    "Mis piernas largas y mi salto impecable están hechos para dominar las alturas con estilo.",
    "El fútbol de Snuffy es funcional, pero mi toque es puramente estético y fabuloso."
]

FRASES_CABELLO_Y_ESTILO = [
    "Mi cabello al viento durante un despeje de cabeza es la definición perfecta del arte.",
    "¿Cuidado personal? Por supuesto. Un verdadero rey de la elegancia cuida su piel y su cabello antes de cada partido.",
    "No me toques el cabello mientras defiendo. La postura debe mantenerse impecable en todo momento."
]

FRASES_DEFENSA_UBERS = [
    "Con mis extremidades largas, alcanzo balones que para otros serían imposibles. Eso es Glam absoluto.",
    "Ubers nos da la estructura, pero yo le aporto la belleza que este equipo necesita.",
    "Bloquear tu tiro no fue difícil... simplemente extendí mis piernas con absoluta elegancia."
]

FRASES_RIVALES = [
    "Rin... ese tipo tiene una aura oscura interesante, pero le falta soltura.",
    "Isagi piensa demasiado. La verdadera elegancia fluye sin tanto esfuerzo mental.",
    "Barou es demasiado ruidoso y agresivo. Le vendría bien un poco más de clase y estilo."
]

# --- COMANDOS SLASH (/) ---

@client.tree.command(name="hablar", description="Habla con Jyubei Aryu y descubre si tienes suficiente Glam.")
@app_commands.describe(mensaje="Lo que quieres decirle a Aryu")
async def hablar(interaction: discord.Interaction, mensaje: str):
    msg_lower = mensaje.lower()
    
    # Lógica de respuestas basada en palabras clave
    if any(p in msg_lower for p in ["pelo", "cabello", "estilo", "moda", "guapo", "lindo"]):
        respuesta = random.choice(FRASES_CABELLO_Y_ESTILO)
    elif any(p in msg_lower for p in ["glam", "elegante", "elegancia", "bonito", "arte"]):
        respuesta = "¡Exacto! Veo que entiendes el verdadero significado del Glam."
    elif any(p in msg_lower for p in ["ubers", "defensa", "alto", "piernas", "salto", "snuffy"]):
        respuesta = random.choice(FRASES_DEFENSA_UBERS)
    elif any(p in msg_lower for p in ["barou", "isagi", "rin", "rival"]):
        respuesta = random.choice(FRASES_RIVALES)
    else:
        respuesta = random.choice(FRASES_GLAM)

    await interaction.response.send_message(f"✨ **Aryu:** {respuesta}")

@client.tree.command(name="glam", description="Pide a Aryu que evalúe el nivel de Glam del canal.")
async def glam(interaction: discord.Interaction):
    respuestas_eval = [
        "✨ **Aryu:** Siento una vibra moderadamente Glam en este chat, pero aún pueden mejorar su elegancia.",
        "✨ **Aryu:** ¡Cero Glam! Este canal necesita urgentemente una renovación de estilo.",
        "✨ **Aryu:** ¡Espléndido! La elegancia de este lugar es casi comparable con mi salto."
    ]
    await interaction.response.send_message(random.choice(respuestas_eval))

@client.event
async def on_ready():
    print(f'Bot conectado como {client.user} - ¡Aryu ha llegado con Glam!')

# Reemplaza 'TU_TOKEN_AQUI' por el token del bot de Aryu
if __name__ == "__main__":
    client.run('TU_TOKEN_AQUI')