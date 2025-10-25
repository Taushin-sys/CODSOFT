# app.py
from flask import Flask, request, jsonify, render_template_string
from studentbot.bot_core import StudentBot

app = Flask(__name__)
bot = StudentBot()

INDEX_HTML = """
<!doctype html>
<title>Student Helper Bot</title>
<h2>Student Helper Bot (Web Demo)</h2>
<input id="msg" placeholder="Type a message" style="width:60%%;">
<button onclick="send()">Send</button>
<div id="out"></div>
<script>
async function send(){
  const msg = document.getElementById('msg').value;
  const res = await fetch('/api/chat', {method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify({msg})});
  const data = await res.json();
  document.getElementById('out').innerHTML += "<p><b>You:</b> "+msg+"<br><b>Bot:</b> "+data.response+"</p>";
  document.getElementById('msg').value = '';
}
</script>
"""

@app.route('/')
def index():
    return render_template_string(INDEX_HTML)

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json() or {}
    msg = data.get('msg', '')
    resp = bot.respond(msg)
    return jsonify({"response": resp})

if __name__ == "__main__":
    app.run(debug=True, port=5000)