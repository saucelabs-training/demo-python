FROM python:3
WORKDIR /demo-python
COPY . /demo-python
RUN pip install -r requirements.txt
EXPOSE 8081