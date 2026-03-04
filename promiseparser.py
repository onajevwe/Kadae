import re

def is_specific_promise(text):
    numbers = re.findall(r"\d+", text)
    return len(numbers) > 0

def extract_quantity(text):
    numbers = re.findall(r"\d+", text)
    return int(numbers[0]) if numbers else None
