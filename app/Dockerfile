FROM python:alpine3.17
WORKDIR /app
#ENV FLASK_APP=api.py
#ENV FLASK_RUN_HOST=0.0.0.0
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["python", "api.py"]
