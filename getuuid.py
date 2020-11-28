import subprocess
current_machine_id = subprocess.check_output('wmic csproduct get uuid').split('\n')[1].strip()
print (current_machine_id)

#subprocess.Popen('dmidecode.exe -s system-uuid'.split())
