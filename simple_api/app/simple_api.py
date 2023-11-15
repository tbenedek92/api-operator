from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("simple_api")

@app.route('/update', methods=['POST'])
def update():
    data = request.json
    logger.info(f"Update Request with payload: {data}")
    # Implement your update logic here
    return jsonify({"status": "update successful", "data": data}), 200

@app.route('/delete', methods=['POST'])
def delete():
    # For the delete endpoint, we assume no payload is sent
    logger.info("Delete Request received")
    # Implement your delete logic here
    return jsonify({"status": "delete successful"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
