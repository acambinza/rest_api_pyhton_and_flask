FROM python:3.10.11

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
#RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

#RUN pip install flask
#CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]

CMD ["flask", "run", "--host", "0.0.0.0"]