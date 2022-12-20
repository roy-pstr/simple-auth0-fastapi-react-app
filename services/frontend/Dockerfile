FROM node:16.4.0-buster
# RUN mkdir -p /home/node/src
WORKDIR /app
COPY ./package.json .
COPY ./package-lock.json .
RUN npm install --production

COPY . ./

CMD [ "npm", "start" ]