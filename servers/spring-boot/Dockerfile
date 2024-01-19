FROM openjdk:17

WORKDIR /var/server

COPY ./build/libs/*.jar /var/server/app.jar

CMD ["java", "-jar", "app.jar"]