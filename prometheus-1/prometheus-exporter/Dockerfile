FROM python
WORKDIR /app
RUN pip3 install prometheus_client flask
COPY . .
EXPOSE 5001
CMD ["python3", "app.py"]