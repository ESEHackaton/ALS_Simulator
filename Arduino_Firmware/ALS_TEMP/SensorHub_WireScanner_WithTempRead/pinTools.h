/*

  SDA:
  PA22 PTC/X[10] *SERCOM3/PAD[0] SERCOM5/PAD[0] TC4/WO[0] TCC0/WO[4]

  
*/

/*
PA14, D2, SERCOM2.2, SERCOM4.2
PA09, D3, SERCOM0.1, SERCOM2.1
PA08, D4, SERCOM0.0, SERCOM2.0
PA15, D5, SERCOM2.3, SERCOM4.3

PORT/PIN: FUNCTION:  NORMAL:   ALT:
PA16      SDA        SERCOM1.0 SERCOM3.0
PA17      SCL        SERCOM1.1 SERCOM3.1
PA22      SDA        SERCOM3.0 SERCOM5.0
PA23      SCL        SERCOM3.1 SERCOM5.1
PA12      SDA        SERCOM2.0 SERCOM4.0
PA13      SCL        SERCOM2.1 SERCOM4.1


*/

class TwiPinPair {
  private:
    uint32_t _dataPin;
    uint32_t _clockPin;
  public:

    TwiPinPair(uint32_t dataPin, uint32_t clockPin) {
      _dataPin = dataPin;
      _clockPin = clockPin;
    }
    
    String getPortPin(uint32_t ulPin)
    {
      // Reports Port/Pin for digital pin
      if ( g_APinDescription[ulPin].ulPinType == PIO_NOT_A_PIN )
      {
        return "NA";
      }

      EPortType port = g_APinDescription[ulPin].ulPort;
      uint32_t pin = g_APinDescription[ulPin].ulPin;
      uint32_t pinMask = (1ul << pin);
      String result = "P";
      char portLetter = 'A';
      portLetter += port;
      result += portLetter;

      result += String(pin);
      return result;
    }
    
    String getPortPinSDA()
    {
      return getPortPin(_dataPin);
    }

    String getPortPinSCL()
    {
      return getPortPin(_clockPin);
    }

    void setPinPeripheralStates() {
      pinPeripheral(_dataPin, PIO_SERCOM);
      pinPeripheral(_clockPin, PIO_SERCOM);
    }

    void setPinPeripheralAltStates() {
      pinPeripheral(_dataPin, PIO_SERCOM_ALT);
      pinPeripheral(_clockPin, PIO_SERCOM_ALT);
    }

};
