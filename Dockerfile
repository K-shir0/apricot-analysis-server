FROM python:3.8

ENV LC_ALL=C.UTF-8 \
    LANG=C.UTF-8 \
    FLASK_ENV=development

WORKDIR /app
COPY . .

RUN apt -y update && \
    apt -y install build-essential libssl-dev libffi-dev python3-dev && \
    pip install pipenv && \
    pipenv install

CMD ["pipenv", "run", "start"]

EXPOSE 5000