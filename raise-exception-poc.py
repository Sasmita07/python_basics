class Accident(Exception):
    def __init__(self, msg):
        self.msg = msg

    def print_exception(self):
        print("User defined exception:", self.msg)


try:
    raise Accident('Accident error')
except Accident as e:
    print("Error Occured is:", e)
    e.print_exception()

# built-in exception
try:
    raise MemoryError('Memory error')
except MemoryError as e:
    print("Error Occured is:", e)


# finally usage
def process_file():
    try:
        f = open("/Users/sas_vsCodeWorkspace/python_basics/file1.txt")
        x = 10/0
    except FileNotFoundError as e:
        print("Error Occured is:", e)
    finally:
        print("Close the file")
        f.close()

process_file()