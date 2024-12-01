import pygame
import customtkinter as ctk

# Initialize pygame mixer for audio playback
pygame.mixer.init()

# Fake data
songs = ["Twinkle Twinkle Little Star", "Jingle Bells", "Für Elise"]
song_files = {
    "Twinkle Twinkle Little Star": "twinkle.mp3",  # Replace with actual file paths
    "Jingle Bells": "jingle_bells.mp3",
    "Für Elise": "fur_elise.mp3"
}

scoreboard = [("Alice", 95), ("Bob", 88), ("Charlie", 72)]

# Global variable to track if dynamics should be used
use_dynamics = False

def toggle_dynamics():
    global use_dynamics
    use_dynamics = dynamics_checkbox.get()
    status_label.configure(text=f"Dynamics {'enabled' if use_dynamics else 'disabled'}.")

def validate_dynamics(note_loudness, expected_loudness):
    """Simulate dynamics detection logic."""
    if not use_dynamics:
        return True  # Always valid if dynamics are disabled
    return abs(note_loudness - expected_loudness) <= 5  # Allowable threshold

def start_practice_mode():
    status_label.configure(text="Practice Mode Started! Enjoy playing at your own pace.")

def start_competitive_mode():
    status_label.configure(text="Competitive Mode Started! Score will be tracked.")

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

def update_scoreboard():
    score_text = "\n".join([f"{name}: {score}" for name, score in scoreboard])
    scoreboard_label.configure(text=score_text)

# Configure the appearance of the UI
ctk.set_appearance_mode("Dark")  # Options: "Light", "Dark", "System"
ctk.set_default_color_theme("blue")  # Options: "blue", "dark-blue", "green"

# Main application window
root = ctk.CTk()
root.title("Hand Lights Controller")
root.geometry("600x600")

# Song selection
selected_song = ctk.StringVar(value=songs[0])
ctk.CTkLabel(root, text="Choose a Song:", font=("Arial", 16)).pack(pady=10)
song_menu = ctk.CTkOptionMenu(root, variable=selected_song, values=songs)
song_menu.pack(pady=10)

# Mode selection
ctk.CTkLabel(root, text="Choose a Mode:", font=("Arial", 16)).pack(pady=10)

modes_frame = ctk.CTkFrame(root)
modes_frame.pack(pady=10)

practice_button = ctk.CTkButton(modes_frame, text="Practice Mode", command=start_practice_mode)
practice_button.grid(row=0, column=0, padx=10, pady=10)

competitive_button = ctk.CTkButton(modes_frame, text="Competitive Mode", command=start_competitive_mode)
competitive_button.grid(row=0, column=1, padx=10, pady=10)

# Dynamics checkbox
dynamics_checkbox = ctk.BooleanVar(value=False)
ctk.CTkCheckBox(root, text="Use Dynamics", variable=dynamics_checkbox, command=toggle_dynamics).pack(pady=10)

# Listen to the song
listen_button = ctk.CTkButton(root, text="Listen to Song", command=listen_to_song)
listen_button.pack(pady=10)

# Stop the song
stop_button = ctk.CTkButton(root, text="Stop Song", command=stop_song)
stop_button.pack(pady=10)

# Status display
status_label = ctk.CTkLabel(root, text="Welcome! Choose a song and mode to get started.", wraplength=500, font=("Arial", 14))
status_label.pack(pady=10)

# Scoreboard
ctk.CTkLabel(root, text="Scoreboard", font=("Arial", 16)).pack(pady=10)
scoreboard_label = ctk.CTkLabel(root, text="", wraplength=500, font=("Arial", 14))
scoreboard_label.pack()

# Update the fake scoreboard
update_scoreboard()

# Run the application
root.mainloop()

# Quit pygame mixer when the application exits
pygame.mixer.quit()
