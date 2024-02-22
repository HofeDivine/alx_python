from flask import Flask, request, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import re
import sys

# Check for command-line arguments
if len(sys.argv) != 4:
    print("Usage: python 8-add_retrieve_users.py <db_username> <db_password> <db_name>")
    sys.exit(1)

db_username = sys.argv[1]
db_password = sys.argv[2]
db_name = sys.argv[3]
db_host = 'localhost'

app = Flask(__name__)

############################# TO DO 1 ############################
# Configure Database Connection
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{db_username}:{db_password}@{db_host}/{db_name}"

###############################################################

db = SQLAlchemy(app)

############################  TO DO 2 ##############################
# Define User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

#################################################################

# Create the database tables
def create_tables():
    with app.app_context():
        db.create_all()

create_tables()  # This calls the function to create tables


@app.route('/', strict_slashes=False)
def index():
    return "Hello, ALX Flask!"
@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        try:
            new_user = User(name=name, email=email)
            db.session.add(new_user)
            db.session.commit()
            flash("User added successfully!")
        except Exception as e:
            db.session.rollback()
            flash("Error: " + str(e), "error")
    return render_template('add_user.html')
@app.route('/users')
def show_users():
    
    users = User.query.all()

    
    return render_template('users.html', users=users)


@app.route('/update_user/<int:user_id>', methods=['GET', 'POST'])
def update_user(user_id):
    if request.method == 'POST':
        
        updated_name = request.form.get('name')
        updated_email = request.form.get('email')
        
        
        if not updated_name or not updated_email:
            flash("Both name and email fields are required.", "error")
            return redirect(url_for('update_user', user_id=user_id))
        
        
        user = User.query.get(user_id)
        
    
        if not user:
            flash("User not found.", "error")
            return redirect(url_for('update_user', user_id=user_id))
        
    
        existing_user = User.query.filter_by(email=updated_email).first()
        if existing_user and existing_user.id != user_id:
            flash("Email already taken by another user.", "error")
            return redirect(url_for('update_user', user_id=user_id))
        
        try:
            user.name = updated_name
            user.email = updated_email

            db.session.commit()
            flash("User updated successfully!", "success")
        except Exception as e:
        
            db.session.rollback()
            
            
            flash(f"Error: {str(e)}", "error")
    return render_template('update_user.html', user=user)
from flask import flash, redirect, url_for

@app.route('/delete_user/<int:user_id>')
def delete_user(user_id):

    user = User.query.get(user_id)
    
    
    from flask import render_template

@app.route('/delete_user/<int:user_id>', methods=['GET'])
def delete_user(user_id):
    # Retrieve the user from the database based on user_id
    user = User.query.get(user_id)
    
    # Check if the user exists
    if user:
        return render_template('delete_user.html', user=user)
    else:
        flash("User not found.", "error")
        return redirect(url_for('index'))




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)