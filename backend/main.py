import os
from flask import Flask, request, jsonify, render_template
import requests
import traceback

app = Flask(__name__, template_folder="templates")

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

# ENV’den alalım, yoksa varsayılanı host.docker.internal’e çek
OLLAMA_URL = os.environ.get(
    "OLLAMA_URL",
    "http://host.docker.internal:11434/api/generate"
)

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
        resp = requests.post(OLLAMA_URL, json={
            "model": "codellama",
            "prompt": f"{SYSTEM_PROMPT}\n\n{prompt}",
            "stream": False
        })
        resp.raise_for_status()
        result = resp.json()
        output = result.get("response", "").strip()

        title = "Kod Üretimi"
        code = output
        if "Title:" in output:
            try:
                parts = output.split("Title:")
                title_part = parts[1]
                if "```python" in title_part:
                    title = title_part.split("```")[0].strip()
                    code = title_part.split("```python")[1].split("```")[0].strip()
                elif "```" in title_part:
                    title = title_part.split("```")[0].strip()
                    code = title_part.split("```")[1].strip()
                else:
                    title = title_part.strip()
            except Exception:
                traceback.print_exc()

        return jsonify({"title": title, "code": code})

    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)

