import { Server } from 'http';

import { NestFactory } from '@nestjs/core';

import { AppModule } from './app.module';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  const server = app.getHttpServer() as Server;

  server.keepAliveTimeout = 10000;
  server.maxConnections = 10;

  await app.listen(3000);
}
bootstrap();
