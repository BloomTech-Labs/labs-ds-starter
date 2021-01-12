FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED 1
RUN python -m pip install --upgrade pip && pip install pipenv
COPY Pipfile* ./
RUN pipenv install --system --deploy
COPY ./app ./app
EXPOSE 8000
CMD uvicorn app.main:app --host 0.0.0.0 --port 8000
