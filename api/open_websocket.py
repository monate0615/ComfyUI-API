import websocket #NOTE: websocket-client (https://github.com/websocket-client/websocket-client)
import uuid

from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Access the variables
server_address = os.getenv('SERVER_URL')

def open_websocket_connection():
  client_id=str(uuid.uuid4())
  ws = websocket.WebSocket()
  ws.connect("ws://{}/ws?clientId={}".format(server_address, client_id))
  return ws, server_address, client_id