https://docs.espressif.com/projects/esptool/en/latest/esp32/
https://micropython.org/download/esp32/

└─ $ ▶ esptool.py --chip esp32 --port /dev/ttyUSB0 erase_flash


└─ $ ▶ esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000  ./esp32-20220117-v1.18.bin 


http://docs.micropython.org/en/latest/esp32/quickref.html
http://docs.micropython.org/en/latest/genrst/index.html