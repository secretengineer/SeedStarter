1#include <Wire.h>
2#include <Adafruit_BMP085.h>
3#include <Adafruit_HTU21DF.h>
45Adafruit_BMP085 bmp;
6Adafruit_HTU21DF htu;
78void setup() {
9  Serial.begin(9600);
10  if (!bmp.begin()) {
11    Serial.println("Could not find a valid BMP085 sensor, check wiring!");
12    while (1) {}
13  }
14  if (!htu.begin()) {
15    Serial.println("Couldn't find HTU21DF sensor! Check wiring.");
16    while (1) {}
17  }
18}
1920void loop() {
21  float temperature = bmp.readTemperature();
22  float humidity = htu.readHumidity();
23  Serial.print("Temperature: ");
24  Serial.print(temperature);
25  Serial.print("*C  Humidity: ");
26  Serial.print(humidity);
27  Serial.println("%");
28  delay(1000);
29  }
