from dotenv import load_dotenv
from flask import Blueprint, Flask, jsonify, request
from mem0 import Memory

load_dotenv()

app = Flask(__name__)

api = Blueprint("api", __name__, url_prefix="/v1")

memory = Memory()


@api.route("/memories", methods=["POST"])
def add_memories():
    try:
        body = request.get_json()
        messages = body["messages"]
        del body["messages"]
        return memory.add(messages, **body)
    except Exception as e:
        return jsonify({"message": str(e)}), 400


@api.route("/memories/<memory_id>", methods=["PUT"])
def update_memory(memory_id):
    try:
        existing_memory = memory.get(memory_id)
        if not existing_memory:
            return jsonify({"message": "Memory not found!"}), 400
        body = request.get_json()
        return memory.update(memory_id, data=body["data"])
    except Exception as e:
        return jsonify({"message": str(e)}), 400


@api.route("/memories/search", methods=["POST"])
def search_memories():
    try:
        body = request.get_json()
        query = body["query"]
        del body["query"]
        return memory.search(query, **body)
    except Exception as e:
        return jsonify({"message": str(e)}), 400


@api.route("/memories", methods=["GET"])
def get_memories():
    try:
        user_id = request.args.get("user_id", None)
        agent_id = request.args.get("agent_id", None)
        run_id = request.args.get("run_id", None)
        return memory.get_all(user_id=user_id, agent_id=agent_id, run_id=run_id)
    except Exception as e:
        return jsonify({"message": str(e)}), 400


@api.route("/memories/<memory_id>/history", methods=["GET"])
def get_memory_history(memory_id):
    try:
        return memory.history(memory_id)
    except Exception as e:
        return jsonify({"message": str(e)}), 400


app.register_blueprint(api)
