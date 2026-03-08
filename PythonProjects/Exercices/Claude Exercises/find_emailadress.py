import re

text = "Please contact me at john.doe@example.com or jane.doe@company.org for more information."

email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

email_matches = re.findall(email_pattern, text)

print(email_matches) 

#Phone Numbers: `r"\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b"` (This pattern matches phone numbers in various formats, such as "123-456-7890", "123 456 7890", and "123.456.7890".)

#Dates: `r"\b\d{1,2}[-/]\d{1,2}[-/]\d{2,4}\b"` (This pattern matches dates in formats like "mm/dd/yyyy", "dd-mm-yyyy", and "mm/dd/yy".)

#URLs: `r"https?://\S+"` (This pattern matches URLs starting with "http://" or "https://".)