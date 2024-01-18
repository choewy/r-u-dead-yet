# R U Dead Yet?

## Clone

```zsh
python3 -m venv .venv

source .venv/bin/activate

pip3 install -r requirements.txt
```

## Run RUDY Attack

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

## Run Express Server

- port: 3000
- keepAliveTimeout: 15s
- maxConnections: 10

```zsh
python3 main.py http://localhost:3000
```

```zsh
cd servers/express
npm run start
```
