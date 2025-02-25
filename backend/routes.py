from . import app
import os
import json
from flask import jsonify, request, make_response, abort, url_for  # noqa; F401

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(SITE_ROOT, "data", "pictures.json")
data: list = json.load(open(json_url))


data = [
    {"id": 1, "pic_url": "http://dummyimage.com/230x100.png/dddddd/000000", "event_country": "United States", "event_state": "California", "event_city": "Fremont", "event_date": "11/2/2030"},
    {"id": 2, "pic_url": "http://dummyimage.com/230x100.png/dddddd/000000", "event_country": "United States", "event_state": "California", "event_city": "San Jose", "event_date": "12/1/2030"},
    {"id": 3, "pic_url": "http://dummyimage.com/230x100.png/dddddd/000000", "event_country": "United States", "event_state": "California", "event_city": "Sunnyvale", "event_date": "12/5/2030"},
    {"id": 4, "pic_url": "http://dummyimage.com/230x100.png/dddddd/000000", "event_country": "United States", "event_state": "California", "event_city": "Palo Alto", "event_date": "12/9/2030"},
    {"id": 5, "pic_url": "http://dummyimage.com/230x100.png/dddddd/000000", "event_country": "United States", "event_state": "California", "event_city": "Mountain View", "event_date": "12/15/2030"},
    {"id": 6, "pic_url": "http://dummyimage.com/230x100.png/dddddd/000000", "event_country": "United States", "event_state": "California", "event_city": "Menlo Park", "event_date": "12/20/2030"},
    {"id": 7, "pic_url": "http://dummyimage.com/230x100.png/dddddd/000000", "event_country": "United States", "event_state": "California", "event_city": "Redwood City", "event_date": "12/25/2030"},
    {"id": 8, "pic_url": "http://dummyimage.com/230x100.png/dddddd/000000", "event_country": "United States", "event_state": "California", "event_city": "Mountain View", "event_date": "12/30/2030"},
    {"id": 9, "pic_url": "http://dummyimage.com/230x100.png/dddddd/000000", "event_country": "United States", "event_state": "California", "event_city": "Cupertino", "event_date": "1/5/2031"},
    {"id": 10, "pic_url": "http://dummyimage.com/230x100.png/dddddd/000000", "event_country": "United States", "event_state": "California", "event_city": "Santa Clara", "event_date": "1/10/2031"}
]


######################################################################
# RETURN HEALTH OF THE APP
######################################################################


@app.route("/health")
def health():
    return jsonify(dict(status="OK")), 200

######################################################################
# COUNT THE NUMBER OF PICTURES
######################################################################


@app.route("/count")
def count():
    """return length of data"""
    if data:
        return jsonify(length=len(data)), 200

    return {"message": "Internal server error"}, 500


######################################################################
# GET ALL PICTURES
######################################################################
@app.route("/picture", methods=["GET"])
def get_pictures():
    return jsonify(data)

######################################################################
# GET A PICTURE
######################################################################


@app.route("/picture/<int:id>", methods=["GET"])
def get_picture_by_id(id):
    picture = next((picture for picture in data if picture["id"] == id), None)
    if picture is None:
        abort(404)
    return jsonify(picture)


######################################################################
# CREATE A PICTURE
######################################################################
@app.route("/picture", methods=["POST"])
def create_picture():
    """create a new picture"""
    new_picture = request.get_json()
    existing_picture = next((picture for picture in data if picture["id"] == new_picture["id"]), None)
    if existing_picture:
        return jsonify({"Message": f"picture with id {new_picture['id']} already present"}), 302
    data.append(new_picture)
    return jsonify(new_picture), 201


######################################################################
# UPDATE A PICTURE
######################################################################


@app.route("/picture/<int:id>", methods=["PUT"])
def update_picture(id):
    """update a picture"""
    picture = next((picture for picture in data if picture["id"] == id), None)
    if picture is None:
        return {"message": "picture not found"}, 404
    picture.update(request.get_json())
    return jsonify(picture)

######################################################################
# DELETE A PICTURE
######################################################################
@app.route("/picture/<int:id>", methods=["DELETE"])
def delete_picture(id):
    """delete a picture"""
    picture = next((picture for picture in data if picture["id"] == id), None)
    if picture is None:
        return {"message": "picture not found"}, 404
    data.remove(picture)
    return {"message": "picture deleted successfully"}, 204
