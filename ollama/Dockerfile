# Temel imaj: Ollama'nın resmi imajı
FROM ollama/ollama:latest

# (Opsiyonel) Modeli önceden yüklemek istersen buraya yazabilirsin:
# RUN ollama pull codellama

# Ollama varsayılan olarak 11434 portunda çalışır
EXPOSE 11434

# Ollama sunucusunu başlat
CMD ["ollama", "serve"]
