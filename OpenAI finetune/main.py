import openai

with open("D:/StudyDoc/Python stuff/Capstone Project/OpenAI API/API.txt") as file:
    openai.api_key = file.read()

""" openai.api_key = "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" """

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()
    
def save_file(filepath, content):
    with open(filepath, 'a', encoding='utf-8') as outfile:
        outfile.write(content)

with open("D:/StudyDoc/Python stuff/Capstone Project/OpenAI finetune/processed_data.jsonl") as file:
    response = openai.File.create(
        file=file,
        purpose='fine-tune'
    )

file_id = response['id']
print(f"File uploaded successfully with ID: {file_id}")