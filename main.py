from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.get_json()

        # Verifica se recebeu JSON válido
        if not data:
            return jsonify({"erro": "Nenhum JSON enviado"}), 400
        
        print(f"📥 Webhook recebido: {data}")  # Log dos dados recebidos

        # Extrai informações importantes (ajuste conforme necessário)
        event = data.get("event")
        sale_id = data.get("sale_id")
        customer_name = data.get("customer", {}).get("name")
        total_price = data.get("total_price")
        payment_status = data.get("status")

        print(f"📝 Evento: {event}, Venda: {sale_id}, Cliente: {customer_name}, Valor: {total_price}, Status: {payment_status}")

        # Aqui você pode salvar os dados no banco ou disparar uma ação

        return jsonify({"status": "sucesso", "mensagem": "Webhook processado"}), 200
    
    except Exception as e:
        print(f"❌ Erro ao processar webhook: {e}")
        return jsonify({"erro": str(e)}), 400

if __name__ == '__main__':
    app.run()
