import MySQLdb
import smtplib

db = MySQLdb.connect (host = "localhost",user = "root",passwd = "123456",db = "mydb")
cursor = db.cursor ()
sql = "SELECT id,email_to,email_cc,email_content,no_of_try,attachment,email_subject FROM email_queue WHERE email_status=0 ORDER BY id DESC LIMIT 5"
# try:

count = 0;
if (cursor.execute(sql)):
	result = cursor.fetchall()
    for val in result:
    	print(val)
    #     email_to = '';
    #     id = row[0];
#         $email_content = $row['email_content'];
#         $email_to = str_replace("'", "", $row['email_to']);
#         $email_cc = str_replace("'", "", $row['email_cc']);
#         $attachment = $row['attachment'];
#         $email_subject = $row['email_subject'];

#         $no_of_try = $row['no_of_try'];

#         $mail->setFrom('no-reply@ocpl.com.bd', env('PROJECT_NAME'));
#         $mail->addAddress($email_to, '');     // Add a recipient email, Recipent Name is optional

#         $email_cc_exp = explode(',', $email_cc);
#         if (!empty($email_cc_exp[1])) {
#             foreach ($email_cc_exp as $emailCC) {
#                 $mail->addCC($emailCC);
#             }
#         } else {
#             $mail->addCC($email_cc);
#         }

#         //$mail->addBCC('jakir.ocpl@batworld.com');
#         $mail->addAttachment($attachment);         // Add attachments
#         //$mail->addAttachment('http://beza.sms.com.bd/uploads/2016/10/beza_57f09bb96aaa79.73874888.pdf', 'beza_57f09bb96aaa79.73874888.pdf');    // Optional name
#         $mail->isHTML(true); // Set email format to HTML

#         if($attachment){
#             $attachments = '<br/><a href="' . $attachment . '"><u>Click here for downloading the document.</u></a>';
#         } else{
#             $attachments = '';
#         }

#         $mail->Subject = $email_subject;
#         $mail->Body = $email_content . $attachments;
#         $mail->AltBody = '';
# // disable verify_peer
#         // its only for local server
#         $server_type = env('server_type');
#         if($server_type == 'local'){
#             $mail->SMTPOptions = array(
#                 'ssl' => array(
#                     'verify_peer' => false,
#                     'verify_peer_name' => false,
#                     'allow_self_signed' => true
#                 ));
#         }
#         // disable verify_peer
#         // its only for local server
#         if (!$mail->send()) {
#             $mail_msg = '<br/> Email could not be sent. <br/> Mailer Error: ' . $mail->ErrorInfo;
#             $no_of_try = $row['no_of_try'] + 1; // indicates number of failed trying to send the data to the PDF server

#             if ($no_of_try > 10) {
#                 $status = -9; // data is invalid, abort sending
#             } else {
#                 $status = 0; // email has not been sent yet
#             }
#         } else {
#             $mail_msg = '<br/> Email  has been sent on ' . date("j F, Y, g:i a");
#             $status = 1;
#         }
#         $mail->ClearAddresses();
#         $mail->ClearCCs();
#         $count++;


#         $sql = "UPDATE email_queue SET email_status=$status WHERE id=$id";
#         $mysqli->query($sql);
#         echo $mail_msg; // For showing the sending status of the email
#     }
#     $result2->close();
# }



	# cursor.execute (sql)
	# row = cursor.fetchall()
	# for val in row:
	# 	print(val)
	# cursor.close ()









# except:
# 	db.rollback
# db.close ()




# /* End of sending emails from email_queue */

# $mysqli->close();
# if ($count == 0) {
#     echo '<br/>No email in queue to send! ' . date("j F, Y, g:i a");
# }
# die();


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