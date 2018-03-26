from flask import request
from flask import session
from flask import flash
from flask import url_for, redirect, render_template
from Project2.app.borrowlist import BorrowList
from Project2.app.admin import BorrowListAdmin
from Project2.user.user import User

from Project2 import app
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
@app.route()