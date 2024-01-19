import express from 'express';

import { Server } from './server';

const server = new Server(3000, '::', 10000, 10);
const router = express.Router();

router.get('/', async (_, res) => {
  res.status(200).send({ connections: await server.getConnections() });
});

router.post('/', async (_, res) => {
  res.status(201).send({ connections: await server.getConnections() });
});

server.bindRouters({ path: '/', router }).listen();
