from aiogram.dispatcher.filters.state import StatesGroup, State


class OrderState(StatesGroup):

    Buy = State()
    Sell = State()
    VerifyManager = State()
    Processing = State()
    AddingCourse = State()
    EditingCourse = State()
    RemovingCourse = State()
    Cancelling = State()
    Completing = State()