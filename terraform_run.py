import subprocess

def terraform_init(command):
    # process = subprocess.run(command,shell=True,check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    # print(process.stdout.decode())
    subprocess.run(command,shell=True,check=True)

directory = "/home/nabeel-sarfraz/python-training/terraform"
# command = f"terraform -chdir={directory} init"
# command = f"terraform -chdir={directory} plan"
command = f"terraform -chdir={directory} destroy -auto-approve"

# print(command)
terraform_init(command)