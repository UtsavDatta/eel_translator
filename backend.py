import eel
from googletrans import Translator
trans = Translator()


eel.init("web")

@eel.expose
def translate(data, srclang, destlang):
    mytext = data
  
    
    t = trans.translate(mytext,
    src = srclang ,
    dest = destlang)
    print(f'{t.origin}->{t.text}')
    outputText = f'{t.text}'
    return outputText

    
  
eel.start("home.html", size =(1000,700))
