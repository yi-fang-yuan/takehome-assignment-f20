from typing import Tuple

from flask import Flask, jsonify, request, Response
import mockdb.mockdb_interface as db

app = Flask(__name__)


def create_response(
    data: dict = None, status: int = 200, message: str = ""
) -> Tuple[Response, int]:
    """Wraps response in a consistent format throughout the API.
    
    Format inspired by https://medium.com/@shazow/how-i-design-json-api-responses-71900f00f2db
    Modifications included:
    - make success a boolean since there's only 2 values
    - make message a single string since we will only use one message per response
    IMPORTANT: data must be a dictionary where:
    - the key is the name of the type of data
    - the value is the data itself

    :param data <str> optional data
    :param status <int> optional status code, defaults to 200
    :param message <str> optional message
    :returns tuple of Flask Response and int, which is what flask expects for a response
    """
    if type(data) is not dict and data is not None:
        raise TypeError("Data should be a dictionary 😞")

    response = {
        "code": status,
        "success": 200 <= status < 300,
        "message": message,
        "result": data,
    }
    return jsonify(response), status


"""
~~~~~~~~~~~~ API ~~~~~~~~~~~~
"""


@app.route("/")
def hello_world():
    return create_response({"content": "hello world!"})


@app.route("/mirror/<name>")
def mirror(name):
    data = {"name": name}
    return create_response(data)
# part 1 and part 6
@app.route("/shows", methods=['GET'])
def get_all_shows():
    minEpisodes = request.args.get('minEpisodes')
    if minEpisodes is not None: 
        minEpisodes = int(minEpisodes)
        shows = db.get('shows')
        new_shows = list(filter(lambda x: minEpisodes <= x.get('episodes_seen'), shows))
        if not new_shows:
          return  create_response({"response":"there is no show that has that much episodes seen!"})
        return create_response({"shows": new_shows})
    return create_response({"shows": db.get('shows')})

#part 2 
@app.route("/shows/<id>", methods=['GET'])
def get_id_shows(id):
    if db.getById('shows', int(id)) is None:
        return create_response(status=404, message="The provided Id does not exists!")
    return create_response({"result": db.getById('shows',int(id))})

# part 3
@app.route("/shows",methods=['POST'])
def create_shows():
    if request.method == 'POST':
        req_data = request.get_json()
        if req_data['name'] is None:
            return create_response(status=422, message="There is no name in the body!")
        if req_data['episodes_seen'] is None:
            return create_response(status=422, message="There is no episodes_seen in the body!")
        db.create('shows',req_data)
        return create_response({"shows": db.get('shows')})

# part 5        
@app.route("/shows/<id>", methods=['DELETE'])
def delete_show(id):
    if db.getById('shows', int(id)) is None:
        return create_response(status=404, message="No show with this id exists")
    db.deleteById('shows', int(id))
    return create_response(message="Show deleted")

#part 4
@app.route("/shows/<id>", methods=['PUT'])
def update_show(id):
    if request.method == 'PUT':
        req_data = request.get_json()
        update_data = {
            "name": req_data['name'],
            "episodes_seen":req_data['episodes_seen']
        }
        if db.getById('shows', int(id)) is None:
            return create_response(status=404, message="The provided Id does not exists!")
        db.updateById('shows',int(id), update_data)
        return create_response({"shows": db.get('shows')})
# TODO: Implement the rest of the API here!

"""
~~~~~~~~~~~~ END API ~~~~~~~~~~~~
"""
if __name__ == "__main__":
    app.run(port=8080, debug=True)
