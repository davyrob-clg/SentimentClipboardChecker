import tkinter as tk

def get_clipboard_content():
    try:
        # Create a Tkinter root window (it won't be visible)
        root = tk.Tk()
        root.withdraw()  # Hide the main window

        # Retrieve the clipboard content
        clipboard_data = root.clipboard_get()

        # Destroy the root window after getting the data
        root.destroy()

        return clipboard_data
    except tk.TclError:
        # Handle cases where the clipboard is empty or contains non-text data
        return "Clipboard is empty or contains non-text data."

if __name__ == "__main__":
    content = get_clipboard_content()
    print("Clipboard content:", content)