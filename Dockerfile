FROM python:3.13-slim

WORKDIR /app

COPY . /app

RUN pip install poetry
RUN poetry install

EXPOSE 5000

ENV FLASK_APP=app.py
ENV FLASK_ENV=production

CMD ["poetry", "run", "flask", "run", "--host", "0.0.0.0"]
