from PIL import Image, ImageFont, ImageDraw
import pandas as pd
import numpy
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

def sendMail(name,email):
    fromaddr = "sdisilva13@gmail.com"
    toaddr = email
    msg = MIMEMultipart()  
    msg['From'] = fromaddr 
    msg['To'] = toaddr  
    msg['Subject'] = "Certificate of Participation"
    body = """\
    <html>
    <body>
        <p><b>Thanks for attending workshop on Gesture Controlled Gaming using OpenCV</b></p>
        <p><b>Kindly find your E-certificate for the same, attached along with this mail.<br>We look forward seeing you at all our future workshops, seminars and events!</b><p>
        <p><b>Regards<br>IEEE-VIT Student Branch</b></p>
        <div style="text-align:center">
            <p><b>Connect with us on</b></p>
            
            <a href="https://www.facebook.com/IEEEVIT1"><img src="https://www.bworldonline.com/wp-content/uploads/2020/08/f_logo_RGB-Hex-Blue_512.png" height="45" width="45"></img></a>
            
            <a href="https://www.instagram.com/ieeevit/?hl=en"><img src="https://static01.nyt.com/images/2016/05/11/us/12xp-instagram/12xp-instagram-facebookJumbo-v2.jpg" height="55" width="100"></img></a>
            
            <a href="https://ieee.vit.edu.in/"><img src="https://ieee.vit.edu.in/assets/images/ieeevit-blue-1-5017x1103.png" height="55" width="100"></img></a>
            <p><b>Ask us anything about programming, meet like minded people, build projects.</b></p>
            <p><b>Join the coders Republic Group now:</b></p>
            <a href="https://chat.whatsapp.com/GNjVY5fSZav73fl77vGPj2"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/WhatsApp_logo-color-vertical.svg/600px-WhatsApp_logo-color-vertical.svg.png" height="50" width="50"></img></a>
            <p><b>For any error in certificate <a>click here</a></b></p>
        </div>
        <img src="cid:{image_cid}">
    </body>
    </html>
    """

    # for certificate
    certificate = open(f"/home/siddhant/PycharmProjects/Certificate_py/workshop1/{name}.png", "rb")
    msg.attach(MIMEText(body, 'html'))
    filename = f"{name}.png"
    p = MIMEBase('application', 'octet-stream') 
    p.set_payload((certificate).read())
    encoders.encode_base64(p) 
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
    msg.attach(p)

    #for zipfile
    zipfile = open("/home/siddhant/PycharmProjects/Certificate_py/after_workshop.zip", "rb")
    filename1 = "after_workshop.zip"
    p1 = MIMEBase('application', 'octet-stream')
    p1.set_payload((zipfile).read())
    encoders.encode_base64(p1)
    p1.add_header('Content-Disposition', "attachment; filename= %s" % filename1)
    msg.attach(p1)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls() 
    s.login(fromaddr, "saviosavio")
    text = msg.as_string() 
    s.sendmail(fromaddr, toaddr, text) 
    s.quit() 



df = pd.read_csv("cert1.csv")
for i in range(len(df)):
    name = df.iloc[i,0]
    email = df.iloc[i,1]
    sendMail(name, email)
