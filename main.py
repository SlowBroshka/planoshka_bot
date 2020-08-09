from aiogram import executor

from main_help import dp
import handlers


def main():
     executor.start_polling(dp)


if __name__ == '__main__':
    main()
