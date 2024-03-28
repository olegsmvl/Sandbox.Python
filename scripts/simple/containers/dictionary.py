thisdict = {}

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict = dict(name = "John", age = 36, country = "Norway")

thisdict["height"] = 195

thisdict.update({"weight": 105})

field = "work"
value = "programmer"
thisdict.update({field: value})

print(thisdict)

text = "Tokenizing text is a core task of NLP."
tokenized_text = list(text)
token2idx = {ch: idx for idx, ch in enumerate(sorted(set(tokenized_text)))}
print(token2idx)