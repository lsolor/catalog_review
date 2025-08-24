# syntax=docker/dockerfile:1
FROM python:3.12-bookworm

ADD . /app
WORKDIR /app
RUN uv sync --locked

RUN apt-get update && apt-get install -y gcc musl-dev linux-headers
RUN pip install -r requirements.txt
EXPOSE 5000

CMD ["flask", "run", "--debug"]