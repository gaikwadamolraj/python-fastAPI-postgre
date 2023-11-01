FROM python:3.9

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

EXPOSE 5000
#ENV DATABASE_URL="postgresql://myuser:secret@postgres/metadatadb"

CMD [ "bash", "-c", "uvicorn main:app --host 0.0.0.0 --port 5000" ]

#CMD ["python", "/app/api/main.py"]