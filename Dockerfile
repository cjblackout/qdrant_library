FROM python:3.9-slim

WORKDIR /app

#RUN apk update && apk add --no-cache gcc
#RUN apk add build-base
#RUN apk add gcc
#RUN apk add musl-dev
#RUN apk add libffi-dev
#RUN apk add openssl-dev
#RUN apk add python3-dev


COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["python", "./app.py"]