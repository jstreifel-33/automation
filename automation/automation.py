import re

#Given a document potential-contacts, find and collect all email addresses and phone numbers.

#Phone numbers may be in various formats.

#(xxx) yyy-zzzz, yyy-zzzz, xxx-yyy-zzzz, etc.
#phone numbers with missing area code should presume 206
#phone numbers should be stored in xxx-yyy-zzzz format.

#Once emails and phone numbers are found they should be stored in two separate documents.

#The information should be sorted in ascending order.

#Duplicate entries are not allowed.

with open("automation/potential-contacts.txt") as f:
    raw_text = f.read()

#Find and write emails

email_pattern = r"\S+@\S+"

emails = re.findall(email_pattern, raw_text)
emails.sort()
emails_joined = "\n".join(emails)

with open("automation/found_emails.txt", "w") as f:
    f.write(emails_joined)

#Find and write phone numbers

phone_pattern = r"\(?\d{3}\)?[.-]?(?:\d{3})?[.-]?\d{4}"

phones = re.findall(phone_pattern, raw_text)

for phone in phones:
    print(phone)