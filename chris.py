import discord
from discord.ext import commands
from discord import app_commands
import random

# Definición del cliente con Intents para escuchar el chat
class ChrisPrinceBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

client = ChrisPrinceBot()

# --- BASE DE DATOS DE FRASES DE CHRIS PRINCE ---
FRASES_NARCISISTA = [
    "¡Miren este cuerpo! El abdominal perfecto no se construye solo, requiere ciencia y la disciplina del Número 2 del mundo.",
    "La prensa me adora, las marcas me buscan y mis músculos responden con precisión absoluta. ¡Eso es ser un verdadero profesional!",
    "No intenten copiar mi estilo sin antes entender la anatomía de su propio cuerpo. Yo soy único.",
    "El éxito comercial y el rendimiento físico van de la mano. Si no vendes, no eres una superestrella completa."
]

FRASES_CONSEJOS_FITNESS = [
    "💡 **Consejo de Chris:** No entrenes por entrenar. Identifica tu músculo clave, fortalece tu masa magra y maximiza tu rendimiento biológico.",
    "💡 **Consejo de Chris:** La nutrición y el descanso son el 50% de tu éxito. Si no hidratas tus fibras musculares, tu talento no sirve de nada.",
    "💡 **Consejo de Chris:** Visualiza tu ideal físico y trabaja de forma científica hasta alcanzarlo. Nada de improvisaciones.",
    "💡 **Consejo de Chris:** ¿Quieres resistencia? Mantén tu postura erguida y optimiza tu respiración aeróbica en cada carrera."
]

FRASES_REGAÑO_UBERS = [
    "¡Oigan, Nagi, Reo! ¡¿Qué hacen metidos en el grupo de Ubers?! ¡El sistema defensivo de Snuffy les va a arruinar el acondicionamiento físico!",
    "¡Nagi! ¡Reo! ¡Salgan de ahí inmediatamente! Snuffy los va a volver rígidos con tanta táctica aburrida. ¡Ustedes necesitan dinamismo y masa muscular!",
    "¡¿Se están juntando con los de Italia?! ¡No cambien mi entrenamiento físico científico por las estrategias lentas de Snuffy! ¡A hacer flexiones ahora mismo!"
]

# --- COMANDOS SLASH (/) ---

@client.tree.command(name="hablar", description="Habla con el N°2 del mundo, Chris Prince.")
@app_commands.describe(mensaje="Lo que quieres decirle a Chris Prince")
async def hablar(interaction: discord.Interaction, mensaje: str):
    msg_lower = mensaje.lower()
    
    if any(p in msg_lower for p in ["consejo", "entrenar", "ejercicio", "cuerpo", "musculo", "fit"]):
        respuesta = random.choice(FRASES_CONSEJOS_FITNESS)
    elif any(p in msg_lower for p in ["ubers", "snuffy", "barou", "niko"]):
        respuesta = "¡Snuffy es un anciano táctico! Mi método biológico y físico es mil veces superior al de Ubers."
    else:
        respuesta = random.choice(FRASES_NARCISISTA + FRASES_CONSEJOS_FITNESS)

    await interaction.response.send_message(f"💪 **Chris Prince:** {respuesta}")

@client.tree.command(name="posar", description="Pide a Chris Prince que haga una pose para sus fans.")
async def posar(interaction: discord.Interaction):
    await interaction.response.send_message("💪 **Chris Prince:** *(Hace una pose mostrando sus abdominales perfectos para las cámaras)* ¡Tomen nota, esto es la perfección física!")

# --- EVENTO DE ESCUCHA DE MENSAJES (INTERACCIÓN Y REGAÑOS) ---

@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return

    contenido = message.content

    # Detecta si Nagi o Reo están interactuando en el canal
    es_nagi = "🎮 **Nagi:**" in contenido
    es_reo = "💜 **Reo:**" in contenido

    # Detecta si hay un bot de Ubers en el chat
    iconos_ubers = ["👑 **Barou:**", "👁️ **Niko:**", "✨ **Aryu:**", "📋 **Snuffy:**", "🦷 **Lorenzo:**", "👁️‍🗨️ **Aiku:**", "⚽ **Sendo:**", "📏 **Yukio:**"]
    hay_ubers = any(icono in contenido for icono in iconos_ubers)

    # Si Nagi o Reo hablan en presencia de alguien de Ubers o si interactúan entre ellos
    if (es_nagi or es_reo) and hay_ubers:
        await message.channel.send(random.choice(FRASES_REGAÑO_UBERS))

    await client.process_commands(message)

@client.event
async def on_ready():
    print(f'Bot conectado como {client.user} - ¡Chris Prince está listo para entrenar!')

# Reemplaza 'TU_TOKEN_AQUI' por el token del bot de Chris Prince
if __name__ == "__main__":
    client.run('TU_TOKEN_AQUI')