from collections import OrderedDict
glossary = OrderedDict()
glossary["word2"] = "meaning text2"
glossary["word1"] = "meaning text1"
glossary["word3"] = "meaning text3"

for word, meaning in glossary.items():
    formatted = word.title() + ':\n' + '\t' + meaning.title()
    print(formatted)
