class talking:
    def __init__(self, translator):
        self.translator=translator
    
    def translate(self, str_text, calt):
        # 文章を翻訳する
        trans_en = self.translator.translate(str_text, dest=calt)

        return trans_en.text

