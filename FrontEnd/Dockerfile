From python:3.10.13-alpine

COPY . .

RUN pip install -r requirements.txt

CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:8000", "main:app"]