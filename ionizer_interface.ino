#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h> 
#include <Debounce.h>
#include <WiFi.h>

// #define OLED_ADDR   0x3D
#define OLED_ADDR   0x3C
//#define SSD1306_128_32
//#define SSD1306_96_16
#define SSD1306_128_64
#define DEBOUNCE_DELAY	100

/// MIGHT DELETE LATER
const char* ssid = "yourNetworkName";
const char* password =  "yourNetworkPass";

const char * host = "192.168.1.75";
const uint16_t port = 1024;
/// MIGHT DElETE LATER

const byte buttonPin 	= 8;
// static byte nexwellPin 	= 9;
const byte relayPin 	= 10;
const byte ledPin		= 11;

bool ledState = false;
bool relayState = false;

Adafruit_SSD1306 display(-1);
Debounce button(buttonPin, DEBOUNCE_TIME);

void setup() {
	// Start the serial monitor with baud rate 115200
	Serial.begin(115200);
	
	/// MIGHT DElETE LATER
	WiFi.begin(ssid, password);
	while (WiFi.status() != WL_CONNECTED) {
		delay(500);
		Serial.println("...");
	}

	Serial.print("WiFi connected with IP: ");
	Serial.println(WiFi.localIP());
	/// MIGHT DElETE LATER
	
	// OLED Display
	display.begin(SSD1306_SWITCHCAPVCC, OLED_ADDR);
	display.clearDisplay();
	display.display();
	
	// Pin modes
	pinMode(relayPin, OUTPUT);
	pinMode(ledPin, OUTPUT);
	pinMode(buttonPin, INPUT);
	// pinMode(nexwellPin, INPUT);
}

void loop() {
	// Check states of the button and nexwell
	int buttonState = button.read();
	// int nexwellState = digitalRead(nexwellPin)
	
	if(buttonState) {
		relayState = !relayState;
	}
}

void establishConnection() {
	WiFiClient client;
 
    if (!client.connect(host, port)) {
        Serial.println("Connection to host failed");
        delay(1000);
        return;
    }
 
    Serial.println("Connected to server successful!");
    client.print("Hello from ESP32!");
 
    Serial.println("Disconnecting...");
    client.stop();
 
    delay(10000);
}

void displayInformation() {
	// Debug
	if(button.count() == 10) {
		button.resetCount();
		// do debug stuff here...
		// Display wifi information for 5 seconds
	}
}

// https://github.com/Tymec/Debounce
// Nexwell two wires IN and OUTPUT
// or
// Nexwell socket client, check state of button every x seconds
