import random


repeat_list = ['Повторите ещё раз!','Повторите ещё раз','Репит плиз🥺','Не работает,попробуй ещё раз','Повторение - мать учения\nСоветую повторить']

joke_potato_list = ['Да это рофл был бро...\n\nМы все знаем что есть только 2 гендера - трансформер и водка)','шутка бро,ист джоук :)']

else_list = ['Я не знаю, что с этим делать 😲\n\nЯ просто напомню, что есть команда /start =)','ненаю что с этим делать🥺\n\nЯ просто напомню, что есть команда /start =)']
def random_reapeat_list():
	return random.choice(repeat_list)
def too_long():
	return 'Слишком много текста!'
def joke_first():
	return random.choice(joke_potato_list)
def else_list():
	return random.choice(else_list)