

void setup()
{
    Serial.begin(9600);
    //pinMode(D0,INPUT);
}
void loop()
{
   int q = analogRead(A0);
   //int chk = d.read11(DHT11_PIN);

   //float t=d.temperature;
   int pol;
   
   if(q<50)
       Serial.println("fresh");
  else if (q<150)
     Serial.println("low");
  else if(1<700)
     Serial.println("medium");
  else
   {
      Serial.println("high");
   }
   Serial.print("heat: ");
   //Serial.print(t);

   delay(100);
}
