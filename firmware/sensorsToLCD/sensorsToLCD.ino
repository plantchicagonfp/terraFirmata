//include the I2C Wire library - needed for communication with the I2C chip attached to the LCD manual 
#include <Wire.h> 
// include the RobotGeekLCD library
#include <RobotGeekLCD.h>

// create a robotgeekLCD object named 'lcd'
RobotGeekLCD lcd;

int humidity = 0;
int temperature = 0;

unsigned long currentMillisLCD;        // store the current value from millis()
unsigned long previousMillisLCD;       // for comparison with currentMillis
int samplingIntervalLCD = 1000;          // how often to run the main loop (in ms)

  
          
 
 
void setup() 
{
  dht.begin();//start temp/humidity sensor object
  
  // initlaize the lcd object - this sets up all the variables and IIC setup for the LCD object to work
  lcd.init();
  // Print a message to the LCD.
  lcd.print("Plant Chicago!");
  delay(2000);
  lcd.clear();
  
}

/*==============================================================================
 * LOOP()
 *============================================================================*/
void loop() 
{
  currentMillisLCD = millis(); //get current time/milliseconds
  
  //check if samplingIntervalLCD time has elapsed since last LCD refresh
  if (currentMillisLCD - previousMillisLCD > samplingIntervalLCD) 
  {

    previousMillisLCD = currentMillisLCD; //upate LCD, so update previous LCD time
  
    //DISTANCE 1
    lcd.setCursor(0, 0);
    lcd.print("D:");
    lcd.print(convertIRvoltsToMM(analogRead(0))/10);
    lcd.print(" ");
    lcd.print(" ");
    delay(2);//delay for analog read
    
    //DISTANCE 2
    lcd.setCursor(5, 0);
    lcd.print("D:");
    lcd.print(convertIRvoltsToMM(analogRead(1))/10);
    lcd.print(" ");
    lcd.print(" ");
    lcd.print(" ");
    delay(2);//delay for analog read
    
    //DISTANCE 3
    lcd.setCursor(11, 0);
    lcd.print("D:");
    lcd.print(convertIRvoltsToMM(analogRead(2))/10);
    lcd.print(" ");
    lcd.print(" ");
    delay(2);//delay for analog read

    
    // HUMIDITY
     lcd.setCursor(0, 1);
    lcd.print("H:");
    lcd.print(humidity);
    lcd.print(" ");
    delay(2);
    
    // TEMPERATURE
    lcd.print("T:");
    lcd.print(temperature);
    lcd.print(" ");
    delay(2);
    
    // MOISTURE
    lcd.print("M:");
    lcd.print(analogRead(3;/[====-));
    lcd.print(" ");
    delay(2);
    
    
  }
    
    
}


int convertIRvoltsToMM(float v) { 
    return -0.00003983993846*v*v*v+ 0.0456899769 *v*v - 17.48535575 * v + 2571.052715; 
}
