// Pins for RGB LEDs
const int r1 = 13, g1 = 12, b1 = 11;
const int r2 = 10, g2 = 9, b2 = 8;
const int r3 = 7, g3 = 6, b3 = 5;
const int r4 = 4, g4 = 3, b4 = 2;
const int r5 = A3, g5 = A4, b5 = A5;

// LED arrays for indexing
const int redPins[] = {13, 10, 7, 4, A3};
const int greenPins[] = {12, 9, 6, 3, A4};
const int bluePins[] = {11, 8, 5, 2, A5};

const int tempo = 85;
const unsigned long quarterNote = 60.0 / tempo * 1000; // 3/4 time, so a quarter note gets a beat
const unsigned long halfNote = quarterNote * 2;
const unsigned long dottedHalfNote = quarterNote * 3;
const unsigned long eighthNote = quarterNote / 2;

const int songLength = 73; // Song length in half beats

// RGB colors
const int offRGB[] = {0, 0, 0};
const int redRGB[] = {1, 0, 0};
const int greenRGB[] = {0, 1, 0};
const int blueRGB[] = {0, 0, 1}; 
const int yellowRGB[] = {1, 1, 0};
const int cyanRGB[] = {0, 1, 1};
const int magentaRGB[] = {1, 0, 1};
const int whiteRGB[] = {1, 1, 1};

// Color names
const int off = 0;
const int A_red = 1;
const int B_green = 2;
const int C_blue = 3;
const int D_yellow = 4;
const int E_cyan = 5;
const int F_magenta = 6;
const int G_white = 7;

int song[songLength][5] = {
  // Bar 1
  {off, off, off, off, E_cyan},
  {off, off, C_blue, off, off},
  {off, off, off, off, E_cyan},
  {off, off, C_blue, off, off},
  {off, off, off, off, E_cyan},
  {off, off, C_blue, off, off},

  // Bar 2
  {off, off, off, off, E_cyan},
  {off, off, C_blue, off, off},
  {off, off, off, off, E_cyan},
  {off, off, C_blue, off, off},
  {off, off, off, off, E_cyan},
  {off, off, C_blue, off, off},

  // Bar 3
  {off, off, off, off, E_cyan},
  {off, off, C_blue, off, off},
  {off, off, off, off, E_cyan},
  {off, off, C_blue, off, off},
  {off, off, off, off, E_cyan},
  {off, off, C_blue, off, off},

  // Bar 4
  {off, off, off, off, E_cyan},
  {off, off, off, D_yellow, off},
  {off, off, off, off, E_cyan},
  {off, off, off, D_yellow, off},
  {off, off, off, off, E_cyan},
  {off, off, off, D_yellow, off},

  // Bar 5
  {off, off, off, off, E_cyan},
  {off, off, off, D_yellow, off},
  {off, off, off, off, E_cyan},
  {off, off, off, D_yellow, off},
  {off, off, off, off, E_cyan},
  {off, off, off, D_yellow, off},

  // Bar 6
  {off, off, off, off, E_cyan},
  {off, off, C_blue, off, off},
  {off, off, off, off, E_cyan},
  {off, off, off, D_yellow, off},
  {off, off, off, off, E_cyan},
  {off, off, off, D_yellow, off},

  // Bar 7
  {off, off, off, off, E_cyan},
  {off, off, off, D_yellow, off},
  {off, off, off, off, E_cyan},
  {off, off, off, D_yellow, off},
  {off, off, off, off, E_cyan},
  {off, off, off, D_yellow, off},

  // Bar 8
  {off, off, off, off, E_cyan},
  {off, off, off, D_yellow, off},
  {off, off, off, off, E_cyan},
  {off, off, off, D_yellow, off},
  {off, off, off, off, E_cyan},
  {off, off, off, D_yellow, off},

  // Bar 9
  {off, off, off, off, E_cyan},
  {off, off, off, D_yellow, off},
  {off, off, off, off, E_cyan},
  {off, off, off, D_yellow, off},
  {off, off, off, off, E_cyan},
  {off, off, off, D_yellow, off},

  // Bar 10
  {A_red, off, off, off, off},
  {off, off, off, off, E_cyan},

  // Bar 11
  {A_red, off, off, off, off},
  {off, off, off, off, E_cyan},

  // Bar 12
  {off, B_green, off, off, off},
  {off, off, off, off, E_cyan},

  // Bar 13
  {off, B_green, off, off, off},
  {off, off, off, off, E_cyan},

  // Bar 14
  {off, off, C_blue, off, off},
  {off, off, off, off, E_cyan},

  // Bar 15
  {off, off, C_blue, off, off},
  {off, off, off, off, E_cyan},

  // Bar 16
  {off, off, off, D_yellow, off},
  {off, off, off, off, E_cyan},

  // Bar 17
  {off, off, off, D_yellow, off},
  {off, off, off, off, E_cyan},
  {off, B_green, off, off, off},

  // Bar 18
  {A_red, off, off, off, off},
  {off, off, off, off, off},
};

bool practice = false;
bool competitive = false;
int practiceModeBeat = 0;
bool beatChanged = false;

void setup() {
  // Initialize all pins as OUTPUT
  for (int i = 0; i < 5; i++) {
    pinMode(redPins[i], OUTPUT);
    pinMode(greenPins[i], OUTPUT);
    pinMode(bluePins[i], OUTPUT);
  }

  // Initialize serial communication
  Serial.begin(9600);
}

void setLEDColor(const int rgb[], int led) {
  digitalWrite(redPins[led], rgb[0]);
  digitalWrite(greenPins[led], rgb[1]);
  digitalWrite(bluePins[led], rgb[2]);
}

void playSong() {
  for (int beat = 1; beat <= songLength; beat++) {
    playBeat(beat);
    delay(quarterNote);
  }
}

void playBeat(int beat) {
  for (int i = 0; i < 5; i++) {
    switch (song[beat - 1][i]) {
      case off:
        setLEDColor(offRGB, i);
        break;
      case A_red:
        setLEDColor(redRGB, i);
        break;
      case B_green:
        setLEDColor(greenRGB, i);
        break;
      case C_blue:
        setLEDColor(blueRGB, i);
        break;
      case D_yellow:
        setLEDColor(yellowRGB, i);
        break;
      case E_cyan:
        setLEDColor(cyanRGB, i);
        break;
      case F_magenta:
        setLEDColor(magentaRGB, i);
        break;
      case G_white:
        setLEDColor(whiteRGB, i);
        break;
    }
  }
}

void loop() {
  if (Serial.available() > 0) {
    String receivedText = Serial.readString();
    receivedText.trim(); // Remove newline and carriage return characters

    if (receivedText == "p") {
      practiceModeBeat = 0;
      practice = true;
      competitive = false;
    } else if (receivedText == "c") {
      competitive = true;
      practice = false;
    } else if (receivedText == "b") {
      practiceModeBeat += 1;
      beatChanged = true;
    }
  }

  if (practice && beatChanged) {
    playBeat(practiceModeBeat);
    beatChanged = false;
  } else if (competitive) {
    Serial.println("Playing song");
    playSong();
  }
}
