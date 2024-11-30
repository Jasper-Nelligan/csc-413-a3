import mido
from midi_to_note_sequence import midi_to_note_sequence

currentBeat = 0
noteSequence = midi_to_note_sequence("../Interstellar Main Theme.mid")
print(noteSequence)

# Connect to the keyboard
keyboard_port = -1

try:
    keyboard_port = mido.get_input_names()[0]
except IndexError:
    print("No MIDI keyboard found. Exiting...")
    exit()

with mido.open_input(keyboard_port) as inport:
    print("Listening for MIDI messages...")
    current_notes = []

    for message in inport:
        note, velocity = -1, -1
        try:
            _, _, note, velocity, _ = str(message).split()
        except ValueError:
            continue

        note = int(note.split("=")[1])
        velocity = int(velocity.split("=")[1])

        if velocity > 0:
            current_notes.append(note)
        else:
            current_notes.remove(note)

        print(current_notes)
        print("Next note in sequence", noteSequence[currentBeat])

        if current_notes == noteSequence[currentBeat]:
            currentBeat += 1

        print(currentBeat)
