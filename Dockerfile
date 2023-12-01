FROM tiangolo/uwsgi-nginx-flask:python3.8

COPY . /app
COPY api.py /app/main.py

RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r /app/requirements.txt
