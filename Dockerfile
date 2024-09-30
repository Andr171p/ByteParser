FROM python: 3.11

WORKDIR /test_task_app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ..

CMD ["python", "main.py"]