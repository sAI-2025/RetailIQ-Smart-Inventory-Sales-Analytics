import ast
import os

# Get the correct path for the machine_state.py file
MACHINE_STATE_PATH = os.path.join(os.path.dirname(__file__), 'machine_state.py')

def load_machine_state():
    """Loads the Product_live_stock_info dictionary from machine_state.py."""
    with open(MACHINE_STATE_PATH, 'r') as f:
        content = f.read()
        # Extract the part after "=" and evaluate it
        data_str = content.split('=', 1)[1].strip()
        return ast.literal_eval(data_str)

def write_machine_state(data):
    """Writes the updated Product_live_stock_info back to machine_state.py."""
    new_content = f"Product_live_stock_info = {repr(data)}\n"
    with open(MACHINE_STATE_PATH, 'w') as f:
        f.write(new_content)
