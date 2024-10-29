FROM node:18-alpine3.20

WORKDIR /app

COPY ./user-management/package*.json ./

RUN npm i

COPY ./user-management/ ./

EXPOSE 3000

CMD [ "npm","start" ]