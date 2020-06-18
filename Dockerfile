# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
&& apt-get install gcc -y \
&& apt-get clean


# Install pip requirements
ADD requirements.txt .


RUN python -m pip install -r requirements.txt

WORKDIR /app
ADD ./autoremovetorrents /app/autoremovetorrents
ADD config.yml /config/
ADD run.py .

# Switching to a non-root user, please refer to https://aka.ms/vscode-docker-python-user-rights
RUN useradd appuser && chown -R appuser /app
USER appuser

ENV CONFIG_YML /config/config.yml
ENV SCAN_INTERVAL 60

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
#CMD python -m autoremovetorrents.main --conf /config/config.yml --view
#CMD python run.py
ENTRYPOINT ["python", "run.py"]