FROM python:3.7


COPY requirements.txt /app/requirements.txt

RUN apt-get update && apt-get install -y gcc unixodbc-dev sqlite3 libsqlite3-dev

RUN pip install --upgrade pip \
    && apt-get clean -y

RUN pip install -r /app/requirements.txt

WORKDIR /app
COPY . /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN groupadd -g 999 appuser && \
    useradd -r -u 999 -g appuser appuser
USER appuser

VOLUME /app/logs

EXPOSE 5001

CMD python runserver.py