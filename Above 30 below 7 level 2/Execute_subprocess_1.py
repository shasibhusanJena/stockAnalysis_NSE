from subprocess import *
import time

time.sleep(5)
Popen('python ./HistoryPrice_01.py') # it will fail get reference of Stock name from other folder
time.sleep(5)
Popen('python ./HistoryPrice_02.py')
time.sleep(5)
Popen('python ./HistoryPrice_03.py')
time.sleep(10)
Popen('python ./HistoryPrice_04.py')
time.sleep(10)
Popen('python ./HistoryPrice_05.py')
time.sleep(10)
Popen('python ./HistoryPrice_06.py')