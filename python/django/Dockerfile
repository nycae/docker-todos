FROM python:3.8 as builder

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .

RUN mkdir /wheels
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /wheels django djangorestframework gunicorn


FROM python:3.8-alpine

WORKDIR /app
COPY --from=builder /wheels /wheels
RUN pip install --no-cache /wheels/*
RUN rm -rf /wheels

COPY . /app

ENTRYPOINT [ "gunicorn" ]
CMD [ "todos.wsgi:application", "--bind=0.0.0.0:8000" ]