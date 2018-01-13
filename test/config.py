nodes=[
    {
        'type'      : 'wemos d1 mini v2.2.0',
        'port'      : '/dev/serial/by-path/pci-0000:00:14.0-usb-0:3.1:1.0-port0',
        'ip'        : '192.168.13.91',
        'flash_cmd' : 'esptool.py --port {port} -b 1500000  write_flash 0x0 .pioenvs/dev_ESP8266_4096/firmware.bin --flash_size=32m -p',
        'build_cmd' : 'platformio run --environment dev_ESP8266_4096'
    },

    {
        'type'      : 'nodemcu geekcreit ESP12E devkit v2',
        'port'      : '/dev/serial/by-path/pci-0000:00:14.0-usb-0:3.2:1.0-port0',
        'ip'        : '192.168.13.92',
        'flash_cmd' : 'esptool.py --port {port} -b 1500000  write_flash 0x0 .pioenvs/dev_ESP8266_4096/firmware.bin --flash_size=32m -p',
        'build_cmd' : 'platformio run --environment dev_ESP8266_4096'
    },

    {
        'node'      : 3,
        'type'      : 'wemos d1 mini v2.2.0',
        'port'      : '/dev/ttyUSB0',
        'ip'        : '192.168.13.91',
        'flash_cmd' : 'esptool.py --port {port} -b 1500000  write_flash 0x0 .pioenvs/dev_ESP8266_4096/firmware.bin --flash_size=32m -p',
        'build_cmd' : 'platformio run --environment dev_ESP8266_4096'
    },

]


mqtt_broker="192.168.13.236"

#ip of the server running this script
http_server="192.168.13.236"
http_port=8080
