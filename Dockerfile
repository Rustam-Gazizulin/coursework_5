FROM python:3.10

WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY data data
COPY templates templates
COPY app.py .
COPY base.py .
COPY classes.py .
COPY equipment.py .
COPY skills.py .
COPY unit.py .

CMD flask run -h 0.0.0.0 -p 80