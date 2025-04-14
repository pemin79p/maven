from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data store (like a simple database)
data_store = {}

# GET - retrieve all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(data_store)

# POST - add a new item
@app.route('/items', methods=['POST'])
def add_item():
    item = request.json
    item_id = str(len(data_store) + 1)
    data_store[item_id] = item
    return jsonify({'id': item_id, 'item': item}), 201

# PUT - update an existing item
@app.route('/items/<item_id>', methods=['PUT'])
def update_item(item_id):
    if item_id in data_store:
        data_store[item_id] = request.json
        return jsonify({'id': item_id, 'item': data_store[item_id]})
    else:
        return jsonify({'error': 'Item not found'}), 404

# DELETE - delete an item
@app.route('/items/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    if item_id in data_store:
        deleted_item = data_store.pop(item_id)
        return jsonify({'message': 'Item deleted', 'item': deleted_item})
    else:
        return jsonify({'error': 'Item not found'}), 404

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
