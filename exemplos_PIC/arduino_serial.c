int led=13; //led indicativo de leitura e escrita de serial

void setup() {
  pinMode(led, OUTPUT);
  Serial.begin(9600);
  Serial1.begin(9600);
  Serial.println("Inicio comunicacao com PIC");
}

void loop() {
  digitalWrite(led,LOW);
  //faz leitura da serial do PIC e exibe valor no serial monitor
  if (Serial1.available() > 0) {
    digitalWrite(led,HIGH);
    Serial.write(Serial1.read());
    Serial.println("");
  } 
  
  digitalWrite(led,LOW);
  //faz leitura do serial monitor e envia dado para o PIC
  if (Serial.available() > 0) {
    digitalWrite(led,HIGH);
    Serial1.write(Serial.read());
  }
}