import smtplib
import yaml
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr



def send_mail(from_mail,from_password,to_mail,subject,mailto_mail,mailto_subject_pos,mailto_subject_neg,btn_1,btn_2):


    # create message object instance
    msg = MIMEMultipart()

    # setup the parameters of the message
    password = from_password
    msg['From'] = formataddr(('DevOps Admin', from_mail))
    msg['To'] = to_mail
    msg['Subject'] = subject

    # attach the body with the message
    body = """<!DOCTYPE html>
                            <html>
                            <head>
                                <style>
                                    /* Style for buttons */
                                    .btn {
                                        display: inline-block;
                                        padding: 10px 40px;
                                        text-align: center;
                                        text-decoration: none;
                                        background-color: #4CAF50;
                                        color: #fff;
                                        border-radius: 5px;
                                        border: none;
                                        transition: background-color 0.3s;
                                        margin-right: 10px;
                                    }
                                    
                                    /* Hover effect for buttons */
                                    .btn:hover {
                                        background-color: #3e8e41;
                                    }
                                </style>
                            </head>
                            <body>
                                <a href="mailto:%s?subject=%s &body=%s" class="btn">%s</a>
                                <a href="mailto:%s?subject=%s &body=%s Reason: " class="btn">%s</a>
                            </body>
                            </html>
                            """%(mailto_mail,mailto_subject_pos,mailto_subject_pos,btn_1,mailto_mail,mailto_subject_neg,mailto_subject_neg,btn_2)
    msg.attach(MIMEText(body, 'html'))

    # create SMTP session
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    
    # login to the SMTP server
    server.login(from_mail, password)
    
    # send the message via the SMTP server
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    
    # terminate the SMTP session
    server.quit()


if __name__ == "__main__":
    with open('validation.yml') as f:
        content = f.read()

    config = yaml.load(content,Loader=yaml.FullLoader)
    
    send_mail(config['mail'],config['password'],config['client'],f'Requesting for UAT Acceptance release: 7',config['mail'],
    "Changes are accepted release: 7","Changes are not accepted release: 7",'ACCEPT','DECLINE')