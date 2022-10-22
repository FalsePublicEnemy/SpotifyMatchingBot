FROM python:3.9-slim-buster as production
LABEL maintainer="Karim Nassar" description="Spotify Matcher Bot"

RUN apt-get update
WORKDIR /app

COPY requirements.txt requirements.txt
RUN python -m pip install --no-cache-dir -r requirements.txt

RUN apt-get -y install cargo
RUN cargo install --force watchexec 

RUN apt-get update && apt-get install -y curl postgresql-client && apt-get clean

CMD ["watchexec", "-r", "-e", "py", "--", "python", "main.py"]

