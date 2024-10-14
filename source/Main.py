import os
import platform
from cpuinfo import get_cpu_info

cpu = get_cpu_info()

# this shi already looks like yandere dev's code LMAOOO
print("Operating System: " + os.name)
print("System: " + platform.system())
print("User: " + os.getlogin())
print("DE: " + os.environ.get('DESKTOP_SESSION'))
print("CPU: " + cpu)