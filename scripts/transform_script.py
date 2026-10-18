import os
import json

data_dir = "../data/BBC News Articles"
output_file = "data.json"

documents = []

# Walk through the data directory
for root, dirs, files in os.walk(data_dir):
    for file in files:
        if file.endswith(".txt"):
            file_path = os.path.join(root, file)
            category = os.path.basename(root)  # Folder name is the category
            with open(file_path, "r", encoding="ISO-8859-1") as f:
                content = f.read()
            document = {
                "filename": file,
                "category": category,
                "title": file.replace(".txt", ""),  # Name of the file is the title
                "content": content,
                "path": file_path
            }
            documents.append(document)

# Save to JSON
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(documents, f, ensure_ascii=False, indent=4)