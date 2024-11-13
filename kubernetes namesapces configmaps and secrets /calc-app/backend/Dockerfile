# Dockerfile for Flask backend
FROM python

WORKDIR /app

COPY requirements.txt ./
RUN pip3 install flask
RUN pip3 install flask-cors
RUN pip3 install psycopg2-binary

COPY . .

EXPOSE 5000

CMD ["python3","app.py"]