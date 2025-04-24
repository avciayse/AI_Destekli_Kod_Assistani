# 🤖 Yapay Zekâ Destekli Kod Üretici

Bu proje, S4E DevOps staj teknik değerlendirme görevi kapsamında hazırlanmış, Flask tabanlı ve yapay zekâ destekli bir kod üretici web uygulamasıdır. Kullanıcıdan alınan prompt’a göre Python kodu üreten bir LLM (Codellama) ile entegredir.

---

## 🚀 Özellikler

- ✅ Flask tabanlı Python backend
- ✅ HTML (Jinja2) destekli basit kullanıcı arayüzü
- ✅ Ollama ile entegre Codellama modeli üzerinden kod üretimi
- ✅ Docker ile containerleştirme
- ✅ Helm ile Kubernetes üzerinde dağıtım (Minikube)
- ✅ JSON response: başlık + kod bloğu

---

## 🧠 Kullanılan Teknolojiler

| Katman | Teknoloji |
|--------|-----------|
| Backend | Python, Flask, Requests |
| AI | Ollama + Codellama |
| Arayüz | HTML, Jinja2 |
| Container | Docker |
| Orkestrasyon | Kubernetes + Helm + Minikube |

---

## ⚙️ Kurulum ve Çalıştırma

### 1. Codellama Modeli İçin Ollama'yı Başlat
```bash
ollama serve
