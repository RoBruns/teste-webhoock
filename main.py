from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.json  # Captura os dados do webhook no formato JSON
        print(f"🔹 Webhook recebido: {data}")  # Log dos dados recebidos
        
        # Aqui você pode processar os dados conforme necessário
        # Exemplo: salvar em banco de dados, acionar outra API, etc.
        
        return jsonify({"status": "sucesso", "mensagem": "Webhook recebido"}), 200
    
    except Exception as e:
        print(f"❌ Erro ao processar webhook: {e}")
        return jsonify({"status": "erro", "mensagem": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # Executa o servidor na porta 5000
