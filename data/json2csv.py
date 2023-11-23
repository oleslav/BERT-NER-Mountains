import json
import csv

def parse_json_to_csv(json_file_path, csv_file_path):
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    sentences = [item["sentence"] for item in data]
    word_labels = [item["labels"] for item in data]

    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['sentence', 'word_labels']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()

        for sentence, labels in zip(sentences, word_labels):
            writer.writerow({'sentence': sentence, 'word_labels': ",".join(labels)})

    return label2id, id2label

# Example usage:
json_file_path = 'mountains_data.json'
csv_file_path = 'mountains_data.csv'
label2id, id2label = parse_json_to_csv(json_file_path, csv_file_path)

label2id = {'O': 0, 'B-MOUNTAIN': 1,  'I-MOUNTAIN': 2}
id2label = {idx: label for label, idx in label2id.items()}