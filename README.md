#Hello-books
this is an online library application, where a user can register, login, view books, borrow books, return books.
the tests are wriiten using TDD and run using the 'unittest' module. They cover the basic CRUD functionalities of Add,
Delete, Modify. There are also related files with the classes and respective methods required to satisy the test
requirements
### Prerequisites

- Python3.5 and above
- Python virtualenv
- Flask
type on the command line:
```
python -V
```
If your version is anything below python 3.5 the application will not run properly
### Installing

Make sure you are still in the app directory and that python3 is running on a virtual environemnt by doing the following:

1. Create your virtual environment:
```
python -m venv venv
```
2. Start your virtual environment:
```
source venv/bin/activate
```
3. Install the project requirements specified in the requirements.txt file. Usually,
```
pip install -r requirements.txt
```
## Built With

* [Python Flask](https://www.fullstackpython.com/flask.html) - The web framework used