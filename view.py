import eel
import desktop
import translate

from googletrans import Translator


app_name="web"
end_point="index.html"
size=(600,700)
item_csv = 'item.csv'

@ eel.expose
def talk_system(text, lang):
    output_data = trans.translate(text, lang)
    return output_data

# 翻訳クラス生成
trans = translate.talking(Translator())

desktop.start(app_name,end_point,size)