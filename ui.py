import pygame
import customtkinter as ctk
import practice

# Initialize pygame mixer for audio playback
pygame.mixer.init()

# Fake data
songs = ["Interstellar Main Theme"]
song_files = {
    "Interstellar Main Theme": "Interstellar Main Theme.mp3",
}

# Global variable to track if dynamics should be used
use_dynamics = False

# Global variable to track if right or left hand should be used
use_right_hand = False
use_left_hand = False

def toggle_dynamics():
    global use_dynamics
    use_dynamics = dynamics_checkbox.get()
    status_label.configure(text=f"Dynamics {'enabled' if use_dynamics else 'disabled'}.")

def toggle_right_hand():
    global use_right_hand
    use_right_hand = right_hand_checkbox.get()
    status_label.configure(text=f"Right Hand {'enabled' if use_right_hand else 'disabled'}.")

def toggle_left_hand():
    global use_left_hand
    use_left_hand = right_hand_checkbox.get()
    status_label.configure(text=f"Right Hand {'enabled' if use_left_hand else 'disabled'}.")

def listen_to_song():
    selected = selected_song.get()
    if selected in song_files:
        song_path = song_files[selected]
        try:
            pygame.mixer.music.load(song_path)
            pygame.mixer.music.play()
            status_label.configure(text=f"Listening to {selected}...")
        except Exception as e:
            status_label.configure(text=f"Error playing song: {e}")
    else:
        status_label.configure(text="No audio file found for the selected song.")

def stop_song():
    pygame.mixer.music.stop()
    status_label.configure(text="Song stopped.")

def start_practice():
    # Start the practice mode
    status_label.configure(text="Practice mode started.")
    practice.start_practice_mode("Interstellar Main Theme.mid", use_right_hand, use_left_hand, use_dynamics)


# Configure the appearance of the UI
ctk.set_appearance_mode("Dark")  # Options: "Light", "Dark", "System"
ctk.set_default_color_theme("blue")  # Options: "blue", "dark-blue", "green"

# Main application window
root = ctk.CTk()
root.title("Hand Lights Controller")
root.geometry("600x600")

# Status display
status_label = ctk.CTkLabel(root, text="Welcome! Choose a song to get started.", wraplength=500, font=("Arial", 14))
status_label.pack(pady=10)

# Song selection
selected_song = ctk.StringVar(value=songs[0])
ctk.CTkLabel(root, text="Choose a Song:", font=("Arial", 16)).pack(pady=10)
song_menu = ctk.CTkOptionMenu(root, variable=selected_song, values=songs)
song_menu.pack(pady=10)

# Listen to the song
listen_button = ctk.CTkButton(root, text="Listen to Song", command=listen_to_song)
listen_button.pack(pady=10)

# Stop the song
stop_button = ctk.CTkButton(root, text="Stop Song", command=stop_song)
stop_button.pack(pady=10)

# Song selection
selected_song = ctk.StringVar(value=songs[0])
ctk.CTkLabel(root, text="Select your options:", font=("Arial", 16)).pack(pady=10)

# Dynamics checkbox
dynamics_checkbox = ctk.BooleanVar(value=False)
ctk.CTkCheckBox(root, text="Use Dynamics", variable=dynamics_checkbox, command=toggle_dynamics).pack(pady=10)

# Right hand checkbox
right_hand_checkbox = ctk.BooleanVar(value=False)
ctk.CTkCheckBox(root, text="Use Right Hand", variable=right_hand_checkbox, command=toggle_right_hand).pack(pady=10)

# Left hand checkbox
left_hand_checkbox = ctk.BooleanVar(value=False)
ctk.CTkCheckBox(root, text="Use Left Hand", variable=left_hand_checkbox, command=toggle_left_hand).pack(pady=10)

# Start practice mode
start_button = ctk.CTkButton(root, text="Start", command=start_practice)
start_button.pack(pady=10)

# Run the application
root.mainloop()

# Quit pygame mixer when the application exits
pygame.mixer.quit()
