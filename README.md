# R U Dead Yet?

## Clone

```zsh
python3 -m venv .venv

source .venv/bin/activate

pip3 install -r requirements.txt
```

## RUDY

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

### for Example

- host: http://localhost
- port: 3000
- keepAliveTimeout: 10s

```zsh
python3 main.py http://localhost:3000 -t 10
```

## Test Servers

### Run Express with Docker

- version: Node 20
- keepAliveTimeout: 10s
- maxConnections: 10
- port: args(default 3000)

```zsh
cd servers/express

sh docker.sh [port]
```

### Run Flask with Docker

- version: Python 11
- port: args(default 3000)
- processes: 1
- threads: not use

```zsh
cd servers/flask

sh docker.sh [port]
```

### Run SpringBoot With Docker

- version: openjdk-17
- build: gradle
- port: args(default 3000)
- threads: 10

```zsh
cd servers/spring-boot

sh docker.sh [port]
```
