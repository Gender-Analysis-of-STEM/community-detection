import subprocess
 
# Using readlines()
file1 = open('2019.txt', 'r')
Lines = file1.readlines()
 
count = 0
# Strips the newline character
for line in Lines:
    count += 1

    command = "twarc2 search --archive --start-time '2019-02-01' --end-time '2019-03-14' 'conversation_id:{} OR (url:{} is:quote)' ./2019/{}.jsonl".format(line.strip(), line.strip(), line.strip())

    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    process.wait()

#print(process.returncode)