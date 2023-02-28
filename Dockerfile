# Build

FROM python:latest
COPY main.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN chmod u+x ./main.py
ENTRYPOINT ["./main.py"]