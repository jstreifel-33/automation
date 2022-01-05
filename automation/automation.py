import re


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

phone_pattern = r"(?:\+1-)?\(?\d{3}\)?[.-]?(?:\d{3})?[.-]?\d{4}"

phones = re.findall(phone_pattern, raw_text)


def format_phones(phone_string):
    unwanted = [".", "(", ")", "-"]
    for char in unwanted:
        phone_string = phone_string.replace(char, "")
    if len(phone_string) == 10:
        num_list = list(phone_string)
        num_list.insert(3, "-")
        num_list.insert(7, "-")
        phone_string = "".join(num_list)
    elif len(phone_string) == 12:
        num_list = list(phone_string)
        num_list.insert(2, "-")
        num_list.insert(6, "-")
        num_list.insert(10, "-")
        phone_string = "".join(num_list)
    return phone_string


for idx, phone in enumerate(phones):
    phones[idx]=(format_phones(phone))

phones.sort()

phones_joined = "\n".join(phones)

with open("automation/found_phones.txt", "w") as f:
    f.write(phones_joined)
    