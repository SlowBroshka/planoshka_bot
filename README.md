# planoshka_bot

Небольшой таск менеджер:
1. На вход бот получает сообщение/файл
2. Выбирается дата и время
3. По наступлении даты и времени бот отправляет сообщение-напоминание (reply отправленного сообщения)

### Quick start

```
git clone https://github.com/SlowBroshka/planoshka_bot.git
cd planoshka_bot
python3.8.3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3.8.3 main.py
```