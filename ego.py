import discord
from discord import app_commands
import random

# Definición del cliente y árbol de comandos slash
class EgoBot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

client = EgoBot()

# --- FRASES DE JINPACHI EGO ---
FRASES_EGOISMO = [
    " *(Sorbiendo fideos instantáneos)* Bienvenidos, no-talentos. El fútbol no se trata de cooperación tibia, sino de aplastar a los demás con tu propio ego.",
    " ¿Saben cuál es el mejor delantero del mundo? El que puede declarar en la cancha: 'Solo mis goles importan'. Todo lo demás es mediocridad.",
    " Dejen de buscar la aprobación de los demás. El verdadero ego nace cuando estás dispuesto a desesperarte para renacer.",
    " Si no tienen la capacidad de crear una fórmula para sus propios goles, no son más que piezas reemplazables en mi tablero."
]

FRASES_TALENTO = [
    " *(Ajustándose los lentes)* El talento no es algo que nace por gracia divina. Es la capacidad de demostrar que tu ego tiene razón ante el resto del mundo.",
    " Una flor que florece en la comodidad nunca sobrevivirá al infierno de Blue Lock. Si no arriesgas tu orgullo, nunca descubrirás de qué eres capaz.",
    " *(Mirando fijamente la pantalla)* ¿Creen que un genio nace siendo genio? Un genio es solo alguien que se negó a aceptar sus propios límites antes que los demás.",
    " Quien espera una oportunidad es un mediocre. El verdadero delantero crea su propia oportunidad aplastando la suerte de los demás."
]

FRASES_DEVORAR = [
    " *(Sonrisa gélida)* En esta cancha no existen los compañeros de equipo, solo presas y depredadores. Si no devoras al de al lado, serás digerido.",
    " No vinieron aquí a hacer amigos ni a construir recuerdos felices. Vinieron a devorar los sueños de otros 299 futbolistas para alimentar el suyo.",
    " *(Cruzando los brazos)* Para evolucionar debes destruir la versión de ti que te trajo hasta aquí. Devora tu viejo 'yo' o quédate en la basura.",
    " Cuando estés acorralado, no mires a tus lados buscando ayuda. Mira dentro de ti y pregúntate qué parte de tu rival vas a devorar para ganar."
]

FRASES_DESESPERACION = [
    " La desesperación no es el fin; es el ingrediente principal para el despertar de un egoísta. Bienvenidos al abismo.",
    " *(Tecleando en la computadora)* Quien teme perder la comodidad de su vida actual jamás podrá alcanzar el número uno del mundo.",
    " El dolor de la derrota es la única medicina que cura la ilusión del talento no trabajado. Si van a llorar, háganlo afuera.",
    " Solo cuando pierdes todo lo que te sostenía descubres la verdadera forma de tu ego. La desesperación es la incubadora de los héroes."
]

FRASES_FLOW = [
    " El 'Flow' no es magia ni suerte. Es el estado mental donde el miedo a fallar se extingue ante la obsesión de anotar.",
    " *(Apoyando la barbilla en las manos)* Si el desafío que enfrentas no te infunde un terror absoluto, no vas a lograr superar tus límites.",
    " Sumérjanse en la hiperconcentración. Dejen que el instinto tome el control y olviden cualquier pensamiento que no sea el gol.",
    " Entrar en el Flow exige una sola cosa: tirar a la basura todo lo que no sea tu deseo incontrolable de ganar."
]

FRASES_VICTORIA = [
    " ¿Celebran un pase correcto? Qué patético. La única métrica de valor en esta cancha es la pelota atravesando la red.",
    " *(Sorbiendo fideos)* No me interesan sus partidos empatados ni sus derrotas con 'honor'. El fútbol solo recuerda a quien reclamó la victoria.",
    " Ganar por suerte es el veneno más peligroso para un atleta. Si no puedes replicar tu victoria con una fórmula, tu triunfo es una casualidad inútil.",
    " Al final de este experimento, solo uno quedará en pie. El resto será el abono sobre el cual florecerá el mejor delantero del mundo."
]

# --- COMANDOS SLASH ---

@client.tree.command(name="hablar", description="Escucha la filosofía de Jinpachi Ego.")
@app_commands.describe(mensaje="Lo que quieres decirle a Ego")
async def hablar(interaction: discord.Interaction, mensaje: str):
    msg_lower = mensaje.lower()
    
    if any(p in msg_lower for p in ["talento", "genio", "limite", "potencial", "esfuerzo"]):
        respuesta = random.choice(FRASES_TALENTO)
    elif any(p in msg_lower for p in ["equipo", "amigos", "pasar", "compañero", "devorar", "rival"]):
        respuesta = random.choice(FRASES_DEVORAR)
    elif any(p in msg_lower for p in ["perder", "derrota", "miedo", "fracaso", "llorar", "imposible"]):
        respuesta = random.choice(FRASES_DESESPERACION)
    elif any(p in msg_lower for p in ["flow", "concentracion", "instinto", "fórmula", "obsesion"]):
        respuesta = random.choice(FRASES_FLOW)
    elif any(p in msg_lower for p in ["ganar", "gol", "puntos", "victoria", "campeon", "numero 1"]):
        respuesta = random.choice(FRASES_VICTORIA)
    else:
        respuesta = random.choice(FRASES_EGOISMO + FRASES_DESESPERACION)

    await interaction.response.send_message(f"👓 **Ego:** {respuesta}")

@client.tree.command(name="evaluar", description="Pide a Ego que evalúe el nivel de ego del canal.")
async def evaluar(interaction: discord.Interaction):
    EVALUACIONES = [
        " Veo que siguen perdiendo el tiempo charlando en lugar de crear su propia revolución en el campo.",
        " Inútiles... Ninguno de ustedes ha entendido aún la esencia de devorar al rival.",
        " Interesante reacción química, pero aún les falta esa chispa de desesperación para ser mundiales."
    ]
    await interaction.response.send_message(f"👓 **Ego:** {random.choice(EVALUACIONES)}")

@client.tree.command(name="analizar_historial", description="Pide a Ego que lea el historial del chat (incluyendo otros bots) y dé su veredicto.")
@app_commands.describe(limite="Cantidad de mensajes pasados a leer (por defecto 50)")
async def analizar_historial(interaction: discord.Interaction, limite: int = 50):
    await interaction.response.defer()
    
    mensajes_leidos = []
    # Lee los mensajes del canal incluyendo a otros bots, excluyendo solo a sí mismo
    async for msg in interaction.channel.history(limit=limite):
        if msg.author != client.user and msg.content.strip():
            mensajes_leidos.append(f"{msg.author.name}: {msg.content}")

    total = len(mensajes_leidos)
    
    if total > 0:
        veredictos = [
            f" *(Sorbiendo fideos)* He analizado {total} mensajes de este canal (incluyendo a sus inteligencias artificiales)... La concentración de cooperación tibia y mediocridad aquí es alarmante.",
            f" Revisé {total} mensajes entre usuarios y bots. No veo más que piezas reemplazables buscando aprobación mutua. Ninguno ha demostrado un gramo de verdadero ego.",
            f" Tras examinar los últimos {total} mensajes del chat, el diagnóstico es claro: falta de instinto asesino. Si jugaran como escriben, ya habrían sido eliminados de Blue Lock."
        ]
        respuesta = random.choice(veredictos)
    else:
        respuesta = "👓 **Ego:** El historial está completamente vacío de talento. Ni siquiera han intentado mostrar su ego en este canal."

    await interaction.followup.send(respuesta)

# --- ESCUCHA DE MENSAJES ---

@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return

    contenido = message.content.lower()
    if any(palabra in contenido for palabra in ["ego", "blue lock", "futbol", "talento"]):
        if random.random() < 0.3:
            await message.channel.send(f"👓 **Ego:** {random.choice(FRASES_EGOISMO)}")

@client.event
async def on_ready():
    print(f'Bot conectado como {client.user} - ¡Jinpachi Ego está observando desde la sala de control!')

# Reemplaza 'TU_TOKEN_AQUI' por el token del bot
if __name__ == "__main__":
    client.run('TU_TOKEN_AQUI')