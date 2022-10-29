from googletrans import Translator

translator = Translator()

text1 = 'машина'

result = translator.translate(text1)

print(result.text)
