import discord
from discord.ext import commands
from discord import app_commands
import random

# Definición del cliente y árbol de comandos slash
class NagiBot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

client = NagiBot()

# --- BASE DE DATOS DE FRASES DE SEISHIRO NAGI (MANSHINE CITY) ---
FRASES_PEREZA = [
    "Uf... responder este mensaje es tan fastidioso (*mendokusai*)... Prefiero acostarme a jugar en el celular.",
    "¿Entrenar otra vez? Chris Prince me hace hacer demasiado ejercicio... mis músculos están cansados.",
    "Si pudiera ganar la copa del mundo sin levantarme de la cama, sería perfecto.",
    "Ah... qué flojera. Reo, ¿puedes llevarme en la espalda hasta la cancha?",
    "No entiendo por qué la gente se esfuerza tanto. Solo atrapas el balón y lo metes al arco, ¿no?"
]

FRASES_MANSHINE_Y_CONTROL = [
    "En Manshine City desarrollé un cuerpo capaz de responder a cualquier atrapada imposible.",
    "Chris Prince dice que debo entrenar mi físico para respaldar mi talento natural... supongo que tiene razón.",
    "No importa cómo me pases el balón, lo voy a amortiguar con absoluta precisión. Mi control es perfecto.",
    "Aquel tiro de cinco voleas consecutivas contra Bastard Munchen... fue divertido, pero agotador."
]

FRASES_REO_Y_ISAGI = [
    "Reo siempre está pensando en estrategias raras... yo solo sigo sus pases porque son cómodos.",
    "Isagi me dio ganas de probar lo que se siente ganar por mi propia cuenta... aunque igual sigue siendo agotador.",
    "Quería vencer a Isagi para probar mi propio ego, pero ahora que lo hice... ¿qué se supone que deba hacer?"
]

FRASES_GAMING = [
    "Oye, ¿no juegas a nada? El fútbol está bien, pero los videojuegos no te hacen sudar tanto.",
    "Déjame terminar esta partida de celular y luego jugamos al fútbol..."
]

# --- COMANDOS SLASH (/) ---

@client.tree.command(name="hablar", description="Habla con Seishiro Nagi de Manshine City.")
@app_commands.describe(mensaje="Lo que quieres decirle a Nagi")
async def hablar(interaction: discord.Interaction, mensaje: str):
    msg_lower = mensaje.lower()
    
    # Lógica de respuestas basada en palabras clave
    if any(p in msg_lower for p in ["juego", "celular", "gamer", "jugar", "dormir", "flojera", "cansa"]):
        respuesta = random.choice(FRASES_PEREZA + FRASES_GAMING)
    elif any(p in msg_lower for p in ["manshine", "chris", "prince", "control", "atracar", "fisico", "trampa"]):
        respuesta = random.choice(FRASES_MANSHINE_Y_CONTROL)
    elif any(p in msg_lower for p in ["reo", "isagi", "ego", "vencer", "equipo"]):
        respuesta = random.choice(FRASES_REO_Y_ISAGI)
    else:
        respuesta = random.choice(FRASES_PEREZA + FRASES_MANSHINE_Y_CONTROL)

    await interaction.response.send_message(f"🎮 **Nagi:** {respuesta}")

@client.tree.command(name="flojera", description="Pregúntale a Nagi si tiene ganas de hacer algo.")
async def flojera(interaction: discord.Interaction):
    respuestas_pereza = [
        "🎮 **Nagi:** Qué fastidio... 99% de probabilidades de que me quede acostado todo el día.",
        "🎮 **Nagi:** Si Reo no me lleva en hombros, no me muevo de aquí.",
        "🎮 **Nagi:** Solo si me das un refresco y me dejas jugar con el teléfono."
    ]
    await interaction.response.send_message(random.choice(respuestas_pereza))

@client.event
async def on_ready():
    print(f'Bot conectado como {client.user} - ¡Nagi está en el campo (con sueño)!')

# Reemplaza 'TU_TOKEN_AQUI' por el token del bot de Nagi
if __name__ == "__main__":
    client.run('TU_TOKEN_AQUI')