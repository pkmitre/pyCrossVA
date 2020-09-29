FROM tiangolo/uwsgi-nginx-flask:python3.8

COPY . /app
COPY api.py /app/main.py
RUN pip install -r /app/requirements.txt
