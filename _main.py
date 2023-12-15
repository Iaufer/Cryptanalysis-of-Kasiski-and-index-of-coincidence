# import nltk
# from nltk.corpus import wordnet

# def is_text_meaningful(text):
#     tokens = nltk.word_tokenize(text)  # Токенизация текста
#     meaningful_word_count = 0

#     for token in tokens:
#         synsets = wordnet.synsets(token)  # Получение синсетов для каждого слова
#         if synsets:  # Если синсеты доступны
#             meaningful_word_count += 1

#     # Оцениваем, насколько текст является осмысленным на основе количества значимых слов
#     if meaningful_word_count / len(tokens) >= 0.5:  # Пороговое значение 0.5 (можно изменить по своему усмотрению)
#         return 1
#     else:
#         return 


# # text = "HER HIS BALD SCENTED AND SHINING HEAD AND COMPLACENTLY  "
# # result = is_text_meaningful(text)
# # print(result)

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from nltk.classify import NaiveBayesClassifier

# Загрузка стоп-слов и инициализация лемматизатора
# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('wordnet')

stop_words = set(stopwords.words("russian"))
lemmatizer = WordNetLemmatizer()

# Функция для предварительной обработки текста
def preprocess_text(text):
    # Токенизация текста
    tokens = word_tokenize(text.lower())

    # Удаление стоп-слов и пунктуации
    filtered_tokens = [token for token in tokens if token.isalpha() and token not in stop_words]

    # Лемматизация слов
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]

    # Анализ частей речи
    tagged_tokens = pos_tag(lemmatized_tokens)

    # Сбор признаков (слов) и их POS-тегов
    features = {}
    for word, pos in tagged_tokens:
        features[word] = pos

    return features

# Обучающий набор данных
train_data = [
    ('I love this movie', 'positive'),
    ('This was an awesome movie', 'positive'),
    ('I did not like this movie', 'positive'),
    ('The plot was boring', 'positive'),
    ('dagwe hjfd hau iew gqu reig eb', 'negative'),
    (' U FSAMAGO DP PHFLWLSHLFXMV SS AW', 'negative')

    # Дополните этот набор данных нужными примерами для обучения
]



alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def of(C):
    return alphabet.index(C)


def vigenere(m, key):
    m = m.upper()
    key = key.upper()
    k = ""
    r = ""
    key_index = 0
    
    for i in range(len(m)):
        if m[i].isspace():
            k += " "
            r += " "
        else:
            if key[key_index % len(key)].isspace():
                key_index += 1

            k += key[key_index % len(key)]
            r += alphabet[(of(m[i]) + of(k[i])) % len(alphabet)]
            key_index += 1

    return r


def res(s):


    # Подготовка данных для обучения
    preprocessed_train_data = [(preprocess_text(text), label) for (text, label) in train_data]

    # Обучение модели наивного Байесовского классификатора
    classifier = NaiveBayesClassifier.train(preprocessed_train_data)

    # Тестовый текст

    test_text = "".join(s).replace("\n", "")


    # Предварительная обработка тестового текста
    preprocessed_test_text = preprocess_text(test_text)

    # Классификация текста
    result = classifier.classify(preprocessed_test_text)

    # Вывод результата
    #print("Text:", vigenere(test_text, "student"))
    print("Sentiment:", result)

