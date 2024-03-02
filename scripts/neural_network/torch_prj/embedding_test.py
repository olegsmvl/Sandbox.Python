import gensim.downloader as api

model = api.load("glove-wiki-gigaword-50")

result = model.most_similar(positive=['woman', 'king'], negative=['man'])
print(result)
