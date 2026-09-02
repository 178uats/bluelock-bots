import discord
from discord.ext import commands
from discord import app_commands
import random

# Definición del cliente y árbol de comandos slash
class YukioBot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

client = YukioBot()

# --- BASE DE DATOS DE FRASES DE YUKIO ISHIKARI (UBERS) ---
FRASES_ALTURA = [
    "Desde aquí arriba el juego se ve bastante claro. Mis dos metros de altura no son solo adorno.",
    "El aire es mi territorio. Si intentan un balón alto contra Ubers, lo despejaré antes de que toque el suelo.",
    "En Blue Lock todos buscan ser los más rápidos o habilidosos, pero la física y la envergadura no se pueden entrenar así como así.",
    "¿Que si es difícil encontrar ropa de mi talla? Bastante... pero en la cancha mi altura es mi mayor virtud."
]

FRASES_UBERS_TACTICA = [
    "Snuffy sabe exactamente cómo usar mi estatura dentro de las jugadas a balón parado.",
    "Aryu tiene el salto y la elegancia, pero yo aporto la pared física inamovible en el área.",
    "En la defensa de Ubers no necesitamos adivinar; si bloqueamos los ángulos aéreos, obligamos al rival a jugar por abajo donde Aiku y Niko los esperan.",
    "Cumplo mi rol en la estrategia. Un verdadero profesional sabe usar sus fortalezas naturales para el equipo."
]

FRASES_RIVALES = [
    "No me importa qué tan rápido sea el delantero rival, no puede saltar por encima de mi alcance.",
    "Isagi y los demás delanteros de Blue Lock son peligrosos por abajo, pero por arriba la ventaja es completamente mía."
]

# --- COMANDOS SLASH (/) ---

@client.tree.command(name="hablar", description="Habla con Yukio Ishikari, el gigante de Ubers.")
@app_commands.describe(mensaje="Lo que quieres decirle a Yukio")
async def hablar(interaction: discord.Interaction, mensaje: str):
    msg_lower = mensaje.lower()
    
    # Lógica de respuestas basada en palabras clave
    if any(p in msg_lower for p in ["alto", "altura", "metro", "gigante", "tamaño", "cabeza"]):
        respuesta = random.choice(FRASES_ALTURA)
    elif any(p in msg_lower for p in ["ubers", "snuffy", "defensa", "aryu", "aiku", "balon", "centro"]):
        respuesta = random.choice(FRASES_UBERS_TACTICA)
    elif any(p in msg_lower for p in ["blue lock", "isagi", "rival", "delantero"]):
        respuesta = random.choice(FRASES_RIVALES)
    else:
        respuesta = random.choice(FRASES_ALTURA + FRASES_UBERS_TACTICA)

    await interaction.response.send_message(f"📏 **Yukio:** {respuesta}")

@client.tree.command(name="estatura", description="Pide a Yukio que mida el control aéreo del chat.")
async def estatura(interaction: discord.Interaction):
    respuestas = [
        "📏 **Yukio:** Veo todo este canal desde arriba. Nadie va a ganar un balón dividido por aquí.",
        "📏 **Yukio:** Dominio aéreo total. La defensa de Ubers mantiene el control.",
        "📏 **Yukio:** Un poco más de altura en sus pases y quizás tendrían una oportunidad..."
    ]
    await interaction.response.send_message(random.choice(respuestas))

@client.event
async def on_ready():
    print(f'Bot conectado como {client.user} - ¡Yukio Ishikari está en el campo!')

# Reemplaza 'TU_TOKEN_AQUI' por el token del bot de Yukio
if __name__ == "__main__":
    client.run('TU_TOKEN_AQUI')