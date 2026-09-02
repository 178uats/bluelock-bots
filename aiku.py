import discord
from discord.ext import commands
from discord import app_commands
import random

# Definición del cliente y árbol de comandos slash
class AikuBot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

client = AikuBot()

# --- BASE DE DATOS DE FRASES DE OLIVER AIKU (UBERS) ---
FRASES_DEFENSA = [
    "Tranquilo, chico. En esta defensa de Ubers no hay espacio para que hagas lo que quieras.",
    "El rol de un defensor adulto es apagar los sueños de los delanteros novatos. Nada personal.",
    "Puedo oler el peligro antes de que ocurra. Tu intención de ataque ya la tenía detectada.",
    "Cerrar los caminos, presionar en el momento justo y arrebatar la pelota... ese es mi juego."
]

FRASES_MADUREZ_Y_FLIRTEO = [
    "El fútbol es genial, pero no hay que olvidarse de disfrutar de la vida fuera del campo. Un buen café o una charla con chicas siempre viene bien.",
    "Ah, la juventud... tan llena de energía e impaciencia. A veces solo necesitan a un adulto experimentado que los guíe.",
    "Mantén la calma. Los mejores movimientos se hacen con la cabeza fría y una sonrisa confiada."
]

FRASES_UBERS = [
    "Snuffy nos dio un plano perfecto, pero en la línea del fondo soy yo quien ajusta las piezas en tiempo real.",
    "Con Lorenzo rompiendo el juego, Niko leyendo las líneas y Aryu en el aire, mi trabajo es ser el cerrojo final.",
    "Barou causa bastantes dolores de cabeza con su ego, pero hay que admitir que tener a ese monstruo arriba te da tranquilidad."
]

FRASES_OJOS_INTUICIÓ = [
    "Mis ojos no son solo para llamar la atención. Esta heterocromía me permite leer el campo de una forma diferente.",
    "Veo el destello en tus ojos antes de que intentes el pase. Ya es demasiado tarde."
]

# --- COMANDOS SLASH (/) ---

@client.tree.command(name="hablar", description="Habla con Oliver Aiku y recibe consejos del capitán de la defensa.")
@app_commands.describe(mensaje="Lo que quieres decirle a Aiku")
async def hablar(interaction: discord.Interaction, mensaje: str):
    msg_lower = mensaje.lower()
    
    # Lógica de respuestas basada en palabras clave
    if any(p in msg_lower for p in ["ojo", "ojos", "heterocromia", "color", "ver", "leer"]):
        respuesta = random.choice(FRASES_OJOS_INTUICIÓ)
    elif any(p in msg_lower for p in ["chica", "chicas", "cita", "fiesta", "tranquilo", "edad", "viejo"]):
        respuesta = random.choice(FRASES_MADUREZ_Y_FLIRTEO)
    elif any(p in msg_lower for p in ["defensa", "bloqueo", "sub20", "proteger", "cortar"]):
        respuesta = random.choice(FRASES_DEFENSA)
    elif any(p in msg_lower for p in ["snuffy", "barou", "niko", "lorenzo", "aryu", "ubers"]):
        respuesta = random.choice(FRASES_UBERS)
    else:
        respuesta = random.choice(FRASES_DEFENSA + FRASES_MADUREZ_Y_FLIRTEO)

    await interaction.response.send_message(f"👁️‍🗨️ **Aiku:** {respuesta}")

@client.tree.command(name="escanear", description="Pide a Aiku que escanee la defensa del canal.")
async def escanear(interaction: discord.Interaction):
    diagnosticos = [
        "👁️‍🗨️ **Aiku:** Mmm... detecto un par de huecos en la comunicación del canal, pero nada que este veterano no pueda organizar.",
        "👁️‍🗨️ **Aiku:** Cobertura perfecta. Ningún delantero pasaría por esta conversación sin ser interceptado.",
        "👁️‍🗨️ **Aiku:** Calma, muchachos. Dejen que este adulto se encargue de mantener el orden."
    ]
    await interaction.response.send_message(random.choice(diagnosticos))

@client.event
async def on_ready():
    print(f'Bot conectado como {client.user} - ¡Oliver Aiku está listo en la zaga!')

# Reemplaza 'TU_TOKEN_AQUI' por el token del bot de Aiku
if __name__ == "__main__":
    client.run('TU_TOKEN_AQUI')