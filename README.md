# R U Dead Yet?

## clone

```zsh
python3 -m venv .venv

source .venv/bin/activate

pip3 install -r requirements.txt
```

## run

```zsh
usage: main.py [-h] [-s SOCKETS] [-t TIME] [-b BYTES] [-l LENGTH] url

positional arguments:
  url                   URL i.e [http[s]://]host[:port][path]

options:
  -h, --help            show this help message and exit
  -s SOCKETS, --sockets SOCKETS
                        Socket connection count(Default : 150)
  -t TIME, --time TIME  KeepAlive Timeout(Default : 10)
  -b BYTES, --bytes BYTES
                        Byte Length of sent per time(Default : 1)
  -l LENGTH, --length LENGTH
                        HTTP POST Content-Length(Default : 64)
```
