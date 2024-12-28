FROM python:3.12.8-slim-bullseye

COPY ./Source/requirements.txt /app/

WORKDIR /app

RUN pip install -r requirements.txt

COPY ./Source/bot.py ./

CMD ["python3", "bot.py"]