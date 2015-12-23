int Rele = 2;
int ldr = A0;
int ldr_value = 0;
boolean estado = false;
const int medio = 150; //valor de transicao para estado do rele
const int temp = 4600; 
/*
 *tempo que o rele ficara acionado
 *0 nao ira ligar
 *-1 liga ou desliga apenas quando valor do LDR for maior que 150
 */
int aux_temp = -1; //variavel auxiliar para decrementar tempo
int old_value = 0;
/*
 * 1023 valor maximo do LDR
 * 0    valor minimo do LDR
 * 150  valor de crepusculo
 */
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(Rele, OUTPUT);
}

void loop() {
  ldr_value = analogRead(ldr);
  if ((ldr_value >= medio)&&(estado)) {
    Serial.println("Mudar de estado para OFF");
    digitalWrite(Rele, LOW);
    old_value = ldr_value;
    estado = false;
  } else if ((ldr_value < medio)&&!(estado)) {
    if (temp > 0) {
      Serial.println("Mudar de estado para ON");
      digitalWrite(Rele, HIGH);
      old_value = ldr_value;
      aux_temp = temp;
      estado = true;
      delay(2000);
    } else if (temp == -1) {
      Serial.println("Mudar de estado para ON");
      digitalWrite(Rele, HIGH);
      old_value = ldr_value;
      aux_temp = temp;
      estado = true;
      delay(2000);
    }
  }
  
  
  if ((estado)&&(aux_temp == 0)) {
    digitalWrite(Rele, LOW);
  } else  if ((estado)&&(aux_temp > 0)&&(ldr_value >= medio)) {
    Serial.println("Mudar de estado para OFF");
    digitalWrite(Rele, LOW);
    old_value = ldr_value;
    estado = false;
  } else if ((estado)&&(aux_temp > 0)) {
    aux_temp--;
    delay(1000);
    Serial.println(aux_temp);
  }
}
