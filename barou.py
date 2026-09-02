import discord
from discord.ext import commands
from discord import app_commands
import random

# Definición del cliente y árbol de comandos de barra diagonal (Slash Commands)
class BarouBot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        # Sincroniza los comandos slash con Discord
        await self.tree.sync()

client = BarouBot()

# --- BASE DE DATOS DE FRASES DE BAROU (UBERS) ---
FRASES_EGO = [
    "No soy la pieza de nadie. En Ubers o donde sea, ¡yo soy el Rey!",
    "¿Escenas de táctica? ¿Estrategia de Snuffy? Me da igual. Yo solo existo para devorarlos a todos en el campo.",
    "No me pidas que pase el balón. Si quieres la pelota, ¡quítamela si puedes, basura!",
    "Snuffy me dio un sistema, pero yo lo convertí en mi propio reino. Mi gol es lo único que importa.",
    "No te confundas. No sigo las reglas del equipo, el equipo existe para que yo remate."
]

FRASES_LIMPIEZA = [
    "¿Has visto cómo tienes este servidor? Está lleno de desorden. ¡Limpia tu desastre ahora mismo, pedazo de basura!",
    "No puedo concentrarme si las cosas no están perfectas. Ordena tus ideas y tu canal antes de hablarme.",
    "El orden en el campo empieza por la disciplina personal. Si no puedes mantener tu entorno limpio, eres un mediocre.",
    "¡Limpia eso! No tolero la suciedad ni a la gente desorganizada."
]

FRASES_ENTRENAMIENTO = [
    "La rutina no miente. Si no sigues tu entrenamiento al 100% cada día, no eres más que un talento malgastado.",
    "Snuffy dice que el fútbol es un trabajo... pues yo soy el empleado más dominante de esta fábrica.",
    "Despertar, entrenar, perfeccionar el tiro con rosca, dominar. Si te saltas un paso, estás fuera."
]

FRASES_INSULTOS = [
    "Cállate, burro (Donkey).",
    "¿Le hablas al Rey como si fueras su igual? Vuelve a tu posición, extra.",
    "No estorbes en mi camino hacia el gol.",
    "Eres solo una pieza secundaria en mi historia. Apártate."
]

# --- COMANDOS SLASH (/) ---

@client.tree.command(name="hablar", description="Habla con Shoei Barou y recibe sus sabios (y agresivos) comentarios.")
@app_commands.describe(mensaje="Lo que quieres decirle al Rey Barou")
async def hablar(interaction: discord.Interaction, mensaje: str):
    msg_lower = mensaje.lower()
    
    # Lógica de respuestas basada en palabras clave
    if any(p in msg_lower for p in ["limpiar", "desorden", "sucio", "orden"]):
        respuesta = random.choice(FRASES_LIMPIEZA)
    elif any(p in msg_lower for p in ["entrenar", "rutina", "ubers", "snuffy", "ejercicio"]):
        respuesta = random.choice(FRASES_ENTRENAMIENTO)
    elif any(p in msg_lower for p in ["pasar", "equipo", "pase", "ayuda"]):
        respuesta = "¡¿Pasar?! ¡El balón es mío! ¡Yo soy el centro del universo en esta cancha!"
    elif any(p in msg_lower for p in ["isagi", "yoichi"]):
        respuesta = "¡No me menciones a ese maldito adaptativo! Lo devoraré la próxima vez que nos crucemos."
    else:
        # Si no detecta palabra clave, responde con una frase de rey/ego o un insulto
        respuesta = random.choice(FRASES_EGO + FRASES_INSULTOS)

    await interaction.response.send_message(f"👑 **Barou:** {respuesta}")

@client.tree.command(name="ordenar", description="Exige que Barou ponga orden en el canal.")
async def ordenar(interaction: discord.Interaction):
    await interaction.response.send_message("👑 **Barou:** ¡Todo este canal es un asco! Empiecen a limpiar o los barreré a todos del servidor.")

@client.event
async def on_ready():
    print(f'Bot conectado como {client.user} - ¡El Rey Barou ha llegado!')

# Reemplaza 'TU_TOKEN_AQUI' por el token de tu bot de Discord
if __name__ == "__main__":
    client.run('TU_TOKEN_AQUI')