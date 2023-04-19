import imaplib
import email



def poll_mail(mail,mail_app_password,mail_subject,mail_from):

    print(mail_subject)
    imap_url = 'imap.gmail.com'

    connection = imaplib.IMAP4_SSL(imap_url)

    connection.login(mail,mail_app_password)

    connection.select('Inbox')

    email_id = connection.search(None,f'(SUBJECT "{mail_subject}" FROM {mail_from})')[1][0]

    # before testing subject comment out logout connection
    connection.logout()

    if (email_id != b''):
        
        # Tests
        # mail = connection.fetch(email_id,'(RFC822)')[1]
        # for response_part in mail:
        #     if type(response_part) is tuple:
        #         msg = email.message_from_bytes((response_part[1]))
        #         print("-----------------------------------------")
        #         print("subj: "+msg['subject'])
        return True
        
    return False
        
    
if __name__ == "__main__":

    import yaml
    from send_mail_re import send_mail

    with open('credentials.yml') as f:
        content = f.read()

    config = yaml.load(content,Loader=yaml.FullLoader)

    with open(config['workspace'] + "hris_release.log", 'r') as f:
        release_number = int(f.readline().strip())


    found = poll_mail(config['user'],config['password'],f"Build is verified by thanushaw@cbctechsol.com release: {release_number}",config['default_sender'])
    # print(found)
    if found :
        send_mail(config['user'],config['password'],config['default_sender'],f'Requesting for UAT Acceptance release: {release_number}',config['user'],
                f"Changes are accepted release: {release_number}",f"Changes are not accepted release: {release_number}",'ACCEPT','DECLINE')