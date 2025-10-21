import tkinter
from tkinter import *
from textblob import TextBlob
from tkinter import Tk, Label, RAISED
import tkinter as tk
import pyperclip
from plyer import notification

root = None  # Initialize as None
cliptext="Empty String"
#root = None  # Initialize as None

def send_notification():
    notification.notify(
        title='Sentiment!',
        message='This is the body of your notification.',
        #app_icon='path/to/your/icon.ico',  # Optional: Path to an .ico file on Windows
        timeout=10,  # Notification will disappear after 10 seconds
    )

""" This wis the main functin that is called on a timer
    It will grab text from the clipboard and then run the analyser
"""
def updateClipboard():
    global cliptext

    send_notification()
    cliptext = pyperclip.paste()
    analyze_sentiment()
    print(cliptext)
    #processClipping(cliptext=cliptext)
    root.after(ms=5000, func=updateClipboard)


def processClipping(cliptext):
    cliptextCleaned = cleanClipText(cliptext=cliptext)
    #label["text"] = cliptextCleaned


def cleanClipText(cliptext):
    #Removing all characters > 65535 (that's the range for tcl)
    cliptext = "".join([c for c in cliptext if ord(c) <= 65535])
    return cliptext


def onClick(labelElem):
    labelText = labelElem["text"]
    print(labelText)
    pyperclip.copy(labelText)


def get_clipboard_content():

    try:

        if root:  # Check if root is initialized
            root.iconify()  # Minimize the window
        else:
            print("Root window not yet created.")

        # Create a Tkinter root window (it won't be visible)
        #root.withdraw()  # Hide the main window

        # Retrieve the clipboard content
        clipboard_data = root.clipboard_get()

        # Destroy the root window after getting the data
        #root.destroy()

        return clipboard_data
    except tkinter.TclError:
        # Handle cases where the clipboard is empty or contains non-text data
        return "Clipboard is empty or contains non-text data."



def analyze_sentiment():
    text_input = text_area.get("1.0", "end-1c")  # Get text from the Text widget

    content = cliptext

    print("Cliptext is ",cliptext)

    analysis = TextBlob(content)
    #analysis = TextBlob(text_input)

    polarity = analysis.sentiment.polarity
    subjectivity = analysis.sentiment.subjectivity

    print(polarity)
    print(subjectivity)

    if polarity > 0:
        sentiment_label.config(text=f"Sentiment: Positive (Polarity: {polarity:.2f}, Subjectivity: {subjectivity:.2f})")
    elif polarity < 0:
        sentiment_label.config(text=f"Sentiment: Negative (Polarity: {polarity:.2f}, Subjectivity: {subjectivity:.2f})")
    else:
        sentiment_label.config(text=f"Sentiment: Neutral (Polarity: {polarity:.2f}, Subjectivity: {subjectivity:.2f})")




root = Tk()

root.title("Sentiment Analyzer")
# Create a Text widget for input
text_area = Text(root, height=10, width=50)
text_area.pack(pady=10)

# Create a button to trigger analysis
analyze_button = Button(root, text="Analyze Sentiment", command=analyze_sentiment)
analyze_button.pack(pady=5)

# Create a label to display results
sentiment_label = Label(root, text="Enter text and click 'Analyze'", wraplength=400)
sentiment_label.pack(pady=10)
updateClipboard()
root.mainloop()

"""
    label = Label(root, text="", cursor="plus", relief=RAISED, pady=5,  wraplength=500)
    label.bind("<Button-1>", lambda event, labelElem=label: onClick(labelElem))
    label.pack()
    updateClipboard()
    root.mainloop()
"""
