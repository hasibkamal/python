import MySQLdb
import smtplib
from datetime import date

db = MySQLdb.connect (host = "localhost",user = "root",passwd = "123456",db = "mydb")
cursor = db.cursor ()
sql = "SELECT id,email_to,email_cc,email_content,no_of_try,attachment,email_subject FROM email_queue WHERE email_status=0 ORDER BY id DESC LIMIT 1"
try:
	count = 0;
	if (cursor.execute(sql)):
		result = cursor.fetchall()
		for val in result:
			email_to = ''
			id = val[0]
			email_content = val[3]
			email_to = val[1]
			email_cc = val[2]
			attachment = val[5]
			email_subject = val[6]
			no_of_try = val[4]

			from email.MIMEMultipart import MIMEMultipart
			from email.MIMEText import MIMEText
			from email.MIMEBase import MIMEBase
			from email import encoders
			 
			fromaddr = "write2hkc@gmail.com"
			toaddr = email_to
			 
			msg = MIMEMultipart()
			 
			msg['From'] = 'no-reply@ocpl.com.bd'
			msg['To'] = email_to
			msg['Cc'] = email_cc
			msg['Bcc'] = 'hasibkamal.cse@gmail.com'
			msg['Subject'] = email_subject
			body = email_content
			 
			msg.attach(MIMEText(body, 'html'))
			 
			filename = "angularjs tutorial"
			attachment = open("angularjs_tutorial.pdf", "rb")
			 
			part = MIMEBase('application', 'octet-stream')
			part.set_payload((attachment).read())
			encoders.encode_base64(part)
			part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
			 
			msg.attach(part)
			 
			server = smtplib.SMTP('smtp.gmail.com', 587)
			server.starttls()
			server.login(fromaddr, "K@m@l4153")
			text = msg.as_string()
			if(server.sendmail(fromaddr, toaddr, text)):
				mail_msg = 'Email has sent'
				status = 1
			else:
				mail_msg = 'Email could not be sent'
				no_of_try += 1
				if(no_of_try>9):
					status = -9
				else:
					status = 0

			count += 1

			print(email_to)

			cursor.execute("UPDATE email_queue SET email_status=%s WHERE id=%s" %(status,id))
			server.quit()
except:
	print("Exception")





