import re

text = "Please contact me at john.doe@example.com or jane.doe@company.org for more information."

email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

email_matches = re.findall(email_pattern, text)

print(email_matches) 

