# Hafif ve güvenli base image
FROM python:3.13-alpine

# Gerekli sistem kütüphaneleri (C compiler ve pip bağımlılıkları için)
RUN apk add --no-cache gcc musl-dev libffi-dev

# Çalışma dizinini ayarla
WORKDIR /app

# Tüm dosyaları konteynıra kopyala
COPY . /app

# Python kütüphanelerini yükle
RUN pip install --no-cache-dir flask requests

# Uygulamayı başlat
CMD ["python", "main.py"]
