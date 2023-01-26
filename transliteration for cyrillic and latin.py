def transliteration_for_cyrrillic(proposal):
    transliteration = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'jo', 'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'j',
     'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f',
     'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh', 'щ': 'shh', 'ъ': '*', 'ы': 'y', 'ь': "'", 'э': 'je', 'ю': 'ju',
     'я': 'ya', 'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'Jo', 'Ж': 'Zh', 'З': 'Z', 'И': 'I',
     'Й': 'J', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U',
     'Ф': 'F', 'Х': 'H', 'Ц': 'C', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shh', 'Ы': 'Y', 'Э': 'Je', 'Ю': 'Ju',
     'Я': 'Ya'}

    otv = ''

    for i in range(len(proposal)):
        if proposal[i] in transliteration.keys():
            otv += transliteration[proposal[i]]
        else:
            otv += proposal[i]

    return f'\nПеревод: {otv}'


def transliteration_for_latin(proposal):
    transliteration = {'a': 'а', 'b': 'б', 'v': 'в', 'g': 'г', 'd': 'д', 'e': 'е', 'jo': 'ё', 'zh': 'ж', 'z': 'з', 'i': 'и', 'j': 'й',
     'k': 'к', 'l': 'л', 'm': 'м', 'n': 'н', 'o': 'о', 'p': 'п', 'r': 'р', 's': 'с', 't': 'т', 'u': 'у', 'f': 'ф',
     'h': 'х', 'c': 'ц', 'ch': 'ч', 'sh': 'ш', 'shh': 'щ', '*': 'Ъ', 'y': 'ы', "'": 'Ь', 'je': 'э', 'ju': 'ю',
     'ya': 'я', 'A': 'А', 'B': 'Б', 'V': 'В', 'G': 'Г', 'D': 'Д', 'E': 'Е', 'Jo': 'Ё', 'Zh': 'Ж', 'Z': 'З', 'I': 'И',
     'J': 'Й', 'K': 'К', 'L': 'Л', 'M': 'М', 'N': 'Н', 'O': 'О', 'P': 'П', 'R': 'Р', 'S': 'С', 'T': 'Т', 'U': 'У',
     'F': 'Ф', 'H': 'Х', 'C': 'Ц', 'Ch': 'Ч', 'Sh': 'Ш', 'Shh': 'Щ', 'Y': 'Ы', 'Je': 'Э', 'Ju': 'Ю', 'Ya': 'Я'}

    otv = ''

    for i in range(len(proposal)):
        if proposal[i] in transliteration.keys():
            otv += transliteration[proposal[i]]
        else:
            otv += proposal[i]

    return f'Перевод: {otv}'


flag = True
choice = input('If you need transliteration from Russian to English write "r", else "e"/'
               'Если нужна транслитерация с Русского на Английский напиши "р", иначе "а"')


while flag:
    if choice.lower() in 'rhрк':
        print(transliteration_for_cyrrillic(input('Write a sentence for transliteration:/Напиши предложение для транслитерации:')))
        choice = input('If you want more, write "r" or "e". To exit, press any other key/'
                       'Если хочешь ещё, напиши "р" или "а". Для выхода нажми любую другую клавишу')
        if choice.lower() not in 'rhркfaуe':
            flag = False

    elif choice in 'faeу':
        print(transliteration_for_latin(input('Write a sentence for transliteration:/Напиши предложение для транслитерации:')))
        choice = input('If you want more, write "r" or "e". To exit, press any other key/'
                       'Если хочешь ещё, напиши "р" или "а". Для выхода нажми любую другую клавишу')
        if choice.lower() not in 'rhркfaуe':
            flag = False

    else:
        input('Please write "r" if you need transliteration from Russian to English, else "e"/'
              'Пожалуйста напиши "р" если нужна транслитерация с Русского на Английский, иначе "а"')
