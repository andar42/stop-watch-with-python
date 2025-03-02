import tkinter as tk
window = tk.Tk()


class StopwatchApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Stopwatch")
        self.window.geometry("300x200")

        self.time = 0
        self.running = False

        
        self.label = tk.Label(window, text="00:00:00", font=("Arial", 30),fg="green")
        self.label.pack(pady=20)
       # icon = tk.PhotoImage(file="C:\\Users\\N.C.S\\Desktop\\tkinter\\OIP (2).jpeg")
       # self.window.iconphoto(False, icon)
        self.window.config(bg="red")

        
        self.start_button = tk.Button(window, text="Start", command=self.start, width=10)
        self.start_button.pack()

        self.stop_button = tk.Button(window, text="Stop", command=self.stop, width=10)
        self.stop_button.pack()

        self.reset_button = tk.Button(window, text="Reset", command=self.reset, width=10)
        self.reset_button.pack()

    def update_timer(self):
        if self.running:
            self.time += 1
            minutes, seconds = divmod(self.time, 60)
            hours, minutes = divmod(minutes, 60)
            self.label.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")
            self.window.after(1000, self.update_timer)

    def start(self):
        if not self.running:
            self.running = True
            self.update_timer()

    def stop(self):
        self.running = False

    def reset(self):
        self.running = False
        self.time = 0
        self.label.config(text="00:00:00")


app = StopwatchApp(window)
window.mainloop()
