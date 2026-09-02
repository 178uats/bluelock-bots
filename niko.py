import discord
from discord.ext import commands
from discord import app_commands
import random

# Definición del cliente y árbol de comandos slash
class NikoBot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

client = NikoBot()

# --- BASE DE DATOS DE FRASES DE NIKO (UBERS) ---
FRASES_EGO_OBSERVADOR = [
    "Puedo ver todo el campo. Tu siguiente movimiento ya estaba calculado en mi cabeza.",
    "Antes buscaba ser el delantero final... pero destruir los ataques del rival me genera una desesperación hermosa.",
    "Mis ojos ven la estructura del juego. No hay pase que no pueda interceptar.",
    "Snuffy me enseñó a pensar tácticamente. Ya no juego por impulso, juego por lógica.",
    "Pensaste que habías encontrado un espacio libre, pero yo ya estaba esperando ahí."
]

FRASES_VISION = [
    "Veo las líneas de pase antes de que las dibujes. Tu visión de juego es demasiado reducida.",
    "El metavisión no es solo observar, es procesar cada pieza del campo antes que los demás.",
    "Oculto mis ojos con mi flequillo, pero te aseguro que estoy viendo cada uno de tus errores."
]

FRASES_UBERS = [
    "En Ubers no improvisamos. Seguimos las estrategias de Snuffy al pie de la letra hasta sofocar al rival.",
    "El fútbol profesional es un trabajo de estrategia. Si no aportas valor táctico, no sirves.",
    "Barou puede ser el rey que remata, pero la defensa y la transición empiezan con mi lectura del juego."
]

FRASES_RIVALES = [
    "Isagi... la próxima vez seré yo quien anticipe tu metavisión y destruya tu jugada.",
    "No me importa quién sea el delantero rival, mi trabajo es volverlo invisible en la cancha."
]

# --- COMANDOS SLASH (/) ---

@client.tree.command(name="hablar", description="Habla con Ikki Niko y analiza el juego con él.")
@app_commands.describe(mensaje="Lo que quieres decirle a Niko")
async def hablar(interaction: discord.Interaction, mensaje: str):
    msg_lower = mensaje.lower()
    
    # Lógica de respuestas basada en palabras clave
    if any(p in msg_lower for p in ["ojo", "ver", "vision", "flequillo", "mirar"]):
        respuesta = random.choice(FRASES_VISION)
    elif any(p in msg_lower for p in ["ubers", "snuffy", "tactica", "estrategia", "defensa"]):
        respuesta = random.choice(FRASES_UBERS)
    elif any(p in msg_lower for p in ["isagi", "barou", "delantero", "atacar"]):
        respuesta = random.choice(FRASES_RIVALES)
    elif any(p in msg_lower for p in ["pasar", "pase", "pelota", "balon"]):
        respuesta = "Adelante, intenta dar ese pase. Te garantizo que lo interceptaré antes de que llegue a su destino."
    else:
        respuesta = random.choice(FRASES_EGO_OBSERVADOR)

    await interaction.response.send_message(f"👁️ **Niko:** {respuesta}")

@client.tree.command(name="analizar", description="Pide a Niko que analice la situación del canal.")
async def analizar(interaction: discord.Interaction):
    await interaction.response.send_message("👁️ **Niko:** He estado observando este chat... Ya detecté todos sus puntos débiles y líneas de pase.")

@client.event
async def on_ready():
    print(f'Bot conectado como {client.user} - ¡Ikki Niko está en el campo!')

# Reemplaza 'TU_TOKEN_AQUI' por el token del bot de Niko
if __name__ == "__main__":
    client.run('TU_TOKEN_AQUI')