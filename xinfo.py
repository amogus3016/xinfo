import platform

xascii = '''___   ___ 
\  \ /  / 
 \  V  /  
  >   <   
 /  .  \  
/__/ \__\ '''

my_system = platform.uname()

print(xascii)
print("xinfo")
print("===============")
print(f"OS: {my_system.system}")
print(f"Host: {my_system.node}")
print(f"Kernel: {my_system.release}")
print(f"Architecture: {my_system.machine}")
