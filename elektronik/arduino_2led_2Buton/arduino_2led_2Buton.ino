int btn1=2;
int btn2=3;
int led1=4;
int led2=5;
bool durum1=false;
bool durum2=false;
void setup() 
{
  pinMode(btn1,INPUT);
  pinMode(btn2,INPUT);
  pinMode(led1,OUTPUT);
  pinMode(led2,OUTPUT);

}

void loop() 
{
  if(digitalRead(btn1)==HIGH)
    durum1 = !durum1;
    
  if(durum1)
    digitalWrite(led1,HIGH);
  else
    digitalWrite(led1,LOW);

  if(digitalRead(btn2)==HIGH)
    durum2 = !durum2;
    
  if(durum2)
    digitalWrite(led2,HIGH);
  else
    digitalWrite(led2,LOW);
  
  delay(400);
  /*if(digitalRead(btn1)==HIGH)
    digitalWrite(led1,HIGH);
  else
    digitalWrite(led1,LOW);

   if(digitalRead(btn2)==HIGH)
    digitalWrite(led2,HIGH);
  else
    digitalWrite(led2,LOW);
  
   delay(5);*/
  

}
