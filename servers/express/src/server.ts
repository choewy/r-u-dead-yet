import stream from 'stream';
import express from 'express';
import http from 'http';

export class Server {
  express: express.Express;
  http: http.Server;

  constructor(
    private readonly port: number = 3000,
    private readonly host: string = '::',
    keepAliveTimeout: number = 10000,
    maxConnections: number = 10,
  ) {
    this.express = express();
    this.http = http.createServer(this.express);
    this.http.keepAliveTimeout = keepAliveTimeout;
    this.http.maxConnections = maxConnections;
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
