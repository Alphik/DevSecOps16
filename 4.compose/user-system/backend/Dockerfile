FROM python:3.11-alpine3.20

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY main.py .

EXPOSE 5050

CMD [ "python3","main.py" ]