import sys
import time
import paramiko


key = paramiko.RSAKey.from_private_key_file(r'suresh')
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

out_file = open(r'connection_results.txt','w+')
in_file = open(r'servers.txt')
for host in in_file:
      host=host.strip()
      print ("Checking server",host)

      try:
            ssh.connect(host, username="ubuntu", pkey = key)

            command = 'uptime'
            (stdin, stdout, stderr) = ssh.exec_command(command)
            for line in stdout.readlines():
                  print ("Connected to" +" " + host + "and uptime is" + line)
            ssh.close()

      except Exception as e:
            print(e)


in_file.close()
out_file.close()
