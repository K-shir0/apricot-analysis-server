import re
import sys
import jaconv

from flask import Flask, request

sys.path.append("/Users/k-shiro/.local/share/virtualenvs/apricot-sudachi-cXNIPqPY/lib/python3.7/site-packages")
from sudachipy import tokenizer
from sudachipy import dictionary

app = Flask(__name__)

tokenizer_obj = dictionary.Dictionary().create()
mode = tokenizer.Tokenizer.SplitMode.C


@app.route('/', methods=["POST"])
def index():
    word = str(request.form["word"])

    tokenized_word = tokenizer_obj.tokenize(word, mode)[0]

    normalized_word = tokenized_word.normalized_form()

    p = re.compile('[\u30A1-\u30FF]+')

    # カタカナならそのまま漢字ならもう一回実行してひらがな化する
    if p.fullmatch(normalized_word):
        # カタカナの場合はそのまま返す
        return normalized_word

    else:
        # 漢字の場合はひらがなに直して返す
        normalized_tokenized_word = tokenizer_obj.tokenize(normalized_word, mode)[0]

        return jaconv.kata2hira(normalized_tokenized_word.reading_form())


def main():
    app.run(host='0.0.0.0', port=5000)


if __name__ == "__main__":
    main()

# def tokenize_word():
#
#
# print(m.surface())
#
# # => '食べ'
# print(m.surface())
#
# # => '食べる'
# print(m.dictionary_form())
#
# # => 'タベ'
# print(m.reading_form())
#
# # => ['動詞', '一般', '*', '*', '下一段-バ行', '連用形-一般']
# print(m.part_of_speech())
#
# print(m.normalized_form())
