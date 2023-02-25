FROM python:3.10

RUN apt-get update \
 && apt-get install -y \
      ffmpeg \
 && rm -rf /var/cache/apt/*

ADD overlay.png .

ADD requirements.txt .
RUN pip install -r requirements.txt

ADD back.py .

CMD ["uvicorn", "back:app", "--host", "0.0.0.0", "--port", "80", "--proxy-headers"]
