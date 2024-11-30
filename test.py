from mido import MidiFile

# Load the MIDI file
midi_file = MidiFile("../Interstellar Main Theme.mid")

# Initialize data structures for hands
right_hand_events = []
left_hand_events = []

def process_track(track):
    events = []
    absolute_time = 0
    for msg in track:
        absolute_time += msg.time  # Accumulate delta time to get absolute time
        if msg.type in ["note_on", "note_off"]:
            event = {
                "time": absolute_time,
                "note": msg.note,
                "velocity": msg.velocity if msg.type == "note_on" else 0,
            }

            events.append(event)

    return events

def midi_note_to_letter(note_number):
    note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    octave = note_number // 12 - 1
    note = note_names[note_number % 12]
    return f"{note}{octave}"


# Process each track in the MIDI file
right_hand_events = process_track(midi_file.tracks[0])
left_hand_events = process_track(midi_file.tracks[1])

# Merge and align events by time
all_events = sorted(right_hand_events + left_hand_events, key=lambda x: x["time"])

# Output aligned notes
print("Aligned Notes (time, right hand, left hand):")
for event in all_events:
    if event in right_hand_events:
        print(
            f"{event['time']}: Right hand - Note {midi_note_to_letter(event['note'])} {'On' if event['velocity'] > 0 else 'Off'}"
        )
    else:
        print(
            f"{event['time']}: Left hand - Note {midi_note_to_letter(event['note'])} {'On' if event['velocity'] > 0 else 'Off'}"
        )
