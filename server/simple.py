import sys, smtplib

server = sys.argv[1]

fromadd = sys.argv[2]

toaddrs = sys.argv[3]

message = "...."

s = smtplib.SMTP(server)

s.sendmail(fromadd, toaddrs, message)