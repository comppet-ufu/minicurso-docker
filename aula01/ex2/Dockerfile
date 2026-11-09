FROM ubuntu:latest

RUN apt-get update && apt-get install -y fortune cowsay

ENTRYPOINT ["/bin/sh", "-c", "/usr/games/fortune | /usr/games/cowsay"]
