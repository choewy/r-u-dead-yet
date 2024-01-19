from werkzeug.serving import WSGIRequestHandler
from flask import Flask, Blueprint
from typing_extensions import List


class Application(Flask):
  def __init__(self, port: int, host: str, debug: bool = True):
    Flask.__init__(self, __name__)

    WSGIRequestHandler.protocol_version = "HTTP/1.1"

    self.port = port
    self.host = host
    self.debug = debug
    
  
  def register_blueprints(self, *blueprints: List[Blueprint]): 
    for blueprint in blueprints:
      self.register_blueprint(blueprint)

    return self

  def listen(self) -> None:
    self.run(self.host, self.port, self.debug, processes=1, threaded=False)

    return self