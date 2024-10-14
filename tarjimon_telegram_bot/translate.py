from googletrans import Translator 


def translate(matn):
    translator  = Translator()
    til = translator.detect(matn).lang
    if til=="en":
        return translator.translate(matn,dest='uz').text
    else:
        return translator.translate(matn,dest='en').text