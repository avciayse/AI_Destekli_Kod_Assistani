from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

# WSL içinden Windows IP'siyle bağlantı
OLLAMA_URL = "http://10.255.255.254:11434/api/generate"

SYSTEM_PROMPT = (
    "You are a helpful assistant that generates Python code based on user prompts. "
    "Respond in the format:\n\n"
    "Title: <short title>\n\n```python\n<code here>\n```"
)

@app.route('/generate', methods=['POST'])
def generate_code():
    data = request.get_json()
    prompt = data.get("prompt")

    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    try:
        response = requests.post(OLLAMA_URL, json={
            "model": "codellama",
            "prompt": f"{SYSTEM_PROMPT}\n\n{prompt}",
            "stream": False
        })

        result = response.json()
        output = result.get("response", "").strip()

        # Varsayılan değerler
        title = "Kod Üretimi"
        code = output

        # Gelişmiş ayrıştırma
        if "Title:" in output:
            try:
                title_part = output.split("Title:")[1]
                if "```python" in title_part:
                    title = title_part.split("```")[0].strip()
                    code = title_part.split("```python")[1].split("```")[0].strip()
                elif "```" in title_part:
                    title = title_part.split("```")[0].strip()
                    code = title_part.split("```")[1].strip()
                else:
                    title = title_part.strip()
            except:
                pass

        return jsonify({
            "title": title,
            "code": code
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
