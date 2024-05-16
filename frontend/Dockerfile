FROM node:21-alpine as build

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . ./

RUN npm i && npm run build && rm -rf node_modules

CMD cp -r build result_build