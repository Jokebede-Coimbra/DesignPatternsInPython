from adapter import Adapter
from usa_socket import USASocket


usa_socket_instance = USASocket()
adapter_instance = Adapter(usa_socket_instance)

result = adapter_instance.plug_in()
print(result)
