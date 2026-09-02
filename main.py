import asyncio
import os

# --- IMPORTACIÓN DE LOS CLIENTES DESDE CADA ARCHIVO ---
# Asegúrate de que los archivos .py estén en la misma carpeta que main.py
from barou import client as client_barou
from niko import client as client_niko
from aryu import client as client_aryu
from snuffy import client as client_snuffy
from lorenzo import client as client_lorenzo
from aiku import client as client_aiku
from sendo import client as client_sendo
from yukio import client as client_yukio
from nagi import client as client_nagi
from reo import client as client_reo
from chris import client as client_chris
from charles import client as client_charles
from shidou import client as client_shidou
from ego import client as client_ego

# --- DICCIONARIO DE TOKENS DE CADA BOT ---
# Carga los tokens desde las variables de entorno de la nube o usa un texto vacío por defecto
TOKENS = {
    'barou': os.getenv('TOKEN_BAROU', ''),
    'niko': os.getenv('TOKEN_NIKO', ''),
    'aryu': os.getenv('TOKEN_ARYU', ''),
    'snuffy': os.getenv('TOKEN_SNUFFY', ''),
    'lorenzo': os.getenv('TOKEN_LORENZO', ''),
    'aiku': os.getenv('TOKEN_AIKU', ''),
    'sendo': os.getenv('TOKEN_SENDO', ''),
    'yukio': os.getenv('TOKEN_YUKIO', ''),
    'nagi': os.getenv('TOKEN_NAGI', ''),
    'reo': os.getenv('TOKEN_REO', ''),
    'chris': os.getenv('TOKEN_CHRIS', ''),
    'charles': os.getenv('TOKEN_CHARLES', ''),
    'shidou': os.getenv('TOKEN_SHIDOU', ''),
    'ego': os.getenv('TOKEN_EGO', '')
}

# --- FUNCIÓN DE ARRANQUE CONCURRENTE ---

async def main():
    # Se genera la lista de tareas para iniciar todos los bots al mismo tiempo
    tasks = [
        client_barou.start(TOKENS['barou']),
        client_niko.start(TOKENS['niko']),
        client_aryu.start(TOKENS['aryu']),
        client_snuffy.start(TOKENS['snuffy']),
        client_lorenzo.start(TOKENS['lorenzo']),
        client_aiku.start(TOKENS['aiku']),
        client_sendo.start(TOKENS['sendo']),
        client_yukio.start(TOKENS['yukio']),
        client_nagi.start(TOKENS['nagi']),
        client_reo.start(TOKENS['reo']),
        client_chris.start(TOKENS['chris']),
        client_charles.start(TOKENS['charles']),
        client_shidou.start(TOKENS['shidou']),
        client_ego.start(TOKENS['ego'])
    ]
    
    print("🚀 Encendiendo todos los bots de Blue Lock simultáneamente...")
    
    # asyncio.gather ejecuta las corrutinas en paralelo dentro del mismo proceso
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n🛑 Apagando la conexión de todos los bots...")