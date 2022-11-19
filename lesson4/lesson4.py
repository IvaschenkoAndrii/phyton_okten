try:
    with open ('emails.txt') as file_read, open ('emails_gmail.txt', mode='w') as file_write:
        for line in file_read:
            if line.endswith('@gmail.com\n'):
                file_write.write(line)
except Exception as err:
    print(err)