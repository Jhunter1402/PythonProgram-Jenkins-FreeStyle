import paramiko


def ssh_command(hostname, port, username, passwd, command):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh_client.connect(hostname=hostname, port= port, username= username, password=passwd)
        print("Connected to", hostname)

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
    hostname = "192.168.29.37"
    port = 22
    username = "jh"
    passwd = "jh@123456"
    command = "ls -l"
    ssh_command(hostname, port, username, passwd, command)