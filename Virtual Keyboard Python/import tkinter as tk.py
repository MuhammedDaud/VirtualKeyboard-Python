import tkinter as tk
from tkinter import ttk

class VirtualKeyboard(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Virtual Keyboard")
        self.geometry("900x400")
        self.resizable(0, 0)
        
        self.caps_lock_on = False
        self.input_text = tk.StringVar()
        
        self.create_widgets()
        
    def create_widgets(self):
        input_frame = ttk.Frame(self, padding="10")
        input_frame.pack(pady=10)

        input_entry = ttk.Entry(input_frame, textvariable=self.input_text, font=("Arial", 24), width=40)
        input_entry.pack()

        keyboard_frame = ttk.Frame(self)
        keyboard_frame.pack(pady=20)

        self.keys = [
            ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'Backspace'],
            ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
            ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'Enter'],
            ['CapsLock', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '.', 'Space']
        ]

        for row in self.keys:
            row_frame = ttk.Frame(keyboard_frame)
            row_frame.pack()

            for key in row:
                button = ttk.Button(row_frame, text=key, width=10, command=lambda k=key: self.on_key_press(k))
                button.pack(side=tk.LEFT, padx=5, pady=5)
                
                button.bind("<Enter>", self.on_hover)
                button.bind("<Leave>", self.on_leave)

    def on_hover(self, event):
        """Changes button color on hover"""
        event.widget.config(style="Hover.TButton")

    def on_leave(self, event):
        """Restores button color when mouse leaves"""
        event.widget.config(style="TButton")
    
    def on_key_press(self, key):
        if key == "Space":
            self.input_text.set(self.input_text.get() + " ")
        elif key == "Backspace":
            self.input_text.set(self.input_text.get()[:-1])
        elif key == "Enter":
            self.input_text.set(self.input_text.get() + "\n")
        elif key == "CapsLock":
            self.caps_lock_on = not self.caps_lock_on
        else:
            if self.caps_lock_on:
                self.input_text.set(self.input_text.get() + key.upper())
            else:
                self.input_text.set(self.input_text.get() + key.lower())

if __name__ == "__main__":
    style = ttk.Style()
    style.configure("TButton", font=("Arial", 18))
    style.configure("Hover.TButton", background="lightblue", foreground="black")
    
    app = VirtualKeyboard()
    app.mainloop()

