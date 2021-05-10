FROM golang:alpine AS build

WORKDIR /app

COPY . .

RUN go mod download
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -installsuffix cgo -ldflags '-extldflags "-static"' -o Server .


FROM scratch

WORKDIR /app

COPY --from=build /app/Server .

EXPOSE 8000
ENTRYPOINT [ "./Server" ]