rubbish = '! " # $ % & \' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _` { | } ~ '.split(' ')

with open(input('Open: '), 'r') as f:
    text = f.read().replace('\n', ' ')
    for i in rubbish[:-1]:
        text =  text.replace(i, '')
    lines = len(f.readlines())
    words = {}
    wordset = set(text.split(' '))
    wordset.remove('')
    number_of_words = 0
    for word in wordset:
        words[word] = text.split(' ').count(word)
        number_of_words += text.split(' ').count(word)
    letters = len(text.replace(' ', ''))
    word_max = max(words.items(), key=lambda item: item[1])
    f1 = open(f'{word_max[0]}.txt', 'w')
    f1.write(f'''number of lines: {lines}
number of words: {number_of_words}
number of letters: {letters}
''')
    for k,v in words.items():
        f1.writelines(f'{k}: {v} \n')
    f1.close()