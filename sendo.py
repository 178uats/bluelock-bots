import discord
from discord.ext import commands
from discord import app_commands
import random

# Definición del cliente y árbol de comandos slash
class SendoBot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

client = SendoBot()

# --- BASE DE DATOS DE FRASES DE SHUTO SENDO (UBERS) ---
FRASES_IDOLS = [
    "¡Tengo que destacar a toda costa! Si no gano millones en la Liga Sub-20, ¡¿cómo se supone que voy a casarme con una idol?!",
    "¡Mi motivación es pura y sincera! Fama, fortuna y una hermosa idol a mi lado. ¡Eso es lo único que pido!",
    "¡No me importa lo duro que sea el entrenamiento de Snuffy mientras me acerque a mi sueño de portada de revista con una idol!",
    "¿Egoísmo? ¡Mi verdadero ego es conseguir que una idol me pida un autógráfo a mí!"
]

FRASES_DRAMA_Y_DESESPERACION = [
    "¡Oigan, no me ignoren! ¡Yo también era el delantero estrella de la Sub-20 de Japón!",
    "¡¿Por qué todos en este equipo son unos monstruos?! Barou es un loco, Lorenzo parece un zombi y Snuffy nos hace trabajar como locos...",
    "¡Casi me da un ataque en el último partido! La presión en Ubers no es normal...",
    "¡Cielos, casi pierdo el balón! ¡Si cometo un error, Barou me va a devorar vivo!"
]

FRASES_TRABAJO_UBERS = [
    "Snuffy me enseñó que si no puedo ser el rematador principal, tengo que cazar los rebotes y presionar como un demente.",
    "No seré el genio del equipo, ¡pero nadie me ganará en ganas de sobrevivir en esta cancha!",
    "En Ubers aprendí a tragarme mi orgullo. Si tengo que barrerme para recuperar el balón y asistir a Barou... ¡lo haré!",
    "¡Aprovecharé cualquier oportunidad suelta en el área! Un gol de rebote vale lo mismo en el marcador."
]

FRASES_RIVALES = [
    "¡Esos chicos de Blue Lock están completamente locos! Pero no me voy a quedar atrás tan fácilmente.",
    "Aiku se lo toma muy con calma porque es popular... ¡pero yo tengo que luchar por cada segundo de atención!"
]

# --- COMANDOS SLASH (/) ---

@client.tree.command(name="hablar", description="Habla con Shuto Sendo y escucha sus ambiciosos sueños.")
@app_commands.describe(mensaje="Lo que quieres decirle a Sendo")
async def hablar(interaction: discord.Interaction, mensaje: str):
    msg_lower = mensaje.lower()
    
    # Lógica de respuestas basada en palabras clave
    if any(p in msg_lower for p in ["idol", "novia", "casar", "amor", "fama", "chica"]):
        respuesta = random.choice(FRASES_IDOLS)
    elif any(p in msg_lower for p in ["miedo", "presion", "sub20", "loco", "barou", "lorenzo"]):
        respuesta = random.choice(FRASES_DRAMA_Y_DESESPERACION)
    elif any(p in msg_lower for p in ["ubers", "snuffy", "gol", "rebote", "trabajo", "asistencia"]):
        respuesta = random.choice(FRASES_TRABAJO_UBERS)
    elif any(p in msg_lower for p in ["isagi", "blue lock", "aiku", "rival"]):
        respuesta = random.choice(FRASES_RIVALES)
    else:
        respuesta = random.choice(FRASES_IDOLS + FRASES_DRAMA_Y_DESESPERACION + FRASES_TRABAJO_UBERS)

    await interaction.response.send_message(f"⚽ **Sendo:** {respuesta}")

@client.tree.command(name="sueño", description="Pide a Sendo que te cuente su plan de vida.")
async def sueno(interaction: discord.Interaction):
    planes = [
        "⚽ **Sendo:** Plan perfecto: 1. Sobrevivir al sistema de Snuffy. 2. Marcar un gol decisivo. 3. Firmar un contrato millonario. 4. ¡Casarme con mi idol favorita!",
        "⚽ **Sendo:** ¡Solo necesito una oportunidad suelta en el área para demostrar que puedo ser una estrella!",
        "⚽ **Sendo:** ¿Crees que tengo oportunidad con una idol si llego a valer 50 millones de yenes en el mercado?"
    ]
    await interaction.response.send_message(random.choice(planes))

@client.event
async def on_ready():
    print(f'Bot conectado como {client.user} - ¡Shuto Sendo está listo para darlo todo!')

# Reemplaza 'TU_TOKEN_AQUI' por el token del bot de Sendo
if __name__ == "__main__":
    client.run('TU_TOKEN_AQUI')