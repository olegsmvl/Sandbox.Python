import os
import json
import sys
from typing import Any, Dict, List


def load() -> List[Dict[str, Any]]:
    file = os.path.expanduser("~/temp/export/conversations.json")

    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data


def phrase_to_content(phrase) -> List[str]:
    list_content = []
    message = phrase["message"]
    if not message is None:
        role = message["author"]["role"]
        content_type = message["content"]["content_type"]
        if content_type == "text":
            content = message["content"]["parts"]
            print(role)
            if role == "user":
                print(content)
                list_content.append(content[0])
    return list_content


def item_to_phrases(item) -> List[Any]:
    phrases: Dict[str, Any] = item["mapping"]
    return phrases


result_list_content = []

items = load()
for item in items:
    phrases = item_to_phrases(item)
    for phrase in phrases.values():
        list_content = phrase_to_content(phrase)
        result_list_content.extend(list_content)


size = len(result_list_content)
print(size)

for i in range(0, len(result_list_content)):
    result_list_content[i] += "\n"

result_list_content_file = "result.txt"

with open(result_list_content_file, "w", encoding="utf-8") as f:
    f.writelines(result_list_content)
