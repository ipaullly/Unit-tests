from flask import request
from flask import session
from flask import flash
from flask import url_for, redirect, render_template
from app.borrowlist.borrowlist import BorrowList
from app.borrowlist.admin import BorrowListAdmin
from app.user.user import User

from app import app
#for the case of non-persistent, we require a list for authenticated user
authenticated_users = []
#creating user account

@app.route('/api/v1/auth/register', methods=['POST'])
def register():
    email = request.form.get('email')
    password = request.form.get('password')
    name = request.form.get('username')
    for user in authenticated_users:
        if user.email == email:
            flash('{} is already registered, please login.'.format(email))
            return render_template("index.html")
    user = User(email, password, name)
    authenticated_users.append(user)
    flash("{} has succesfully created an account.".format(user.name))
    return redirect('/')

#api endpoint for log in
@app.route('/api/v1/auth/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    for user in authenticated_users:
        if user.email == email:
            if user.password == password:
                session['logged_in'] = True
                session['user'] = email
                return redirect(url_for("Profile page"))
            else:
                flash("wrong login details")
                return render_template("index.html")
    flash("You are not among the authenticated user list")
    return redirect("/")
#api to logout 
@app.route('/api/v1/auth/logout', methods=['POST'])
def logout():
    session['logged_in'] = False
    session.pop('user', None)
    flash("You have signed out")
    return redirect("/")
#creating an object for the user session required to CRUD the borrowlists and borrowlist_items
def get_session_user():
    for user in authenticated_users:
        if user.email == session['user']:
            return user

# to create a borrowlist item (book) in a borrowlist
@app.route('/api/v1/books', methods=['POST'])
def add_borrowlist_item(borrowlist_name):
       
        name = request.form.get('borrowlist_item_name')
        category = str(request.form.get('book_category'))
        description = request.form.get('borrowlist_item_description')
        borrowlist_item_details = (name, category, description)
        
        if get_session_user() is not None:
             session_user = get_session_user()
             for borrowlist in session_user.available_borrowlists:
                 if str(borrowlist) == borrowlist_name:
                     target_index = session_user.available_borrowlists.index(borrowlist)
                     target_borrowlist = session_user.available_borrowlists[target_index]
                     add_item = target_borrowlist.add_item(borrowlist_item_details, owner=session_user)
                     flash(add_item[1])
                     return redirect("/")
        flash("You currently not in session.")
        return redirect("/")
#to view all books
@app.route('/api/v1/books', methods=['GET'])
def display_borrowlist_items(borrowlist_name):
    if get_session_user() is not None:
        session_user = get_session_user()
        for borrowlist in session_user.available_borrowlists:
            if str(borrowlist) == borrowlist_name:
                target_index = session_user.available_borrowlists.index(borrowlist)
                target_borrowlist = session_user.available_borrowlists[target_index]
                items = target_borrowlist.items
                empty_borrowlist = (len(items) == 0)
                flash("You can view books from {} category below.".format(target_borrowlist))
                return render_template("View-all-books.html", borrowlist=target_borrowlist, username=get_session_user().name, empty_borrowlist=empty_borrowlist, session_user=session_user)
            else:
                flash("You are not on session")
                return render_template("index.html")
    
#The API that sends information to update borrowlist items (books)
@app.route('/api/v1/books/<bookld>', methods=['PUT'])
def modify_borrowlist_item(borrowlist_name, item_name):
    name = request.form.get('item_name')
    description = request.form.get('item_desc')
    category = str(request.form.get('item_category'))
    new_details = (name, category, description)

    if get_session_user is not None:
        session_user = get_session_user()
        for borrowlist in session_user.available_borrowlists:
            if str(borrowlist) == borrowlist_name:
                target_index = session_user.available_borrowlists.index(borrowlist)
                target_borrowlist = session_user.available_borrowlists[target_index]
                for borrowlist_item in target_borrowlist.items:
                    if str(borrowlist_item) == item_name:
                        update_item = target_borrowlist.update_item(borrowlist_item, new_details)
                        flash(update_item)
                        return redirect("/")
                    flash("The borrowlist item you are trying to modify is not available")
                    return redirect("/")
    flash("You are not on session")
    return redirect("/")


#the API that removes a borrowlist item(book) from a borrowlist
@app.route('/api/v1/books/<bookld>', methods=['DELETE'])
def delete_borrowlist_item(borrowlist_name, item_name):
    if get_session_user is not None:
        session_user = get_session_user()
        for borrowlist in session_user.available_borrowlists:
            if str(borrowlist) == borrowlist_name:
                target_index = session_user.available_borrowlists.index(borrowlist)
                target_borrowlist = session_user.available_borrowlists[target_index]
                for borrowlist_item in target_borrowlist.items:
                    if str(borrowlist_item) == item_name:
                        delete_item = target_borrowlist.remove_item(borrowlist_item)
                        flash(delete_item)
                        return redirect("/")
                flash("the borrowlist item you are trying to delete does not exist on this borrowlist")
                return redirect("/")
        flash("You are not in a session")
        return redirect("/")

