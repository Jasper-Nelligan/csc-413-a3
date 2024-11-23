import aubio
import numpy as np
from pydub import AudioSegment

# Load the original file
audio = AudioSegment.from_file("f_sharp_piano.wav")

# Convert to PCM WAV format
audio = audio.set_frame_rate(44100).set_channels(1).set_sample_width(2)
audio.export("output.wav", format="wav")

# Path to your audio file
audio_file = "output.wav"

# Initialize aubio source (audio file reader)
samplerate = 0  # Use 0 to auto-detect samplerate
buffer_size = 1024  # Number of samples to process at a time
audio_source = aubio.source(audio_file, samplerate, buffer_size)
samplerate = audio_source.samplerate

# Initialize pitch detection
pitch_detector = aubio.pitch("default", buffer_size, hop_size=512, samplerate=samplerate)
pitch_detector.set_unit("Hz")
pitch_detector.set_silence(-40)  # Ignore silence below -40 dB

print(f"Processing audio file: {audio_file}")
detected_notes = []

while True:
    samples, read = audio_source()  # Read a buffer of audio samples
    pitch = pitch_detector(samples)[0]  # Detect pitch for the buffer
    
    if pitch > 0:  # If a pitch is detected
        # Convert frequency to MIDI note
        midi_note = 69 + 12 * np.log2(pitch / 440.0)
        piano_note = round(midi_note)  # Round to the nearest MIDI note
        
        # Check if the note is F#
        if piano_note % 12 == 6:  # F# MIDI notes have a remainder of 6 when mod 12
            detected_notes.append(piano_note)
            print(f"Detected F# at frequency: {pitch:.2f} Hz (MIDI: {piano_note})")

    if read < buffer_size:  # End of file
        break

print(f"Detected F# notes: {detected_notes}")
