from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

# Create a class


class Item:
    # Define the class
    def __init__(self, data):
        self.id = data['id']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


# post request to add tasks
    @classmethod
    # define the method name, here you are creating an instance of the class and passing the input as a data dictionary
    def create(cls, data):
        # This query will add the following input into the database
        query = """
        INSERT INTO items (description) VALUES(%(description)s);
        """
        # Return the data that was passed to the database
        return connectToMySQL(DATABASE).query_db(query, data)


# get request to view ALL tasks
    @classmethod
    # Define the method name, here we are simply doing a read all method to display every single task in our todo-list
    def get_all(cls):
        # This quert will pull all of the tasks in the items table
        query = """
        SELECT * FROM items;
        """
        # We need this to store the reults of the query in a variable
        results = connectToMySQL(DATABASE).query_db(query)
        # Create an empty list that we will append the results values into, in order to display the results
        all_items = []
        # Iterate through the results and append the values into the items list
        for one_item in results:
            # Create an instance of each item
            this_item_instance = cls(one_item)
            # append the instances into the empty list
            all_items.append(this_item_instance)
        # Return the appended list
        return all_items


# Get ONE task, primarily to edit or view details
    @classmethod
    # Define the method
    def get_one(cls, data):
        # Query the database for getting ONE task with the matching ID
        query = """
        SELECT * FROM items WHERE id=%(id)s;
        """
        # Store the query results in a variable called results
        results = connectToMySQL(DATABASE).query_db(query, data)
        # Using a condition, check if the query result exists
        if results:
            # If the query exists, then return the first matching item in the results variable
            return cls(results[0])
        # Add an else statement to finish off the condition
        return False


# put request to edit a task
    @classmethod
    # Define the method
    def edit_task(cls, data):
        # This query will edit an existing task/item in the database based on the ID of the task and the specific parameters that are being updated
        query = """
        UPDATE items SET description = %(description)s WHERE id=%(id)s;
        """
        # After the update query, we are simply returning the update, no need to get anything else, we are simply updating an existing the item in the database table
        return connectToMySQL(DATABASE).query_db(query, data)


# delete request to delete a task
    @classmethod
    # Define the method
    def delete_task(cls, data):
        # Add the delete query, which will delete a task in the database based on the ID of the task
        query = """
        DELETE FROM items WHERE id=%(id)s;
        """
        # Return the delete query
        return connectToMySQL(DATABASE).query_db(query, data)
