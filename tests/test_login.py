
from pymongo import MongoClient
import bcrypt
# from app.constant import Constant

def test_login():
    client = MongoClient(host='mongodb+srv://phuchauxd12:Abcd0123@cluster0.lf8sh9p.mongodb.net/').get_database("dev")
    db = client.get_collection('USERS')
    user = "chau"
    password = "123"
    key = "0378459c951111ee9d9104ea5623eaeb"
    account = db.find_one({'username':user})
    assert account is not None
    assert bcrypt.checkpw(password.encode('utf-8'), account["password"].encode('utf-8'))
    assert account['key'] == key


def test_login_wrong_username():
    client = MongoClient(host='mongodb+srv://phuchauxd12:Abcd0123@cluster0.lf8sh9p.mongodb.net/').get_database("dev")
    db = client.get_collection('USERS')
    user = "chaurt"
    password = "123"
    key = "0378459c951111ee9d9104ea5623eaeb"
    account = db.find_one({'username':user})
    assert account is None

def test_login_wrong_password():
    client = MongoClient(host='mongodb+srv://phuchauxd12:Abcd0123@cluster0.lf8sh9p.mongodb.net/').get_database("dev")
    db = client.get_collection('USERS')
    user = "chau"
    password = "123wq"
    key = "0378459c951111ee9d9104ea5623eaeb"
    account = db.find_one({'username':user})
    assert account is not None
    assert bcrypt.checkpw(password.encode('utf-8'), account["password"].encode('utf-8')) == False
 
def test_login_wrong_key():
    client = MongoClient(host='mongodb+srv://phuchauxd12:Abcd0123@cluster0.lf8sh9p.mongodb.net/').get_database("dev")
    db = client.get_collection('USERS')
    user = "chau"
    password = "123"
    key = "0378459c951111ee9d9f04ea5623eaeb"
    account = db.find_one({'username':user})
    assert account is not None
    assert bcrypt.checkpw(password.encode('utf-8'), account["password"].encode('utf-8'))
    assert account['key'] != key

