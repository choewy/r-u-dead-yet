import stream from 'stream';
import express from 'express';
import http from 'http';

class Server {
  express: express.Express;
  http: http.Server;

  constructor(
    private readonly port: number = 3000,
    private readonly host: string = '::',
  ) {
    this.express = express();
    this.http = http.createServer(this.express);
    this.http.keepAliveTimeout = 15000;
    this.http.maxConnections = 10;
  }

  async getConnections() {
    return new Promise<number>((resolve) => {
      this.http.getConnections((_, c) => {
        resolve(c);
      });
    });
  }

  bindRouters(...routers: { path: string; router: express.Router }[]) {
    for (const { path, router } of routers) {
      this.express.use(path, router);
    }

    return this;
  }

  bindHttpEvents(server: http.Server) {
    const events = [
      'connect',
      'connection',
      'close',
      'error',
      'listening',
      'checkContinue',
      'checkExpectation',
      'clientError',
      'request',
      'dropRequest',
      'upgrade',
    ];

    for (const event of events) {
      server.on(event, async () => {
        console.log(
          `http - ${event} - connections : ${await this.getConnections()}`,
        );
      });
    }
  }

  bindSocketEvents(socket: stream.Duplex) {
    const events = ['close', 'end', 'timeout', 'error'];

    for (const event of events) {
      socket.on(event, async () => {
        console.log(
          `socket - ${event} - connections : ${await this.getConnections()}`,
        );
      });
    }

    socket.on('data', (data: Buffer) => {
      console.log(`socket - data : ${data.toString('utf-8')}`);
    });
  }

  listen() {
    this.bindHttpEvents(
      this.http
        .on('connection', this.bindSocketEvents.bind(this))
        .listen(this.port, this.host),
    );
  }
}

const server = new Server();
const router = express.Router();

router.get('/', async (_, res) => {
  res.status(200).send({ connections: await server.getConnections() });
});

router.post('/', async (_, res) => {
  res.status(201).send({ connections: await server.getConnections() });
});

server.bindRouters({ path: '/', router }).listen();
