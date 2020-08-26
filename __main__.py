#!python.exe
# -*- coding: utf-8 -*-
import microspec

kit = microspec.Devkit()
print(kit.setBridgeLED(led_setting=microspec.GREEN))
