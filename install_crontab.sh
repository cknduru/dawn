#!/bin/bash
(crontab -l 2>/dev/null; echo "* * * * 1-5 python ~/Desktop/dawn/dawn.py") | crontab -
