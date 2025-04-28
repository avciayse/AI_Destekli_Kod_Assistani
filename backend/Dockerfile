# backend/Dockerfile

FROM python:3.13-alpine

RUN apk add --no-cache gcc musl-dev libffi-dev

WORKDIR /app

# Sadece gerekli dosyaları kopyala
COPY requirements.txt .
COPY main.py .
COPY templates/ templates/

# Paketleri yükle
RUN pip install --no-cache-dir \
        --index-url https://pypi.org/simple \
        -r requirements.txt

# Ortam değişkenleri
ENV OLLAMA_URL=http://host.docker.internal:11434/api/generate

COPY backend/ ./backend/

# Uygulamayı çalıştır
CMD ["python", "./backend/main.py"]
