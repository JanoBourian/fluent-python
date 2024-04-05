import contextlib

class Operation:
    
    def __enter__(self):
        print("Entering...")
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting...")
        
    def some_operation(self):
        print("Operation...")
        
@contextlib.contextmanager
def managed_class(*args, **kwargs):
    try:
        print("Working...")
        yield Operation()
    except Exception as e:
        print(f"Something was wrong: {e}")
    finally:
        print("Closing...")

def some_function():
    print("Yield was returned...")

@contextlib.contextmanager
def managed_resources(*args, **kwargs):
    try:
        print("Working...")
        yield some_function()
    except Exception as e:
        print(f"Something was wrong: {e}")
    finally:
        print("Closing...")

class ContextM:
    
    def __enter__(self):
        print("Entering...")
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting...")
        
with ContextM() as context:
    print(context)
    print("something")

print("##########################")

with managed_resources() as mr:
    print("in with statement...")

print("##########################")

with managed_class() as op:
    print(op)
    with op.some_operation() as sop:
        print("in with statement...")