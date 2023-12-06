# Dockerfile, Image, Container
FROM python:3.11
ADD main.py .
RUN pip install --upgrade pip && pip install requests
CMD ["python", "./main.py"]