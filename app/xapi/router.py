
from fastapi import APIRouter
from app.xapi.connect.connect import ConnectAndDisconnectServers

router = APIRouter()

@router.post("/connect-servers")
def api_connect_servers():
    connect_servers = ConnectAndDisconnectServers()
    logs = connect_servers.run()

    return {"logs": logs}