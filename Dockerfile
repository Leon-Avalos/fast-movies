FROM python:3.9

WORKDIR /movies-api

COPY ./requirements.txt /movies-api/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /movies-api/requirements.txt

COPY  main.py /movies-api

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9000"]
