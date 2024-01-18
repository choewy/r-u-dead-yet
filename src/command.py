import argparse

class Command(argparse.ArgumentParser):
  def __init__(self) -> None:
    argparse.ArgumentParser.__init__(self)

    self.add_argument(
        "-s", "--sockets", 
        type=int, 
        default=150, 
        help="Socket connection count(Default : 150)"
    )

    self.add_argument(
        "-t", "--time", 
        type=float, 
        default=10, 
        help="KeepAlive Timeout(Default : 10)"
    )

    self.add_argument(
        "-b", "--bytes", 
        type=int, 
        default=1, 
        help="Byte Length of sent per time(Default : 1)"
    )

    self.add_argument(
        "-l", "--length", 
        type=int, 
        default=64, 
        help="HTTP POST Content-Length(Default : 64)"
    )

    self.add_argument(
      "url",
      help="URL i.e [http[s]://]host[:port][path]"
    )



