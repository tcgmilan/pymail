from src import email_sender
import tkinter as tk

class Panels:
    def __init__(self):
        self.email_client = email_sender.NewClient()

    def show_login_panel(self):
        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.root.title("PyMail - Login Panel")
        
        username_label = tk.Label(self.root, text = "Email Adress").grid(row = 0, column = 0)
        username = tk.StringVar()
        username_entry = tk.Entry(self.root, textvariable = username).grid(row = 0, column = 1)

        password_label = tk.Label(self.root, text = "Password").grid(row = 1, column = 0)
        password = tk.StringVar()
        password_entry = tk.Entry(self.root, textvariable = password).grid(row = 1, column = 1)
        
        login_button = tk.Button(self.root, text = "Login", command = lambda: self.login_to_client(self.root, username.get(), password.get())).grid(row = 4, column = 0)

        self.root.mainloop()

    def show_email_panel(self):
        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.root.title("PyMail - Mail Panel")

        name_label = tk.Label(self.root, text = "Your Name").grid(row = 0, column = 0)
        name = tk.StringVar()
        name_entry = tk.Entry(self.root, textvariable = name).grid(row = 0, column = 1)

        target_label = tk.Label(self.root, text = "Target Email Adress").grid(row = 1, column = 0)
        target = tk.StringVar()
        target_entry = tk.Entry(self.root, textvariable = target).grid(row = 1, column = 1)
        
        subject_label = tk.Label(self.root, text = "Subject").grid(row = 2, column = 0)
        subject = tk.StringVar()
        subject_entry = tk.Entry(self.root, textvariable = subject).grid(row = 2, column = 1)
     
        content_label = tk.Label(self.root, text = "Content").grid(row = 3, column = 0)
        content_text = tk.Text(self.root)
        content_text.grid(row = 3, column = 1)
        content = content_text.get("1.0", "end")

        send_button = tk.Button(self.root, text = "Send", command = lambda: self.send_email(self.root, name.get(), target.get(), subject.get(), content)).grid(row = 4, column = 0)


        self.root.mainloop()
    def login_to_client(self, root, username, password):
        result = self.email_client.login_client(username, password)
        if result == 1:
            root.destroy()
            self.show_email_panel()

    def send_email(self, root, email_from, email_to, email_subject, email_content):
        result = self.email_client.new_message(email_from, email_to, email_subject, email_content)
        if result == 1:
            root.destroy()
            self.show_email_panel()
