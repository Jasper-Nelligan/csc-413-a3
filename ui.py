import pygame
import customtkinter as ctk
import practice
import competitive

# Initialize pygame mixer for audio playback
pygame.mixer.init()

# Fake data
songs = ["Interstellar Main Theme"]
song_files = {
    "Interstellar Main Theme": "Interstellar Main Theme.mp3",
}
scoreboard_data = [("Alice", 95), ("Bob", 88), ("Charlie", 72)]

def enter_practice_mode():
    clear_options()
    add_practice_options()

def start_practice_mode():
    status_label.configure(text="Practice Started!")

    use_dynamics = dynamics_var.get()
    use_right_hand = right_hand_var.get()
    use_left_hand = left_hand_var.get()

    practice.start_practice_mode("Interstellar Main Theme.mid", use_dynamics, use_right_hand, use_left_hand)

def enter_competitive_mode():
    clear_options()
    add_competitive_options()
    update_scoreboard()

def start_competitive_mode():
    status_label.configure(text="Competitive Started!")
    print("Competitive Started!")
    score = competitive.start_competitive_mode("Interstellar Main Theme.mid")
    print(f"Score: {score}")
    scoreboard_data.append(("You", score))
    update_scoreboard()

def start_listen_mode():
    selected = selected_song.get()
    if selected in song_files:
        try:
            pygame.mixer.music.load(song_files[selected])
            pygame.mixer.music.play()
            status_label.configure(text=f"Listening to {selected}...")
        except Exception as e:
            status_label.configure(text=f"Error playing song: {e}")
    else:
        status_label.configure(text="No audio file found for the selected song.")

def stop_song():
    pygame.mixer.music.stop()
    status_label.configure(text="Song stopped.")

def clear_options():
    for widget in options_frame.winfo_children():
        widget.destroy()
    scoreboard_label.pack_forget()  # Hide scoreboard when not in Competitive Mode

def add_practice_options():
    dynamics_checkbox = ctk.CTkCheckBox(
        options_frame, text="Use Dynamics", variable=dynamics_var
    )
    dynamics_checkbox.pack(pady=5)

    right_hand_checkbox = ctk.CTkCheckBox(
        options_frame, text="Use Right Hand", variable=right_hand_var
    )
    right_hand_checkbox.pack(pady=5)

    left_hand_checkbox = ctk.CTkCheckBox(
        options_frame, text="Use Left Hand", variable=left_hand_var
    )
    left_hand_checkbox.pack(pady=5)

    start_button = ctk.CTkButton(
        options_frame, text="Start Practice", command=start_practice_mode
    )
    start_button.pack(pady=10)

def add_competitive_options():
    start_button = ctk.CTkButton(
        options_frame, text="Start Competitive", command=start_competitive_mode
    )
    start_button.pack(pady=10)
    scoreboard_label.pack(pady=10)  # Show scoreboard in Competitive Mode

def update_scoreboard():
    scores = "\n".join([f"{name}: {score}" for name, score in scoreboard_data])
    scoreboard_label.configure(text=f"Scoreboard:\n{scores}")

# Configure the appearance of the UI
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

# Main application window
root = ctk.CTk()
root.title("Hand Lights Controller")
root.geometry("600x700")

# Variables for checkboxes
dynamics_var = ctk.BooleanVar(value=False)
right_hand_var = ctk.BooleanVar(value=True)
left_hand_var = ctk.BooleanVar(value=True)

# Song selection
selected_song = ctk.StringVar(value=songs[0])
ctk.CTkLabel(root, text="Choose a Song:", font=("Arial", 16)).pack(pady=10)
song_menu = ctk.CTkOptionMenu(root, variable=selected_song, values=songs)
song_menu.pack(pady=10)

# Mode selection
ctk.CTkLabel(root, text="Choose a Mode:", font=("Arial", 16)).pack(pady=10)

modes_frame = ctk.CTkFrame(root)
modes_frame.pack(pady=10)

practice_button = ctk.CTkButton(modes_frame, text="Practice Mode", command=enter_practice_mode)
practice_button.grid(row=0, column=0, padx=10, pady=10)

competitive_button = ctk.CTkButton(modes_frame, text="Competitive Mode", command=enter_competitive_mode)
competitive_button.grid(row=0, column=1, padx=10, pady=10)

listen_button = ctk.CTkButton(modes_frame, text="Listen to Song", command=start_listen_mode)
listen_button.grid(row=0, column=2, padx=10, pady=10)

# Options frame for dynamic options
options_frame = ctk.CTkFrame(root)
options_frame.pack(pady=10)

# Stop song button
stop_button = ctk.CTkButton(root, text="Stop Song", command=stop_song)
stop_button.pack(pady=10)

# Scoreboard (hidden initially)
scoreboard_label = ctk.CTkLabel(root, text="", wraplength=500, font=("Arial", 14))

# Status display
status_label = ctk.CTkLabel(root, text="Welcome! Choose a song and mode to get started.", wraplength=500, font=("Arial", 14))
status_label.pack(pady=10)

# Run the application
root.mainloop()

# Quit pygame mixer when the application exits
pygame.mixer.quit()
