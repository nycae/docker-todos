FROM mcr.microsoft.com/dotnet/sdk:5.0-alpine AS base

# copy csproj and restore as distinct layers
COPY dotnet.csproj .
RUN dotnet restore .

# copy everything else and build
ADD . .
RUN dotnet publish . --runtime linux-musl-x64 -c release -o out -p:PublishTrimmed=true

# build runtime image
FROM mcr.microsoft.com/dotnet/runtime-deps:5.0-alpine
WORKDIR /app
COPY --from=base /out ./

EXPOSE 8000
ENTRYPOINT ["./dotnet"]