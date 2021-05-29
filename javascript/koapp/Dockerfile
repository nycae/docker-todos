FROM node:15 AS builder

WORKDIR /app
# COPY package-lock.json package.json index.js ./
COPY index.js .
RUN npm i koa koa-router koa-body-parser

FROM node:15-alpine

WORKDIR /app
COPY --from=builder /app /app
EXPOSE 8000
ENTRYPOINT [ "node" ]
CMD [ "." ]
