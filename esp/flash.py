#!/usr/bin/env python
# coding: utf-8
'''
@File   :Flash.py
@Author :youxinweizhi
@Date   :2019/3/28
@Github :https://github.com/youxinweizhi
'''


def run(com, esp_type, firmware):
    FLASH_START = "0x1000"
    FLASH_MODE = "dio"
    FLASH_FREQ = "40m"
    from esptool import main
    import sys, traceback
    if esp_type == "esp8266":
        sys.argv = [
            'AutoFlash.py',
            '--port', com,
            '--baud', '460800',
            'write_flash', "--flash_size=detect", '0',
            firmware
        ]
    else:
        sys.argv = [
            'AutoFlash.py', '--chip', 'esp32',
            '--port', com,
            '--baud', '460800',
            'write_flash', '-z',
            '--flash_mode', FLASH_MODE,
            '--flash_size', '4MB',
            '--flash_freq', FLASH_FREQ,
            FLASH_START, firmware
        ]
    try:
        main()
        return None
    except Exception as e:
        return str(e)
