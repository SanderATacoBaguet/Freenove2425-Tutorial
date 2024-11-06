import os
import base64
import winreg as reg
import ctypes

# Base64 encoded cursor file (replace this with your actual Base64 string)
CURSOR_DATA = """
YOUR_BASE64_STRING_HERE
"""

def save_cursor(cursor_data, filename):
    # Decode the Base64 string and write it to a .cur file
    with open(filename, "wb") as cursor_file:
        cursor_file.write(base64.b64decode(cursor_data))
        print(f"Cursor saved to {filename}")

def change_cursor(cursor_path):
    # Set the cursor in the registry
    reg_path = r'Control Panel\Cursors'
    try:
        with reg.OpenKey(reg.HKEY_CURRENT_USER, reg_path, 0, reg.KEY_SET_VALUE) as cursor_key:
            # Change the default cursor
            reg.SetValueEx(cursor_key, 'Arrow', 0, reg.REG_SZ, cursor_path)
            print("Cursor changed successfully. You may need to log out or restart your PC.")
    except Exception as e:
        print(f"Failed to change cursor: {e}")

def main():
    # Specify the destination for the cursor file
    cursor_filename = r'C:\Windows\Cursors\my_cursor.cur'  # Make sure you have permission to write here

    # Save the cursor file from the embedded Base64 string
    save_cursor(CURSOR_DATA, cursor_filename)

    # Change the cursor if saved successfully
    change_cursor(cursor_filename)

    # Optional: Load new cursor immediately
    ctypes.windll.user32.SystemParametersInfoW(0x0057, 0, None, 0)

if __name__ == '__main__':
    main()
