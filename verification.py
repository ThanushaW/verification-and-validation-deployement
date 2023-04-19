import datetime
import sys
from poll_mail_re import poll_mail
from send_mail_re import send_mail

def verification(mail,password,team_lead,log_path,client):

    with open('C:/JENKINS_HOME/workspace/Test HRIS/verify_build/scripts/verification.config', 'r') as f:
        action = f.read().split()[0]

    if action == 'start':

        with open(log_path, 'r') as f:
            release_number = int(f.readline().strip())

        found = poll_mail(mail,password,
            f"Build is verified by {team_lead} release: {release_number}",team_lead)

        if found:
            
            send_mail(mail,password,client,f'Requesting for UAT Acceptance release: {release_number}',mail,
                    f"Changes are accepted release: {release_number}",f"Changes are not accepted release: {release_number}",'ACCEPT','DECLINE')
            with open('C:/JENKINS_HOME/workspace/Test HRIS/verify_build/scripts/validation.config', 'w') as f:
                f.write('start')
            with open('C:/JENKINS_HOME/workspace/Test HRIS/verify_build/scripts/verification.config', 'w') as f:
                f.write('stop')

            with open('C:/JENKINS_HOME/workspace/Test HRIS/verify_build/scripts/verification.log', 'a') as f:
                f.write(f'{datetime.datetime.now()} - The script ran and verification is done\n')
        else: 
            with open('C:/JENKINS_HOME/workspace/Test HRIS/verify_build/scripts/verification.log', 'a') as f:
                    f.write(f'{datetime.datetime.now()} - The script started and verification is not yet done\n')
    else:
        with open('C:/JENKINS_HOME/workspace/Test HRIS/verify_build/scripts/verification.log', 'a') as f:
                    f.write(f'{datetime.datetime.now()} - The script is not started\n')


if __name__ == "__main__":
    # print(sys.argv)
    mail = sys.argv[1]
    password = sys.argv[2]
    team_lead = sys.argv[3]
    log_path = sys.argv[4]
    client = sys.argv[5]

    verification(mail,password,team_lead,log_path,client)


