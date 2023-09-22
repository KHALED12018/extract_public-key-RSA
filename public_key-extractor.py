import tkinter as tk
from tkinter import filedialog
from Crypto.PublicKey import RSA
import os

def extract_public_key(cert_file_path):
    try:
        with open(cert_file_path, 'rb') as cert_file:
            cert_data = cert_file.read()
        
        cert = RSA.import_key(cert_data)
        return cert.publickey().export_key()
    except FileNotFoundError:
        return None

def save_public_key(public_key, save_path):
    try:
        with open(save_path, 'wb') as key_file:
            key_file.write(public_key)
    except Exception as e:
        print(f"Error saving public key: {e}")

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("PEM Files", "*.pem")])
    file_path_label.config(text=f"File Path: {file_path}")

    public_key = extract_public_key(file_path)
    if public_key:
        public_key_text.config(text=f"Public Key:\n{public_key.decode()}")

        # Ask user where to save the public key
        save_path = filedialog.asksaveasfilename(defaultextension=".pem", filetypes=[("PEM Files", "*.pem")])
        if save_path:
            save_public_key(public_key, save_path)
            print(f"Public key saved to: {save_path}")
    else:
        public_key_text.config(text="Invalid or missing certificate file.")

app = tk.Tk()
app.title("Public Key Extractor by DEAGON-NOIR")
app.geometry("700x400")

file_path_label = tk.Label(app, text="File Path: ")
file_path_label.pack()

open_button = tk.Button(app, text="Open Certificate", command=open_file)
open_button.pack()

public_key_text = tk.Label(app, text="")
public_key_text.pack()

app.mainloop()
