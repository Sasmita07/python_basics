from fixtures.mydb import MyDb
import pytest

# setup and teardown method
# conn = None
# cur = None

# def setup_module():
#     global conn
#     global cur
#     db = MyDb()
#     conn = db.connect("connection_string")
#     cur = conn.cursor()

# def teardown_module():
#     cur.close()
#     conn.close()

# fixture leverage the concept of dependecy injection py.test -v --capture=no
@pytest.fixture(scope="module")
def cur():
    print("setting up the Db")
    db = MyDb()
    conn = db.connect("connection_string")
    curs = conn.cursor()
    yield curs
    curs.close
    conn.close
    print("closing the Db")

def test_john_id(cur):
    id = cur.execute('select employee_id from employee_db where name = "John"')
    assert id == 123

def test_tom_id(cur):
    id = cur.execute('select employee_id from employee_db where name = "Bob"')
    assert id == 456
