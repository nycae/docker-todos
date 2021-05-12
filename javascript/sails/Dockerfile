FROM node:14 AS builder

WORKDIR /app
#COPY package.json api assets config tasks views app.js Gruntfile.js ./
ADD . .
RUN npm install

FROM node:14-alpine

WORKDIR /app
COPY --from=builder /app /app
EXPOSE 8000
ENTRYPOINT [ "npm" ]
CMD [ "start" ]
