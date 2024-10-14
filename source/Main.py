import os
import platform


# this shi already looks like yandere dev's code LMAOOO
print("Operating System: " + os.name)
print("System: " + platform.system())
print("User: " + os.getlogin())
print("DE: " + os.environ.get('DESKTOP_SESSION'))
#print("CPU: " + platform.processor())
# ^ temporarily commented cuz it wont do anything
