FROM python:3.12.4

WORKDIR /usr/app/

RUN apt update && apt upgrade -y && apt install -y libusb-1.0-0-dev

COPY requirements.txt ./
RUN pip install --no-cache-dir -U -r requirements.txt

COPY ./src ./src

ENV PYTHONPATH=/usr/app/src

CMD ["python", "src/main.py"]
