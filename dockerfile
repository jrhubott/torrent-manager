FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY config.yml ./
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "autoremove-torrents" ]