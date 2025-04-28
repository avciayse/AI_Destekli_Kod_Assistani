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

---![TP51IyCm68Rl-HKVExM7GhlrK3p8fY32EbTSTnAHs7v8Q9gK91M6-9yy-GVqX_arNMM7hOSImlC-xmjPMiUDwrl9UEMqWNKl9LUY4i0jx2qQnZfUDVmDORRkNz4eT6ZXLlRMeO5W8vHew3wSmGS3-lploQOODRgEk1NMaIyYqxkey7dGxiPpSW6jiPFwqA9o4Dn9RXkueGMewj2d2rqVavgc](https://github.com/user-attachments/assets/955d8405-f95a-4740-a818-4ffaab635a76)



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
