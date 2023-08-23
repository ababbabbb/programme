from flask import jsonify


def handle_exception(error):
    response = {
        'error': str(error),
    }
    return jsonify(response), error.code
