#include <wiringPi.h>
int main(void){
	wiringPiSetup();
	pinMode(25, OUTPUT);
	pinMode(24, INPUT);
	for(;;){
		if(digitalRead(24)==HIGH){
			digitalWrite(25, HIGH);
			delay(10);
		} else {
			digitalWrite(25, LOW);
			delay(10);
		}
	}
}			
		
