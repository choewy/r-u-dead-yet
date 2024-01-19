import urllib.parse
import json


class Args:
  socket_count = 150
  timeout = 10
  byte_length = 1
  content_length = 64
  url = ""
  tls = False
  host = ""
  port = 80
  path = ""

  def __init__(self, args):
    self.socket_count = args.sockets
    self.timeout = args.time
    self.byte_length = args.bytes
    self.content_length = args.length
    self.__set_http_url(args.url)
    self.__set_http_args()

  def __set_http_url(self, url: str) -> None:
    if url.startswith("http://") or url.startswith("https://"):
      self.url = url
    else:
      self.url = f"https://{url}"

  def __set_http_args(self) -> None:
    url = urllib.parse.urlparse(self.url)
    host = url.netloc

    self.path = "/" if url.path == "" else url.path
    self.host = host

    if url.scheme == "https":
      self.tls = True
      self.port = 443

      return

    if host.find(":") > -1:
      [__host, __port] = host.split(":")
      self.host = __host
      self.port = int(__port)

  def __str__(self) -> str:
    return json.dumps({
      "socket_count": self.socket_count,
      "timeout": self.timeout,
      "byte_length": self.byte_length,
      "content_length": self.content_length,
      "url": self.url,
      "tls": self.tls,
      "host": self.host,
      "port": self.port,
      "path": self.path
    }, indent=2)
      


    


