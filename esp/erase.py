#!/usr/bin/env python
# coding: utf-8
'''
@File   :erase.py
@Author :youxinweizhi
@Date   :2019/3/28
@Github :https://github.com/youxinweizhi
'''


def run(com):
    from esptool import main
    import sys, traceback
    sys.argv = [
        'AutoFlash.py',
        '--port', com,
        '--baud', '460800',
        'erase_flash'
    ]
    try:
        main()
        return None
    except Exception as e:
        return str(e)
