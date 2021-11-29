# xinfo is a simple neofetch alternative that aims to make modification, should the user know basic python, very easy.
# Please refer to the README.md if you are looking to install

import platform

xascii = '''db	db 
`8b  d8'
 `8bd8' 
 .dPYb.
.8P  Y8. 
YP	YP 
'''
# The xascii variable allows the user to easily change the ascii art by pasting it between the triple quotes

my_system = platform.uname()

print(xascii) # Prints the X ascii art
print("xinfo") # Prints xinfo
print("===============") # Prints the separator line
print(f"OS: {my_system.system}") # Prints the OS
print(f"Host: {my_system.node}") # Prints the user's hostname
print(f"Kernel: {my_system.release}") # Prints the kernel's version
print(f"Architecture: {my_system.machine}") # Prints the CPU's architecture
print("===============") # Prints the separator line

# xinfo is licensed under the GNU GPL
