// Pins for RGB LEDs
int r1 = 13, g1 = 12, b1 = 11;
int r2 = 10, g2 = 9, b2 = 8;
int r3 = 7, g3 = 6, b3 = 5;
int r4 = 4, g4 = 3, b4 = 2;
int r5 = A3, g5 = A4, b5 = A5;

// LED arrays for indexing
int redPins[] = {13, 10, 7, 4, A3};
int greenPins[] = {12, 9, 6, 3, A4};
int bluePins[] = {11, 8, 5, 2, A5};

int tempo = 85;

unsigned long quarterNote = 60.0 / tempo * 1000; // 3/4 time, so a quarter note gets a beat
unsigned long halfNote = quarterNote * 2;
unsigned long dottedHalfNote = quarterNote * 3;
unsigned long eighthNote = quarterNote / 2;

bool practice = false;
bool competitive = false;

// RGB colors
int offRGB[] = {0, 0, 0};
int redRGB[] = {1, 0, 0};
int greenRGB[] = {0, 1, 0};
int blueRGB[] = {0, 0, 1}; 
int yellowRGB[] = {1, 1, 0};
int cyanRGB[] = {0, 1, 1};
int magentaRGB[] = {1, 0, 1};
int whiteRGB[] = {1, 1, 1};

// Color names
const int off = 0;
const int A_red = 1;
const int B_green = 2;
const int C_blue = 3;
const int D_yellow = 4;
const int E_cyan = 5;
const int F_magenta = 6;
const int G_white = 7;

const int songLength = 108; // Song length in half beats

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
  {A_red, off, off, off, off},
  {off, off, off, off, E_cyan},
  {off, off, off, off, E_cyan},
  {off, off, off, off, E_cyan},
  {off, off, off, off, E_cyan},

  // Bar 11
  {A_red, off, off, off, off},
  {A_red, off, off, off, off},
  {off, off, off, off, E_cyan},
  {off, off, off, off, E_cyan},
  {off, off, off, off, E_cyan},
  {off, off, off, off, E_cyan},

  // Bar 12
  {off, B_green, off, off, off},
  {off, B_green, off, off, off},
  {off, off, off, off, E_cyan},
  {off, off, off, off, E_cyan},
  {off, off, off, off, E_cyan},
  {off, off, off, off, E_cyan},

  // Bar 13
  {off, B_green, off, off, off},
  {off, B_green, off, off, off},
  {off, off, off, off, E_cyan},
  {off, off, off, off, E_cyan},
  {off, off, off, off, E_cyan},
  {off, off, off, off, E_cyan},

  // Bar 14
  {off, off, C_blue, off, off},
  {off, off, C_blue, off, off},
  {off, off, off, off, E_cyan},
  {off, off, off, off, E_cyan},
  {off, off, off, off, E_cyan},
  {off, off, off, off, E_cyan},

  // Bar 15
  {off, off, C_blue, off, off},
  {off, off, C_blue, off, off},
  {off, off, off, off, E_cyan},
  {off, off, off, off, E_cyan},
  {off, off, off, off, E_cyan},
  {off, off, off, off, E_cyan},

  // Bar 16
  {off, off, off, D_yellow, off},
  {off, off, off, D_yellow, off},
  {off, off, off, off, E_cyan},
  {off, off, off, off, E_cyan},
  {off, off, off, off, E_cyan},
  {off, off, off, off, E_cyan},

  // Bar 17
  {off, off, off, D_yellow, off},
  {off, off, off, D_yellow, off},
  {off, off, off, off, E_cyan},
  {off, off, off, off, E_cyan},
  {off, B_green, off, off, off},
  {off, B_green, off, off, off},

  // Bar 18
  {A_red, off, off, off, off},
  {A_red, off, off, off, off},
  {A_red, off, off, off, off},
  {A_red, off, off, off, off},
  {A_red, off, off, off, off},
  {A_red, off, off, off, off},
};

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

void setLEDColor(int rgb[], int led) {
  digitalWrite(redPins[led], rgb[0]);
  digitalWrite(greenPins[led], rgb[1]);
  digitalWrite(bluePins[led], rgb[2]);
}

void playSong() {
  for (int beat = 1; beat <= songLength; beat++) {
    playBeat(beat);
    delay(eighthNote);
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
    playSong();
  }
}
