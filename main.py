import webview
import os
import sys

# This part helps the EXE find the HTML file after it's bundled
def get_resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# Create the window
window = webview.create_window(
    'FocusFlow Multi-Pro', 
    get_resource_path('index.html'),
    width=1100,
    height=800
)

if __name__ == '__main__':
    webview.start()