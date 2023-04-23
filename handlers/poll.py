# Aiogram
from aiogram import types
from aiogram.dispatcher import FSMContext

# Keyboard
from keyboards.general import (YesNo_Keyboard, Finish_Poll, Remove,
                               OptionsQuiz_Keyboard, Menu_Keyboard)

# Local
from basic import log


# Responses In -> Create Poll -> Poll Title state
async def get_pollTitle(message: types.Message, state: FSMContext):
    log(message.from_id, '__Poll-Title__', message.text)
    await state.set_data({'poll_title': message.text})
    await message.answer('Is poll anonymous?', reply_markup=YesNo_Keyboard)
    await state.set_state('poll-anonymous')


# Responses In -> Create Poll -> Poll Anonymous state
async def get_pollAnonymous(message: types.Message, state: FSMContext):
    log(message.from_id, '__Poll-Anonymous__', message.text)
    yes_no = {'yes': True, 'no': False}
    if message.text.lower() in yes_no:
        await state.update_data({'poll-anonymous': yes_no.get(message.text.lower())})
        await message.answer('Is poll a quiz?', reply_markup=YesNo_Keyboard)
        await state.set_state('poll-quiz')
    else:
        await message.answer('Please choose from options below')


# Responses In -> Create Poll -> Poll Quiz State
async def get_pollQuiz(message: types.Message, state: FSMContext):
    log(message.from_id, '__Poll-Quiz__', message.text)
    yes_no = {'yes': True, 'no': False}
    if message.text.lower() == 'yes':
        await state.update_data({'poll-quiz': 'quiz'})
        await message.answer(
            'Please send poll option text. \n\n<i>If you want to finish just type Finish</i>',
            parse_mode='HTML', reply_markup=Finish_Poll
        )
        await state.set_state('poll-option')
    elif message.text.lower() == 'no':
        await message.answer('Is it possible to choose multiple-answers?')
        await state.set_state('poll-multi-ans')
    else:
        await message.answer('Please choose from option below')


# Responses In -> Create Poll -> Poll Multiple Answers State
async def get_pollMultiAns(message: types.Message, state: FSMContext):
    log(message.from_id, '__Poll-Multiple-Answers__', message.text)
    yes_no = {'yes': True, 'no': False}
    if message.text.lower() in yes_no:
        if yes_no.get(message.text.lower()):
            await state.update_data({'poll-multi-ans': yes_no.get(message.text.lower())})
        await message.answer(
            'Please send poll option text. \n\n<i>If you want to finish just type Finish</i>',
            parse_mode='HTML', reply_markup=Finish_Poll
        )
        await state.set_state('poll-option')
    else:
        await message.answer('Please choose from option below')


# Responses In -> Create Poll -> Poll Option State
async def get_pollOption(message: types.Message, state: FSMContext):
    log(message.from_id, '__Poll-Options__', message.text)
    data = await state.get_data()
    nOptions = data.get('number-poll-option') or 0
    if message.text.lower() == 'finish':
        if nOptions > 1:
            await message.answer(f'You have total {nOptions} options', reply_markup=Remove)
            if data.get('poll-quiz'):
                await message.answer(
                    'Please choose between option, which is correct answer for quiz.',
                    reply_markup=OptionsQuiz_Keyboard(nOptions, data)
                )
                await state.set_state('poll-quiz-ans')
            else:
                options = [data.get(f'poll-option-{i}') for i in range(1, data.get('number-poll-option') + 1)]
                await message.answer_poll(
                    question=data.get('poll_title'),
                    is_anonymous=data.get('poll-anonymous'),
                    type=data.get('poll-quiz') or 'regular',
                    allows_multiple_answers=data.get('poll-multi-ans'),
                    options=options,
                    reply_markup=Menu_Keyboard
                )
                await state.set_state('menu')
        else:
            await message.answer('Please add at least 2 option')
    else:
        nOptions += 1
        await state.update_data({'number-poll-option': nOptions, f'poll-option-{nOptions}': message.text})
        await message.answer(
            'Option added! \n\nSend text for next option. \n\n<i>If you want to finish just type Finish</i>',
            parse_mode='HTML', reply_markup=Finish_Poll
        )


# Responses In -> Create Poll -> Poll Quiz Answer State
async def get_pollQuizAns(callback: types.CallbackQuery, state: FSMContext):
    log(callback.from_user.id, '__Poll-Quiz-Ans__', callback.data)
    data = await state.get_data()
    if callback.data in data:
        await callback.message.delete()

        ops = [data.get(f'poll-option-{i}') for i in range(1, data.get('number-poll-option') + 1)]
        await callback.message.answer_poll(
            question=data.get('poll_title'),
            is_anonymous=data.get('poll-anonymous'),
            type=data.get('poll-quiz') or 'regular',
            allows_multiple_answers=data.get('poll-multi-ans'),
            options=ops,
            correct_option_id=int(callback.data[-1]),
            reply_markup=Menu_Keyboard
        )
        await callback.message.answer('menu')
    else:
        return
