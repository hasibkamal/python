import MySQLdb
import smtplib

db = MySQLdb.connect (host = "localhost",user = "root",passwd = "123456",db = "mydb")
cursor = db.cursor ()
sql = "SELECT company_name FROM company_info"
try:
	cursor.execute (sql)
	row = cursor.fetchall()
	for val in row:
		print(val)
	cursor.close ()
except:
	db.rollback
db.close ()



# from email.MIMEMultipart import MIMEMultipart
# from email.MIMEText import MIMEText
# from email.MIMEBase import MIMEBase
# from email import encoders
 
# fromaddr = "write2hkc@gmail.com"
# toaddr = "majbah39@gmail.com"
 
# msg = MIMEMultipart()
 
# msg['From'] = fromaddr
# msg['To'] = toaddr
# msg['Subject'] = "Subject - Eamil sending from python"
 
# body = "Vaiya, This is an email from python with an attached pdf file."
 
# msg.attach(MIMEText(body, 'plain'))
 
# filename = "MySQL PDF File"
# attachment = open("sql_tutorial.pdf", "rb")
 
# part = MIMEBase('application', 'octet-stream')
# part.set_payload((attachment).read())
# encoders.encode_base64(part)
# part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
# msg.attach(part)
 
# server = smtplib.SMTP('smtp.gmail.com', 587)
# server.starttls()
# server.login(fromaddr, "K@m@l4153")
# text = msg.as_string()
# server.sendmail(fromaddr, toaddr, text)
# server.quit()