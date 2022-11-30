FROM python
RUN apt-get update && apt-get install python3-pip -y && apt-get install python-dev -y
WORKDIR /app
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN pip install flask
CMD ["python","app.py"]