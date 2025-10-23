// C++ code
// Brown = Web not have 
void setup()
{ 
  Serial.begin(9600);
  pinMode(11, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(8, OUTPUT);
  
}

void loop()
{
  int readLDR = analogRead(A0);
  Serial.print("ReadDigital");
  Serial.print(" : ");
  Serial.println(readLDR);
  delay (100);
  digitalWrite(11, 0); //HIGHT = 1
  digitalWrite(10,0); //LOW = 0
  digitalWrite(9,0);
  digitalWrite(8,0);
  Serial.println(readLDR);// Wait for a second
  delay(250); // Wait for 1000 millisecond(s)
  digitalWrite(11,0);
  digitalWrite(10,0);
  digitalWrite(9,0);
  digitalWrite(8,1);
  Serial.println(readLDR);
  delay(250);
  digitalWrite(11,0);
  digitalWrite(10,0);
  digitalWrite(9,1);
  digitalWrite(8,1);
  Serial.println(readLDR);
  delay(250);
  digitalWrite(11,0);
  digitalWrite(10,1);
  digitalWrite(9,1);
  digitalWrite(8,1);
  Serial.println(readLDR);
  delay(250);
  digitalWrite(11,1);
  digitalWrite(10,1);
  digitalWrite(9,1);
  digitalWrite(8,1);
  Serial.println(readLDR);
  delay(250);

}
