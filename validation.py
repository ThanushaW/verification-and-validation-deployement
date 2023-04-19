
import requests
import sys
from poll_mail_re import poll_mail
import datetime

def validation(mail,password,client,log_path,deploy_url,jenkins_user,jenkins_app):

    with open('C:/JENKINS_HOME/workspace/Test HRIS/verify_build/scripts/validation.config', 'r') as f:
        action = f.read()
    
    if action == 'start':

        with open(log_path, 'r') as f:
            release_number = int(f.readline().strip())

        found = poll_mail(mail,password,
            f"Changes are accepted release: {release_number}",client)

        if found:
            jenkins_url = deploy_url
            auth = (jenkins_user, jenkins_app)
            response = requests.get(jenkins_url, auth=auth)
            print(f'status code : {response.status_code}')
            print("Deployed "+deploy_url)
            with open('C:/JENKINS_HOME/workspace/Test HRIS/verify_build/scripts/validation.config', 'w') as f:
                f.write('stop')

            with open('C:/JENKINS_HOME/workspace/Test HRIS/verify_build/scripts/validation.log', 'a') as f:
                f.write(f'{datetime.datetime.now()} - The script ran and validation is done\n')
        else: 
            with open('C:/JENKINS_HOME/workspace/Test HRIS/verify_build/scripts/validation.log', 'a') as f:
                    f.write(f'{datetime.datetime.now()} - The script started and validation is not yet done\n')
    else:
        with open('C:/JENKINS_HOME/workspace/Test HRIS/verify_build/scripts/validation.log', 'a') as f:
                    f.write(f'{datetime.datetime.now()} - The script is not started\n')

if __name__ == "__main__":
    # print(sys.argv)
    # mail = sys.argv[1]
    # password = sys.argv[2]
    # client = sys.argv[3]
    # log_path = sys.argv[4]
    # deploy_url = sys.argv[5]
    # jenkins_user = sys.argv[6]
    # jenkins_app = sys.argv[7]
    # validation(mail,password,client,log_path,deploy_url,jenkins_user,jenkins_app)
    import yaml

    with open('validation.yml', 'r') as f:
        config = yaml.safe_load(f)
    
    validation(config['mail'],config['password'],config['client'],config['log_path'],config['deploy_url'],config['jenkins_user'],config['jenkins_app'])