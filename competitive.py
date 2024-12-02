"""
Starts competitive mode

Arguments:
    midi_file_path: The path to the MIDI file to practice
"""

import mido
from midi_to_note_sequence import midi_to_note_sequence
import time

def start_competitive_mode(midi_file_path):
    time.sleep(2)

    noteSequence = midi_to_note_sequence(midi_file_path, True, True)
    print(noteSequence)

    # Connect to the keyboard
    keyboard_port = -1

    try:
        keyboard_port = mido.get_input_names()[0]
    except IndexError:
        print("No MIDI keyboard found. Exiting...")
        exit()
    time.sleep(2)

    with mido.open_input(keyboard_port) as inport:
        print("Listening for MIDI messages...")

        current_index = 0
        score = 0

        start_time = time.time()

        for message in inport:
            if current_index >= len(noteSequence):
                break
            
            elapsed_time = time.time() - start_time
            if elapsed_time > 45:
                break
            
            expected_notes, expected_velocity = noteSequence[current_index]
            
            played_note, velocity = -1, -1
            try:
                _, _, played_note, velocity, _ = str(message).split()
            except ValueError:
                # Ignore messages that are not note_on
                continue

            played_note = int(played_note.split("=")[1])
            velocity = int(velocity.split("=")[1])

            if velocity > 0:
                if played_note in expected_notes and expected_velocity - 20 <= velocity <= expected_velocity + 20:
                    score += 1
                    current_index += 1
                else:
                    score -= 1
                

        return score

if __name__ == "__main__":
    start_competitive_mode("Interstellar Main Theme.mid")