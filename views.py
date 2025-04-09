from flask import Blueprint, render_template, jsonify, request ,redirect , url_for

views = Blueprint(__name__, "views")

#home
@views.route("/")
def home():
    return render_template("Index.html")

@views.route("/better_call_saul")
def bettercallsaul():
    
    return render_template("Better_call_saul.html")






#otevrit json data
@views.route("/json")
def get_json():
    return jsonify({'name':'tim', 'coolness':10})

#pridat json data
@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)

#redirect
@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views.get_json"))

