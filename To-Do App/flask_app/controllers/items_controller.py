from flask_app import app
from flask_app.models.item_model import Item
from flask import Flask, render_template, redirect, request

# Route to show all tasks (get all requestm using a render template)
# FIRST YOU NEED TO ALWAYS START WITH APP.ROUTE


@app.route("/")
# THEN DEFINE THE METHOD
def all_items():
    # Call the method from the models file to get all items
    all_items = Item.get_all()
    # AS A NIFTY TRICK, PRINT ALL_ITEMS IN THE CONSOLE TO SEE IF THIS REQUEST IS WORKING THE WAY IT SHOULD
    print(all_items)
    # RENDER THE CORRECT TEMPLATE AND INCLUDE THE ITEMS IN IT
    return render_template("all_tasks.html", all_items = all_items)


# Route to display the add a task form
@app.route("/items/new")
def add_task_form():
    return render_template("add_tasks.html")



# Route to add a task (add a task using a redirect)
# You need to pass in a URL endpoint, and include the method POST because you are creating a task
@app.route("/items/create", methods=["POST"])
# Define the method
def add_items():
    # Post an instance of the class via a form request
    Item.create(request.form)
    # Redirect to the get all page to view the task you just added, along with the others
    return redirect("/")




# Route to display one task (get one request using a render template)
@app.route("/items/<int:id>/view", methods=["GET"])
# Define the method
def get_one(id):
    # Create a dictionary that contains the id key-value pair
    data = {
        'id': id
    }
    # Store the instance of the Item class based on its ID in a variable
    one_item = Item.get_one(data)
    # Return the template to view that one item and  pass in the instance variable along with it
    return render_template("one_item.html", one_item=one_item)


# Route to edit a task
# FIRST PART IS TO LOAD THE TASK TO BE EDITED USING A RENDER TEMPLATE
@app.route("/items/<int:id>/edit")
def edit_one_item(id):
    this_specific_item = Item.get_one({"id": id})
    return render_template("edit_item.html", this_specific_item=this_specific_item)

# SECOND PART IS TO ACTUALLY UPDATE THE TASK


@app.route("/items/<int:id>/update", methods=['POST'])
def update_this_item(id):
    # Create a data dictionary where you set all of the inputs to the form
    data = {
        "id": id,
        "description": request.form["description"]
    }
    # Call the edit method in the model and pass in the data dictionary
    Item.edit_task(data)
    # Redirect to the all tasks page
    return redirect("/")


# Route for deleting a task (delete a task using a redirect)
@app.route("/items/<int:id>/delete")
def delete_this_task(id):
    Item.delete_task({"id": id})
    return redirect("/")
