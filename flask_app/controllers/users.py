from flask import render_template, redirect, request, session 
from flask_app import app
from flask_app.models.user import User

@app.route("/")
def index():
    return redirect("/users")

@app.route("/users")
def all_users():
    users = User.get_all()
    # users is the list users =[] in the get_all class method. Friend is the class. get)all is the method name
    print(users)
    return render_template("read.html", users=users)

@app.route("/users/new")
def new_users():
    return render_template("create.html")


@app.route('/users/add', methods=['POST'])
def create_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    # data = {
    #     "first_name": request.form["first_name"],
    #     "last_name": request.form["last_name"],
    #     "email":request.form["email"]
    # }
    print(request.form)
    # We pass the data dictionary into the save method from the User class.
    User.save(request.form)
    # Don't forget to redirect after saving to the database.
    return redirect("/users")


@app.route("/users/show/<int:id>")
def show(id):
    data = {
        "id": id,
    }
    return render_template("show.html", user=User.get_one(data))

@app.route("/users/edit/<int:id>")  # <int:id> = path variable - the id of the individual item
def edit(id):
    data = {
        "id": id,
    }
    return render_template("edit_user.html", user=User.get_one(data))


@app.route("/users/update", methods=['POST'])
def update():
    User.update(request.form)
    return redirect("/users")


@app.route("/users/delete/<int:id>")
def delete(id):
    data = {
        "id": id,
    }
    User.delete(data)
    return redirect("/users")

if __name__ == "__main__":
    app.run(debug=True)
