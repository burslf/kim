FROM python:3.8.1-slim 

ENV PYTHONUNBUFFERED 1 
EXPOSE 6262

COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt

COPY . /app

CMD ["python", "app.py"]