FROM python:3.9.2-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV WORKDIR=/app

RUN mkdir -p ./logs

# COPY ./requirements.txt /
# COPY ./config.py /
# COPY app $WORKDIR
# COPY ./docker/entrypoint.sh /
# Install dependencies.
RUN pip install --no-cache-dir --upgrade pip && \
    pip install -r requirements.txt && rm requirements.txt && \
    apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y locales logrotate && \
    sed -i -e 's/# ru_RU.UTF-8 UTF-8/ru_RU.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales && \
    update-locale LANG=ru_RU.UTF-8 && \
    chmod u+x entrypoint.sh

ENV LANG ru_RU.UTF-8
COPY ./deploy/logs.conf /etc/logrotate.d/
ENTRYPOINT ["./entrypoint.sh"] 

