import re
import redaction_config
with open(r"C:\Users\daler\Desktop\Projects\DaleLuis Persistent training\file operations\Q2\report.txt","r") as f:
    reader=f.read()
    replace = reader
    count=0
    total_count=0
    print("Redaction complete.")
    for i in range(len(redaction_config.sensitive)):
        for match in re.finditer(redaction_config.sensitive[i],reader):
            count+=1
        print(f"{redaction_config.sensitive[i]} -> {count} occurences redacted")
        replace =re.sub(redaction_config.sensitive[i],"[REDACTED]",replace)
    
    
with open(r"C:\Users\daler\Desktop\Projects\DaleLuis Persistent training\file operations\Q2\report_redacted.txt", "w", newline="") as f:
    f.write(replace)