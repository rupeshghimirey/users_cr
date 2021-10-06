from flask import Flask, render_template, session, request, redirect
# import the class from friend.py
from user import User
app = Flask(__name__)
app.secret_key = "random key for flask"  

@app.route("/")
def index():
    # call the get all classmethod to get all users
    return render_template("createUser.html")
    # return render_template("readAll.html", allUsers = listOfAllUsers)

# relevant code snippet from server.py
from user import User
@app.route('/create_user', methods=["POST"])
def create_User():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "firstName": request.form["firstName"],
        "lastName" : request.form["lastName"],
        "email" : request.form["email"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    User.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/showAllUser')

@app.route("/showAllUser")
def showAll():
    # call the get all classmethod to get all users
    listOfAllUsers = User.get_all()    
    print(session)
    return render_template("readAll.html", allUsers = listOfAllUsers)

            
if __name__ == "__main__":
    app.run(debug=True)