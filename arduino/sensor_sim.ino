void setup() {
  Serial.begin(9600);
}

void loop() {
  int temperature = random(20, 35);
  int humidity = random(40, 80);
  int light = random(200, 900);

  Serial.print(temperature);
  Serial.print(",");
  Serial.print(humidity);
  Serial.print(",");
  Serial.println(light);

  delay(2000);
}