import tkinter as tk
from tkinter import filedialog, messagebox
        # filedialog → Opens “Save As” / “Open” dialog windows.
        # messagebox → Shows pop-up alerts (error messages).
import qrcode


# Simple QR code generator GUI using tkinter and qrcode

def set_status(message, error=False): # Updates the status message at the bottom of the window.
    status_var.set(message)
    status_label.config(fg="red" if error else "green")


def generate_qr():
    url = url_var.get().strip() # getting user input from the entry field and stripping whitespace
   
    if not url:
        # No input provided then call set_status to show error message
        set_status("Please enter a link or text to encode.", error=True)
        return

    try:
        # inishialize QR code object with smallest size and box size of 8 pixels and border of 4 boxes
        qr = qrcode.QRCode(version=1, box_size=8, border=4) 

        qr.add_data(url) # Add the user input data to the QR code object
        qr.make(fit=True) # Generate the QR code  fit=True automatically adjusts the size of the QR code to fit the data

        img = qr.make_image(fill_color="black", back_color="white") # Create an image from the QR code object with black and white colors uusing pil

        app_state["qr_image"] = img
        save_btn.config(state=tk.NORMAL)
        set_status("QR code ready. Click 'Save QR as PNG'.")

    except Exception as exc:
        
        save_btn.config(state=tk.DISABLED)
        app_state["qr_image"] = None
        messagebox.showerror("QR Error", f"Could not generate QR code.\n{exc}")
        set_status("QR generation failed.", error=True)


def save_qr():
    img = app_state.get("qr_image")
    if img is None:
        set_status("Generate a QR code before saving.", error=True)
        return

    file_path = filedialog.asksaveasfilename(
        title="Save QR Code",
        defaultextension=".png",
        filetypes=[("PNG Image", "*.png"), ("All Files", "*.*")],
    )
    if not file_path:
        set_status("Save canceled.")
        return

    try:
        img.save(file_path)
        set_status(f"Saved to {file_path}")
    except Exception as exc:
        messagebox.showerror("Save Error", f"Could not save QR code.\n{exc}")
        set_status("Save failed.", error=True)


app_state = {"qr_image": None}

window = tk.Tk()
window.title("QR Code Generator")
window.geometry("420x220")
window.resizable(False, False)
window.configure(padx=16, pady=16)

title_label = tk.Label(window, text="Generate a QR Code", font=("Arial", 16, "bold"))
title_label.grid(row=0, column=0, columnspan=2, sticky="w")

instruction = tk.Label(
    window,
    text="Enter a link or any text below, then click Generate.",
    font=("Arial", 10),
)
instruction.grid(row=1, column=0, columnspan=2, sticky="w", pady=(4, 10))

url_var = tk.StringVar()
url_entry = tk.Entry(window, textvariable=url_var, width=45, font=("Arial", 12))
url_entry.grid(row=2, column=0, columnspan=2, sticky="we", pady=(0, 10))
url_entry.focus()

generate_btn = tk.Button(
    window,
    text="Generate QR",
    command=generate_qr,
    font=("Arial", 11, "bold"),
    width=14,
)
generate_btn.grid(row=3, column=0, sticky="we", padx=(0, 6))

save_btn = tk.Button(
    window,
    text="Save QR as PNG",
    command=save_qr,
    font=("Arial", 11, "bold"),
    width=14,
    state=tk.DISABLED,
)
save_btn.grid(row=3, column=1, sticky="we", padx=(6, 0))

status_var = tk.StringVar(value="Ready.")
status_label = tk.Label(window, textvariable=status_var, font=("Arial", 10), fg="green")
status_label.grid(row=4, column=0, columnspan=2, sticky="w", pady=(12, 0))

window.bind("<Return>", lambda event: generate_qr())
window.mainloop()
