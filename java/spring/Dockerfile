FROM alpine:3.13 as builder

WORKDIR /build

RUN apk --no-cache add openjdk11 
RUN apk --no-cache add maven

RUN /usr/lib/jvm/default-jvm/bin/jlink \
    --compress=2 \
    --module-path /usr/lib/jvm/default-jvm/jmods \
    --add-modules java.base,java.logging,java.xml,jdk.unsupported,java.sql,java.naming,java.desktop,java.management,java.security.jgss,java.instrument \
    --output /jdk-minimal

COPY pom.xml pom.xml
RUN mvn dependency:go-offline

COPY src src
RUN mvn clean package


FROM alpine:3.13

COPY --from=builder /jdk-minimal /opt/jdk/
COPY --from=builder /build/target/*.jar /app.jar

EXPOSE 8000
ENTRYPOINT [ "/opt/jdk/bin/java" ]
CMD [ "-jar", "/app.jar"]