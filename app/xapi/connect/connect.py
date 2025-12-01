import grpc
from app.xapi.connect import utilities_pb2 as util
from app.xapi.connect import utilities_pb2_grpc as util_grpc
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
pem_path = os.path.join(BASE_DIR, "roots.pem")

servers = ['njxapi.taltrade.com','chixapi.taltrade.com']


class ConnectAndDisconnectServers:
    def __init__(self):
        self.user = 'PSXAPI03'
        self.domain = 'XAPITEST'
        self.password = 'ezesoft1'
        self.locale = 'Global Americas'
        self.port = '9000'
    
    def run(self):
        logs = []

        with open(pem_path, "rb") as f:
            pem_data = f.read()
        
        for server in servers:
            channel = grpc.secure_channel(
                f'{server}:{self.port}',
                grpc.ssl_channel_credentials(root_certificates=pem_data)
            )

            util_stub = util_grpc.UtilityServicesStub(channel)
            connect_request = util.ConnectRequest(
                UserName=self.user,
                Domain=self.domain,
                Password=self.password,
                Locale=self.locale
            )
            connect_response = util_stub.Connect(connect_request)
            logs.append(f'Connect result to {server}: {connect_response.Response}')

            if connect_response.Response == 'success':
                disconnect_response = util_stub.Disconnect(util.DisconnectRequest(UserToken=connect_response.UserToken))
                logs.append(f'Disconnect result from {server}: {disconnect_response.ServerResponse}')

        print(logs)
        return logs

