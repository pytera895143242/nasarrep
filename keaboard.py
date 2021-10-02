from aiogram.types import ReplyKeyboardRemove, \
ReplyKeyboardMarkup, KeyboardButton, \
InlineKeyboardMarkup, InlineKeyboardButton

the_first_go_button = InlineKeyboardMarkup().add(InlineKeyboardButton('🔥Погнали🔥', callback_data='go_button'))
pass_the_five_question = InlineKeyboardMarkup().add(InlineKeyboardButton('🔻 Пройти 5 тестов 🔻', callback_data='five_question'))

first_k_word1 = InlineKeyboardButton('К', callback_data='first_question')
second_a_word1 = InlineKeyboardButton('А', callback_data='first_question')
third_i_word1 = InlineKeyboardButton('Й', callback_data='first_question')
fourth_f_word1 = InlineKeyboardButton('Ф', callback_data='first_question')

first_question_buttons = InlineKeyboardMarkup(row_width=4).add(first_k_word1, second_a_word1, third_i_word1, fourth_f_word1)

first_k_word2 = InlineKeyboardButton('К', callback_data='second_question')
second_a_word2 = InlineKeyboardButton('А', callback_data='second_question')
third_i_word2 = InlineKeyboardButton('Й', callback_data='second_question')
fourth_f_word2 = InlineKeyboardButton('Ф', callback_data='second_question')

second_question_buttons = InlineKeyboardMarkup(row_width=4).add(first_k_word2, second_a_word2, third_i_word2, fourth_f_word2)

first_k_word3 = InlineKeyboardButton('К', callback_data='third_question')
second_a_word3 = InlineKeyboardButton('А', callback_data='third_question')
third_i_word3 = InlineKeyboardButton('Й', callback_data='third_question')
fourth_f_word3 = InlineKeyboardButton('Ф', callback_data='third_question')

third_question_buttons = InlineKeyboardMarkup(row_width=4).add(first_k_word3, second_a_word3, third_i_word3, fourth_f_word3)

first_k_word4 = InlineKeyboardButton('К', callback_data='fourth_question')
second_a_word4 = InlineKeyboardButton('А', callback_data='fourth_question')
third_i_word4 = InlineKeyboardButton('Й', callback_data='fourth_question')
fourth_f_word4 = InlineKeyboardButton('Ф', callback_data='fourth_question')

fourth_question_buttons = InlineKeyboardMarkup(row_width=4).add(first_k_word4, second_a_word4, third_i_word4, fourth_f_word4)

first_k_word5 = InlineKeyboardButton('К', callback_data='five_questions')
second_a_word5 = InlineKeyboardButton('А', callback_data='five_questions')
third_i_word5 = InlineKeyboardButton('Й', callback_data='five_questions')
fourth_f_word5 = InlineKeyboardButton('Ф', callback_data='five_questions')

five_question_buttons = InlineKeyboardMarkup(row_width=4).add(first_k_word5, second_a_word5, third_i_word5, fourth_f_word5)

finished_text_button = InlineKeyboardMarkup().add(InlineKeyboardButton('🕹 Погнали 🕹', callback_data='go_2'))

further_button = InlineKeyboardMarkup().add(InlineKeyboardButton('💥 Далее 💥', callback_data='further'))

futher2_button = InlineKeyboardMarkup().add(InlineKeyboardButton('💥 Спринт 💥', callback_data='further2'))




