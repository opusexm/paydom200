import subprocess

# Define the banner
BANNER = '''██████╗  █████╗ ██╗   ██╗██████╗  ██████╗ ███╗   ███╗██████╗  ██████╗  ██████╗ 
██╔══██╗██╔══██╗╚██╗ ██╔╝██╔══██╗██╔═══██╗████╗ ████║╚════██╗██╔═████╗██╔═████╗
██████╔╝███████║ ╚████╔╝ ██║  ██║██║   ██║██╔████╔██║ █████╔╝██║██╔██║██║██╔██║
██╔═══╝ ██╔══██║  ╚██╔╝  ██║  ██║██║   ██║██║╚██╔╝██║██╔═══╝ ████╔╝██║████╔╝██║
██║     ██║  ██║   ██║   ██████╔╝╚██████╔╝██║ ╚═╝ ██║███████╗╚██████╔╝╚██████╔╝
╚═╝     ╚═╝  ╚═╝   ╚═╝   ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚══════╝ ╚═════╝  ╚═════╝'''

# Display the banner and run the first script 200check.py
print(BANNER)
result1 = subprocess.run(['python3', '200check.py'], stdout=subprocess.PIPE)
print(result1.stdout.decode())

# Display the banner and run the second script domCheck.py
print(BANNER)
result2 = subprocess.run(['python3', 'domCheck.py'], stdout=subprocess.PIPE)
print(result2.stdout.decode())

# Display the banner and run the third script payCheck.py
print(BANNER)
result3 = subprocess.run(['python3', 'payCheck.py'], stdout=subprocess.PIPE)
print(result3.stdout.decode())

