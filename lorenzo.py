import discord
from discord.ext import commands
from discord import app_commands
import random

# Definición del cliente y árbol de comandos slash
class LorenzoBot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

client = LorenzoBot()

# --- BASE DE DATOS DE FRASES DE DON LORENZO (UBERS) ---
FRASES_DINERO = [
    "¿Dinero? ¡El dinero lo es todo en esta vida, amigo! Si no hay un buen contrato de por medio, ni me muevo.",
    "Todo en este mundo tiene un precio. ¿Cuánto vale tu estrella principal? Yo la borro del campo por la cifra correcta.",
    "Mis dientes de oro no son solo para deslumbrar, son el recordatorio de que pasé de no tener nada a valer millones.",
    "Snuffy me salvó la vida y me enseñó que el fútbol es un negocio. ¡Y a mí me encantan los negocios jugosos!",
    "Si juegas gratis, estás regalando tu trabajo. ¡Asegura esa bolsa de dinero primero!"
]

FRASES_ESTILO_ZOMBI = [
    "¿Mi forma de moverme? Jeje, es el regate zombi. Movimientos impredecibles que rompen cualquier postura.",
    "No intenten adivinar hacia dónde iré. Ni yo mismo lo sé hasta que mis piernas sueltas lo deciden.",
    "Parece que me voy a caer, ¿verdad? ¡Error! Así es exactamente como rompo tu defensa.",
    "En cuanto la estrella rival recibe el balón... ¡chas! Aparezco de la nada para devorarla."
]

FRASES_UBERS = [
    "Barou es un tipo divertido. Un rey ruidoso, pero mientras meta goles y suba el valor del equipo, me cae bien.",
    "Snuffy es el jefe absoluto. Sin sus contratos y sus ideas, yo seguiría comiendo basura en la calle.",
    "Niko y Aryu hacen el trabajo sucio atrás mientras yo me encargo de anular a la amenaza principal."
]

FRASES_RIVALES = [
    "Kaiser... ese tipo cree que vale mucho, pero en este partido lo tengo metido en mi bolsillo.",
    "Isagi Yoichi... tu valor de mercado está subiendo, ¿eh? Eso te convierte en una presa muy apetitosa para devorar."
]

# --- COMANDOS SLASH (/) ---

@client.tree.command(name="hablar", description="Habla con Don Lorenzo y negocia tu valor en el mercado.")
@app_commands.describe(mensaje="Lo que quieres decirle a Lorenzo")
async def hablar(interaction: discord.Interaction, mensaje: str):
    msg_lower = mensaje.lower()
    
    # Lógica de respuestas basada en palabras clave
    if any(p in msg_lower for p in ["dinero", "plata", "oro", "contrato", "comprar", "precio", "cuanto"]):
        respuesta = random.choice(FRASES_DINERO)
    elif any(p in msg_lower for p in ["zombi", "mover", "regate", "defensa", "caer"]):
        respuesta = random.choice(FRASES_ESTILO_ZOMBI)
    elif any(p in msg_lower for p in ["snuffy", "barou", "kaiser", "isagi", "ubers"]):
        respuesta = random.choice(FRASES_UBERS + FRASES_RIVALES)
    else:
        respuesta = random.choice(FRASES_DINERO + FRASES_ESTILO_ZOMBI)

    await interaction.response.send_message(f"🦷 **Lorenzo:** {respuesta}")

@client.tree.command(name="cotizar", description="Pide a Lorenzo que evalúe el valor financiero del servidor.")
async def cotizar(interaction: discord.Interaction):
    cotizaciones = [
        "🦷 **Lorenzo:** Mmm... este canal vale unos 50 millones de yenes. ¡Nada mal, pero podemos sacarle más si apretamos!",
        "🦷 **Lorenzo:** ¡Bah! Este chat no vale ni una moneda de diez centavos. ¡Necesitamos estrellas que generen ingresos!",
        "🦷 **Lorenzo:** ¡Negocio redondo! El valor de mercado de este servidor acaba de dispararse."
    ]
    await interaction.response.send_message(random.choice(cotizaciones))

@client.event
async def on_ready():
    print(f'Bot conectado como {client.user} - ¡Don Lorenzo está listo para los negocios!')

# Reemplaza 'TU_TOKEN_AQUI' por el token del bot de Lorenzo
if __name__ == "__main__":
    client.run('TU_TOKEN_AQUI')