FROM node:20

EXPOSE 3000

WORKDIR /var/server

COPY ./package* /var/server
COPY ./tsconfig* /var/server
COPY ./nest* /var/server
COPY ./src /var/server/src

RUN npm ci
RUN npm run build

CMD ["node", "dist/main.js"]