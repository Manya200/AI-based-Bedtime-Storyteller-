import os.path
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog
import threading
from PIL import ImageTk, Image
from moviepy.editor import VideoFileClip
from Story_maker import printinfo
import subprocess

subprocess.run(["python", "video_player.py"])

class BedtimeStoryTellerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bedtime Story Teller")
        self.root.geometry('1366x768')

        self.create_canvas()
        self.load_background_image()
        self.create_input_fields()
        self.create_buttons()

    def create_canvas(self):
        self.canvas = tk.Canvas(self.root, bg='#0096DC')
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def load_background_image(self):
        bg_image = Image.open("BEITproject.png")
        bg_image = bg_image.resize((1366, 768))
        self.bg_img = ImageTk.PhotoImage(bg_image)
        self.img_label = Label(self.canvas, image=self.bg_img)
        self.img_label.place(relwidth=1, relheight=1)

    def create_input_fields(self):
        self.character1_name = tk.Entry(self.canvas, width=50)
        self.character1_name.place(x=874, y=141, width=400, height=30)
        # other fields...

        self.character1_type = tk.Entry( self.canvas, width=50 )
        self.character1_type.place( x=874, y=206, width=400, height=30 )

        self.character2_name = tk.Entry( self.canvas, width=50 )
        self.character2_name.place( x=874, y=286, width=400, height=30 )

        self.character2_type = tk.Entry( self.canvas, width=50 )
        self.character2_type.place( x=874, y=359, width=400, height=30 )

        self.venue = tk.Entry( self.canvas, width=50 )
        self.venue.place( x=874, y=427, width=400, height=30 )

        self.genre = tk.Entry( self.canvas, width=50 )
        self.genre.place( x=874, y=496, width=400, height=30 )

        self.path_entry = tk.Entry( self.canvas, width=50 )
        self.path_entry.place( x=874, y=554, width=400, height=30 )


    def create_buttons(self):
        img1 = Image.open("photo_2024-02-26_15-18-07.jpg")
        img1 = img1.resize((200, 53), Image.ANTIALIAS) if hasattr(Image, 'ANTIALIAS') else img1.resize((200, 53))
        self.browse_image = ImageTk.PhotoImage(img1)
        self.select_folder_button = tk.Button(self.canvas, image=self.browse_image, command=self.select_folder,
                                              borderwidth=0, cursor= "hand2")
        self.select_folder_button.place(x=669, y=554)

        img2 = Image.open("photo_2024-02-26_14-23-41.jpg")
        img2 = img2.resize((200, 53), Image.ANTIALIAS) if hasattr(Image, 'ANTIALIAS') else img2.resize((200, 53))
        self.submit_image = ImageTk.PhotoImage(img2)
        self.store_run_button = tk.Button(self.canvas, image=self.submit_image, command=self.runall, borderwidth=0, cursor="hand2")
        self.store_run_button.place(x=400, y=554)

    def select_folder(self):
        self.root.withdraw()
        path = filedialog.askdirectory()
        folder_name = os.path.basename(path)
        self.path_entry.delete(0, tk.END)
        self.path_entry.insert(0, folder_name)
        subprocess.run(["python", "Story_Reader.py", path])
        self.root.deiconify()

    def play_video(self, video_path, callback):
        clip = VideoFileClip(video_path)
        clip.preview()
        clip.close()
        self.root.deiconify()  # Bring back the main window when video playback is complete
        callback()  # Trigger the callback function after video playback

    def display_video_window(self, video_path, callback):
        self.root.withdraw()  # Temporarily hide the main window
        self.video_window_thread = threading.Thread(target=self.play_video, args=(video_path, callback))
        self.video_window_thread.start()

    def close_video_window(self):
        if self.video_window_thread:
            self.video_window_thread.join()
        self.root.quit()

    def on_closing(self):
        if messagebox.askokcancel("Close Window", "Are you sure you want to close the window?"):
            self.close_video_window()

    def run_printinfo(self):
        try:
            result = printinfo(self.character1_name.get(), self.character1_type.get(), self.character2_name.get(),
                               self.character2_type.get(), self.venue.get(), self.genre.get())
            if result.get("status") == "success":
                messagebox.showinfo("Story Creation Successful", f"Your files are in {result['directory']}.")
                self.path_entry.delete(0, tk.END)
                self.path_entry.insert(0, result["directory"])
            elif result.get("status") == "error":
                messagebox.showerror("Story Creation Unsuccessful", result.get("error_message", "Unknown error"))
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during story generation: {e}")

    def runall(self):
        try:
            self.display_video_window("story genration video.mp4", self.run_printinfo)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = BedtimeStoryTellerApp(root)
    root.mainloop()
