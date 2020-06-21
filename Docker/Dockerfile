FROM python:3.8.3-slim AS compile-image

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install -y --no-install-recommends build-essential gcc

RUN python -m venv /opt/venv
# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"

# Install pip requirements
ADD requirements.txt .
RUN pip install -r requirements.txt

# remove python cache files
RUN find /opt/venv -name \*.pyc -delete

# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8.3-slim AS build-image

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

COPY --from=compile-image /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /app
ADD config/* /config/
ADD ./torrent-manager /app/

# Switching to a non-root user, please refer to https://aka.ms/vscode-docker-python-user-rights
RUN useradd appuser && chown -R appuser /app
USER appuser

ENV CONFIG_YML /config/config.yml
ENV SCAN_INTERVAL 60

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
#CMD python -m autoremovetorrents.main --conf /config/config.yml --view
#CMD python run.py
ENTRYPOINT ["python", "torrent-manager.py"]
