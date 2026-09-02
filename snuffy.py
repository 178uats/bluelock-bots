import discord
from discord.ext import commands
from discord import app_commands
import random

# Definición del cliente y árbol de comandos slash
class SnuffyBot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

client = SnuffyBot()

# --- BASE DE DATOS DE FRASES DE MARC SNUFFY (UBERS) ---
FRASES_PROFESIONALES = [
    "El fútbol no es solo talento e ilusión; es un trabajo. Si quieres triunfar, debes tratarlo como tal.",
    "No necesitas ser un héroe individual en cada partido. Cumple con tu función táctica y el equipo ganará.",
    "He visto a miles de 'genios' destruirse por no tener un plan de carrera. No cometas ese mismo error.",
    "Si el Plan A falla, ejecutamos el Plan B. Si el B falla, pasamos al C. En Ubers siempre tenemos un diseño para ganar.",
    "El talento te consigue el primer contrato, pero la disciplina y la estrategia te mantienen en la cima durante 10 años."
]

FRASES_MENTOR = [
    "Tu valor como ser humano no depende de si ganas o pierdes un partido de fútbol. Cuida tu mente.",
    "Apoya a tus compañeros. Cuando tu cuerpo ya no responda igual con los años, la estructura del equipo te sostendrá.",
    "¿Quieres ser un profesional? Entonces aprende a analizar tus derrotas sin dejar que destruyan tu autoestima."
]

FRASES_UBERS = [
    "Diseñé a Ubers para ser la máquina táctica más eficiente del mundo. Barou, Niko, Aryu... todos tienen su rol exacto.",
    "Barou es una fuerza salvaje, pero dentro de mi sistema, su ego se convierte en un arma letal y constante.",
    "El metavisión de Niko y la cobertura de Aryu son la base de nuestra transición defensiva."
]

FRASES_CONSEJOS = [
    "No juegues por impulso. Observa los patrones, aprende la estrategia y ejecuta sin dudar.",
    "Un verdadero profesional siempre tiene una alternativa. ¿Cuál es tu plan secundario si las cosas salen mal?"
]

# --- COMANDOS SLASH (/) ---

@client.tree.command(name="hablar", description="Habla con Marc Snuffy y recibe consejos tácticos de un veterano profesional.")
@app_commands.describe(mensaje="Lo que quieres decirle al Maestro Snuffy")
async def hablar(interaction: discord.Interaction, mensaje: str):
    msg_lower = mensaje.lower()
    
    # Lógica de respuestas basada en palabras clave
    if any(p in msg_lower for p in ["plan", "estrategia", "tactica", "sistema"]):
        respuesta = "Tener un diseño claro es la diferencia entre un aficionado y un profesional. Sigue el sistema."
    elif any(p in msg_lower for p in ["barou", "niko", "aryu", "equipo", "ubers"]):
        respuesta = random.choice(FRASES_UBERS)
    elif any(p in msg_lower for p in ["triste", "perder", "presion", "consejo", "futuro", "miedo"]):
        respuesta = random.choice(FRASES_MENTOR)
    elif any(p in msg_lower for p in ["trabajo", "dinero", "profesional", "carrera"]):
        respuesta = random.choice(FRASES_PROFESIONALES)
    else:
        respuesta = random.choice(FRASES_PROFESIONALES + FRASES_CONSEJOS)

    await interaction.response.send_message(f"📋 **Snuffy:** {respuesta}")

@client.tree.command(name="tactica", description="Pide a Snuffy un diseño táctico para el servidor.")
async def tactica(interaction: discord.Interaction):
    planes = [
        "📋 **Snuffy:** Plan A: Mantener el orden en el chat, asignar roles claros y ejecutar las reglas con precisión.",
        "📋 **Snuffy:** Plan B: Si la conversación se descontrola, aplicamos contención táctica e interceptamos el spam.",
        "📋 **Snuffy:** Recuerda: un servidor organizado no depende de la suerte, sino de la disciplina de sus miembros."
    ]
    await interaction.response.send_message(random.choice(planes))

@client.event
async def on_ready():
    print(f'Bot conectado como {client.user} - ¡Marc Snuffy está listo para dirigir!')

# Reemplaza 'TU_TOKEN_AQUI' por el token del bot de Snuffy
if __name__ == "__main__":
    client.run('TU_TOKEN_AQUI')