import paramiko


def ssh_command(hostname, username, passwd):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh_client.connect(hostname=hostname, username= username, password=passwd)
        print("Connected to", hostname)
        command = "ls -l"
        stdin, stdout, stderr = ssh_client.exec_command(command)
        # stdin, stdout, stderr inbuilt variables

        output = stdout.read().decode("utf-8")
        err = stderr.read().decode("utf-8")
        print(output)
        print(err)

    except paramiko.AuthenticationException:
        print("Error: AuthenticationException")

    except:
        print("Error: Unable to connect to SSH")

    finally:
        ssh_client.close()
        print("Connection Closed.")

if __name__ == "__main__":
    shh_ip = "192.168.29.37"
    username = "jh"
    passwd = "jh@123456"
    ssh_command(ssh_ip, username, passwd)
