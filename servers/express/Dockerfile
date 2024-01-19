FROM node:20

EXPOSE 3000

WORKDIR /var/server

COPY ./package* /var/server
COPY ./src /var/server/src

RUN npm ci
RUN npm i -g typescript ts-node

CMD ["ts-node", "src/main.ts"]