// Pins for RGB LEDs
int r1 = 13, b1 = 12, g1 = 11;
int r2 = 10, b2 = 9, g2 = 8;
int r3 = 7, b3 = 6, g3 = 5;
int r4 = 4, b4 = 3, g4 = 2;
int r5 = A3, b5 = A4, g5 = A5;

// LED arrays for indexing
int redPins[] = {13, 10, 7, 4, A3};
int bluePins[] = {12, 9, 6, 3, A4};
int greenPins[] = {11, 8, 5, 2, A5};

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
const int red = 1;
const int green = 2;
const int blue = 3;
const int yellow = 4;
const int cyan = 5;
const int magenta = 6;
const int white = 7;

int song[3][5] = {
  {red, off, blue, off, off},
  {off, green, off, yellow, off},
  {off, off, blue, off, cyan},
};

int beat = 0;

void setup() {
  // Initialize all pins as OUTPUT
  for (int i = 0; i < 5; i++) {
    pinMode(redPins[i], OUTPUT);
    pinMode(bluePins[i], OUTPUT);
    pinMode(greenPins[i], OUTPUT);
  }

  // Initialize serial communication
  Serial.begin(9600);
}

void setLEDColor(int rgb[], int led) {
  digitalWrite(redPins[led], rgb[0]);
  digitalWrite(bluePins[led], rgb[1]);
  digitalWrite(greenPins[led], rgb[2]);
}

void playSong() {
  for (int i = 0; i < 5; i++) {
    switch (song[beat][i]) {
      case off:
        setLEDColor(offRGB, i);
        break;
      case red:
        setLEDColor(redRGB, i);
        break;
      case green:
        setLEDColor(greenRGB, i);
        break;
      case blue:
        setLEDColor(blueRGB, i);
        break;
      case yellow:
        setLEDColor(yellowRGB, i);
        break;
      case cyan:
        setLEDColor(cyanRGB, i);
        break;
      case magenta:
        setLEDColor(magentaRGB, i);
        break;
      case white:
        setLEDColor(whiteRGB, i);
        break;
    }
  }
}

void loop() {
  if (Serial.available() > 0) {
    String receivedText = Serial.readString();

    if (receivedText == "practice") {
      practice = true;
      competitive = false;
    } else if (receivedText == "competitive") {
      competitive = true;
      practice = false;
    } else if (receivedText == "beat") {
      beat += 1;
    }
  }

  if (practice) {
    playSong();
  } else if (competitive) {

  }
}
