import subprocess

user = input("Podaj kod: ")
subprocess.run(f"echo hello: {user}",shell=True)
# subprocess.run(["ls","-la","/dark_side"])
