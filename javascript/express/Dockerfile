FROM node:15 AS builder

WORKDIR /app
COPY package.json index.js ./
RUN npm install

FROM node:15-alpine

WORKDIR /app
COPY --from=builder /app /app
EXPOSE 8000
ENTRYPOINT [ "node" ]
CMD [ "." ]
