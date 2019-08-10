FROM python:3.7
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /code:$PYTHONPATH
WORKDIR /code
COPY . .
RUN pip install -r requirements.txt
RUN (apt-get update && apt-get install -y postgresql-client)
