import os
import platform


# this shi already looks like yandere dev's code LMAOOO
#print("Operating System: " + os.name)
# ^ also commented like the cpu info cuz it just prints "posix" as the os name
print("System: " + platform.system())
print("User: " + os.getlogin())
print("DE: " + os.environ.get('DESKTOP_SESSION'))
#print("CPU: ", platform.processor())
# ^ temporarily commented cuz it wont do anything, if this doesnt get fixed for a while then idfk lol
print("CPUs:", os.cpu_count())
