from googletrans import Translator
translator = Translator()

print(vars(translator.detect('Ваза')))

# try:
#     translation = translator.translate('Hello', dest='fr')
#     print(translation.text)
# except AttributeError as e:
#     print("Translation failed: " + str(e))


# from googletrans import Translator

# translator = Translator()
# translator.detect('이 문장은 한글로 쓰여졌습니다.')

# translations = translator.translate(['The quick brown fox', 'jumps over', 'the lazy dog'], dest='ko')

# for translation in translations:
#     print(translation.origin, ' -> ', translation.text)

# translator.translate('안녕하세요.', dest='ja')

# translator.translate('veritas lux mea', src='la')

# from googletrans import Translator
# translator = Translator()
# translator.translate('안녕하세요.')