FROM python:3.8-alpine as builder

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /wheels
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /wheels flask gunicorn

FROM python:3.8-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY --from=builder /wheels /wheels
RUN pip install --no-cache /wheels/*
RUN rm -rf /wheels

COPY main.py /app

ENTRYPOINT [ "gunicorn" ]
CMD [ "main:app", "--bind=0.0.0.0:8000" ]