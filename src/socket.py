import socket
import ssl
import random
import string

ASCII_CHARACTERS = string.ascii_letters + string.digits


class Socket(socket.socket):
  def __init__(self, host, port, tls=False, timeout=5) -> None:
    socket.socket.__init__(self)

    self.settimeout(timeout)
    self.connect(( host, port ))

    if tls:
      context = ssl.SSLContext(ssl._SSLMethod.PROTOCOL_TLS)
      context.load_default_certs()
      self = context.wrap_socket(self)

  def send_request(self, http_request: str) -> bool:
    ok = 0

    try:
      self.sendall(http_request.encode('utf-8'))
      ok += 1

    except socket.error:
      ok -= 1
  
    return ok > 0

  def send_bytes(self, byte_length: int) -> bool:
    ok = 0

    chars = [random.choice(ASCII_CHARACTERS) for _ in range(byte_length)]

    try:
      self.send("".join(chars).encode("utf-8"))
      ok += 1

    except socket.error:
      ok -= 1
    
    return ok > 0