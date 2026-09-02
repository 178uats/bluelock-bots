import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import asyncio
import threading

# Importamos los clientes desde tus archivos individuales
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

# --- TOKENS LEÍDOS DE FORMA SEGURA ---
# Si ejecutas en local sin variables, usa el valor por defecto
TOKENS = {
    'barou': os.getenv('TOKEN_BAROU', 'TU_TOKEN_BAROU_LOCAL'),
    'niko': os.getenv('TOKEN_NIKO', 'TU_TOKEN_NIKO_LOCAL'),
    'aryu': os.getenv('TOKEN_ARYU', 'TU_TOKEN_ARYU_LOCAL'),
    'snuffy': os.getenv('TOKEN_SNUFFY', 'TU_TOKEN_SNUFFY_LOCAL'),
    'lorenzo': os.getenv('TOKEN_LORENZO', 'TU_TOKEN_LORENZO_LOCAL'),
    'aiku': os.getenv('TOKEN_AIKU', 'TU_TOKEN_AIKU_LOCAL'),
    'sendo': os.getenv('TOKEN_SENDO', 'TU_TOKEN_SENDO_LOCAL'),
    'yukio': os.getenv('TOKEN_YUKIO', 'TU_TOKEN_YUKIO_LOCAL'),
    'nagi': os.getenv('TOKEN_NAGI', 'TU_TOKEN_NAGI_LOCAL'),
    'reo': os.getenv('TOKEN_REO', 'TU_TOKEN_REO_LOCAL'),
    'chris': os.getenv('TOKEN_CHRIS', 'TU_TOKEN_CHRIS_LOCAL'),
    'charles': os.getenv('TOKEN_CHARLES', 'TU_TOKEN_CHARLES_LOCAL'),
    'shidou': os.getenv('TOKEN_SHIDOU', 'TU_TOKEN_SHIDOU_LOCAL'),
    'ego': os.getenv('TOKEN_EGO', 'TU_TOKEN_EGO_LOCAL')
}

CLIENT_MAP = {
    'barou': (client_barou, TOKENS['barou']),
    'niko': (client_niko, TOKENS['niko']),
    'aryu': (client_aryu, TOKENS['aryu']),
    'snuffy': (client_snuffy, TOKENS['snuffy']),
    'lorenzo': (client_lorenzo, TOKENS['lorenzo']),
    'aiku': (client_aiku, TOKENS['aiku']),
    'sendo': (client_sendo, TOKENS['sendo']),
    'yukio': (client_yukio, TOKENS['yukio']),
    'nagi': (client_nagi, TOKENS['nagi']),
    'reo': (client_reo, TOKENS['reo']),
    'chris': (client_chris, TOKENS['chris']),
    'charles': (client_charles, TOKENS['charles']),
    'shidou': (client_shidou, TOKENS['shidou']),
    'ego': (client_ego, TOKENS['ego'])
}

active_tasks = {}
loop = None

def run_async_loop():
    global loop
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_forever()

threading.Thread(target=run_async_loop, daemon=True).start()

class RequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.end_headers()

    def do_OPTIONS(self):
        self._set_headers()

    def do_POST(self):
        global loop, active_tasks
        if self.path == '/api/status':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))

            for bot_id, is_active in data.items():
                if bot_id in CLIENT_MAP:
                    client, token = CLIENT_MAP[bot_id]

                    if is_active and bot_id not in active_tasks:
                        if loop and loop.is_running():
                            print(f"⚡ Encendiendo bot: {bot_id}")
                            task = asyncio.run_coroutine_threadsafe(client.start(token), loop)
                            active_tasks[bot_id] = task

                    elif not is_active and bot_id in active_tasks:
                        print(f"🛑 Apagando bot: {bot_id}")
                        asyncio.run_coroutine_threadsafe(client.close(), loop)
                        del active_tasks[bot_id]

            self._set_headers()
            response = json.dumps({"status": "ok", "active": list(active_tasks.keys())})
            self.wfile.write(response.encode('utf-8'))

    def log_message(self, format, *args):
        return

if __name__ == '__main__':
    server_address = ('', 5000)
    httpd = HTTPServer(server_address, RequestHandler)
    print("🌐 Servidor Puente Activo en http://localhost:5000")
    print("Pon los tokens reales en el diccionario TOKENS y usa index.html para activar los bots.")
    httpd.serve_forever()