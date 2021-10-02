from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.utils import executor
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import TOKEN2
import text_or_question as text
import keaboard as kb
import time
import datetime
import asyncio

from db_admin import DateBase

datebase = DateBase('users.db')

bot = Bot(token=TOKEN2)
db = Dispatcher(bot, storage=MemoryStorage())

user_list1 = []
user_list2 = []
user_list3 = []
user_list4 = []
user_list5 = []
user_list6 = []
user_list7 = []


class Form(StatesGroup):
    info_text = State()
    user_delete = State()


@db.message_handler(commands=['start'])
async def greetings(message: types.Message):
    user_id = message.chat.id
    user_username = '@' + message.from_user.username
    try:
        datebase.records_of_all_users(user_username, user_id)
    except Exception as e:
        print(e)
    await message.answer_photo(text.hi_photo_id, caption=text.hi_text, reply_markup=kb.the_first_go_button)


@db.message_handler(commands=['status'])
async def status(message: types.Message):
    count_user = datebase.count_string()
    cunt_mailing_user = datebase.count_string2()
    status_string = 'На ваш бот зашло: ' + str(count_user) + ' человек\nРассылку получат ' + str(cunt_mailing_user) + \
                    'человек.\nБаза данных доступна по команде: /send_db\n'
    await message.answer(status_string)


@db.message_handler(commands=['mailing'], content_types=['text', 'photo', 'video_note', 'video', 'voice'])
async def mailing(message: types.Message):
    await message.answer('Введите текст, который хотите разослать.')
    await Form.info_text.set()


@db.message_handler(commands=['send_db'], content_types=['text', 'document'])
async def send_db(message: types.Message):
    await message.answer("База данных.")
    await message.answer_document(open("users.db", "rb"))


@db.message_handler(commands=['delus'])
async def delete_user_message(message: types.Message):
    await message.answer('Скиньте сообщение с тем, кого хотите удалить из бд')
    await Form.user_delete.set()


@db.message_handler(state=Form.user_delete)
async def delete_user(message: types.Message, state: FSMContext):
    if message.text == 'отмена':
        await state.finish()
        await message.answer('отменено')
    else:
        user_id = message.forward_from.id
        try:
            datebase.delete_user(user_id)
        except Exception as e:
            print(e)
        await state.finish()
        await message.answer('Пользователь удалён.')


@db.message_handler(state=Form.info_text, content_types=['text', 'photo', 'video_note', 'video', 'voice'])
async def send_mailing_text(message: types.Message, state: FSMContext):
    if message.text == 'отмена':
        await state.finish()
        await message.answer('отменено')
    if message.text or message.photo or message.video:
        for user_id in datebase.mailing_user_id():
            if message.text and message.photo:
                await bot.send_photo(user_id[1], message.photo[2].file_id, caption=message.text)
            elif message.text and message.video:
                await bot.send_video(user_id[1], message.video.file_id, caption=message.text)
            elif message.photo:
                await bot.send_photo(user_id[1], message.photo[2].file_id)
            elif message.video:
                await bot.send_video(user_id[1], message.video.file_id)
            elif message.text:
                await bot.send_message(user_id[1], message.text)
    elif message.video_note:
        for user_id in datebase.mailing_user_id():
            await bot.send_video_note(user_id[1], message.video_note.file_id)
    elif message.voice:
        for user_id in datebase.mailing_user_id():
            await bot.send_voice(user_id[1], message.voice.file_id)
    await message.answer('Рассылка произведена.')
    await message.answer(f'Рассылку получили {datebase.count_string2()} из {datebase.count_string()}')
    await state.finish()


@db.callback_query_handler(lambda call: True)
async def answer_push_inline_button(call):
    global user_list1
    if call.data == 'go_button':
        await call.message.answer_video_note(text.video_note_id, reply_markup=kb.pass_the_five_question)
    elif call.data == 'five_question':
        await call.message.answer_animation(text.the_first_question_gif_id, caption=text.the_first_question_text,
                                            reply_markup=kb.first_question_buttons)
    elif call.data == 'first_question':
        await call.message.delete()
        await call.message.answer_animation(text.the_second_question_gif_id, caption=text.the_second_question_text,
                                            reply_markup=kb.second_question_buttons)
    elif call.data == 'second_question':
        await call.message.delete()
        await call.message.answer_animation(text.the_third_question_gif_id, caption=text.the_third_question_text,
                                            reply_markup=kb.third_question_buttons)
    elif call.data == 'third_question':
        await call.message.delete()
        await call.message.answer_animation(text.the_fourth_question_gif_id, caption=text.the_fourth_question_text,
                                            reply_markup=kb.fourth_question_buttons)
    elif call.data == 'fourth_question':
        await call.message.delete()
        await call.message.answer_animation(text.the_five_question_gif_id, caption=text.the_five_question_text,
                                            reply_markup=kb.five_question_buttons)
    elif call.data == 'five_questions':
        await call.message.delete()
        await call.message.answer('🕺🏻А вот и обещанный бонус 🕺🏻')
        await call.message.answer_document(text.bonus_dock_file_id)
        await call.message.answer_photo(text.finished_text_file_id, caption=text.finished_text, reply_markup=kb.finished_text_button)

    elif call.data == 'go_2':
        await call.message.answer_video('BAACAgIAAxkBAAMkYVhHoBPjFCP06Kl8zf0VhKDVXmsAAskPAALV8iFKCHW1_hoeEK0hBA')
        # await call.message.answer('Первое видео')
        await asyncio.sleep(60)
        await call.message.answer(text='Жмякай кнопку пока не убежала👇', reply_markup=kb.further_button)

    elif call.data == 'further':
        await call.message.answer_video('BAACAgIAAxkBAAMlYVhHsyFzE4bcJzcjfpNRguTzqu4AAogVAALalClK2pHyf52uJv4hBA')
        # await call.message.answer('Второе видео')
        await asyncio.sleep(120)
        await call.message.answer(text='Жмякай кнопку пока не убежала👇', reply_markup=kb.futher2_button)

    elif call.data == 'further2':
        await call.message.answer_video('BAACAgIAAxkBAAMmYVhHyZGSYB59NUj_kFumCTY_rDUAAp0TAAKBgcBKCaMKOONjO6chBA', caption=
                                        'Личка - @nikolanext')
        # await call.message.answer('Третье видео')
        await asyncio.sleep(60)
        await call.message.answer(text.last_text)
        user_id = call.message.chat.id
        username = call.message.from_user.username
        user_list1.append(user_id)
        try:
            datebase.records_of_mailing_users(username, user_id)
        except Exception as e:
            print(e)


@db.message_handler(content_types=['text', 'photo', 'video_note', 'animation', 'document', 'video'])
async def all_message(message: types.Message):
    pass
    # print(message.video.file_id)
    # print(message.photo[2].file_id)
    # print(message.video_note.file_id)
    # print(message.animation.file_id)
    # print(message.document.file_id)
    # await message.answer_video_note(text.video_note_id)


async def send_to_a_certain_hour():
    while True:
        offset = datetime.timezone(datetime.timedelta(hours=3))
        now_time = datetime.datetime.now(offset)
        if now_time.hour == 16:
            for user7 in user_list7:
                await bot.send_message(user7, text=text.dayly_text7)
                user_list7.remove(user7)

            for user6 in user_list6:
                await bot.send_photo(user6, photo=text.dayly_photo_id6, caption=text.dayly_text6)
                user_list7.append(user6)
                user_list6.remove(user6)

            for user5 in user_list5:
                await bot.send_photo(user5, photo=text.dayly_photo_id5, caption=text.dayly_text5)
                user_list6.append(user5)
                user_list5.remove(user5)

            for user4 in user_list4:
                await bot.send_photo(user4, photo=text.dayly_photo_id4, caption=text.dayly_text4)
                user_list5.append(user4)
                user_list4.remove(user4)

            for user3 in user_list3:
                await bot.send_photo(user3, photo=text.dayly_photo_id3, caption=text.dayly_text3)
                user_list4.append(user3)
                user_list3.remove(user3)

            for user2 in user_list2:
                await bot.send_message(user2, text=text.dayly_text2)
                user_list3.append(user2)
                user_list2.remove(user2)

            for user1 in user_list1:
                await bot.send_photo(user1, photo=text.dayly_photo_id1, caption=text.dayly_text1)
                user_list2.append(user1)
                user_list1.remove(user1)

        await asyncio.sleep(3600)


async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(send_to_a_certain_hour())
    executor.start_polling(db, on_shutdown=shutdown)
