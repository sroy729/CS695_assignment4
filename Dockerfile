FROM python:latest
LABEL Maintainer="shbham"
WORKDIR /usr/app/src
COPY server.py ./
EXPOSE 8084
CMD [ "python3", "./server.py"]
