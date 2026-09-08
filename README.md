# 🎭 TorD — Truth or Dare

Модуль «Правда или действие» для [Heroku](https://github.com/coddrago/Heroku) / Hikka userbot с инлайн-кнопками, несколькими режимами интенсивности и поддержкой игры как вживую, так и удалённо.

---

## Возможности

- Инлайн-интерфейс (без лишних команд во время игры)
- Три режима интенсивности:
  - 🍃 **Лёгкий** — дружеские вопросы и задания без неловкости
  - 🌶 **Хот** — лёгкий флирт, комплименты, близость
  - 🔥 **Хард (18+)** — более откровенные вопросы и задания, в том числе для парочек
- Выбор формата: **вживую** или **удалённо** (физические задания автоматически скрываются в удалённом режиме)
- Случайный выбор «Правда / Действие»
- Система наказаний
- Блокировка «только Правда» на несколько ходов
- Полная локализация (русский / английский)
- Поддержка как групповых чатов, так и личных сообщений (1 на 1)

---

## Установка

### Способ 1 — через ссылку
```
.dlmod https://raw.githubusercontent.com/BigFloppa9/TorD/main/TorD.py
```

### Способ 2 — файлом
1. Скачай `TorD.py`
2. Отправь его в любой чат с юзерботом
3. Ответь на файл командой:
```
.lm
```

---

## Команды

| Команда | Описание |
|---------|----------|
| `.tord` | Начать новую игру |
| `.endgame` / `.end` | Принудительно завершить текущую игру |
| `.tordmode` | Выбрать режим (лёгкий / хот / хард) и формат (вживую / удалённо) |

---

## Как играть

1. Запусти `.tord` в чате
2. Игроки нажимают **«Присоединиться»**
3. Создатель игры нажимает **«Начать»**
4. Игроки по очереди выбирают «Правда», «Действие» или «Случайно»
5. Можно взять готовый вопрос/задание или придумать своё
6. После ответа — кнопка **«Ответил»**, либо **«Не смог ответить»** (тогда срабатывает наказание)

В личных сообщениях второй игрок просто нажимает «Присоединиться» — игра стартует автоматически.

---

## Режимы

### 🍃 Лёгкий
Подходит для любой компании. Без двусмысленностей и неловких тем.

### 🌶 Хот
Лёгкая перчинка: комплименты, флирт, небольшая близость. Для тех, кому это комфортно.

### 🔥 Хард (18+)
Более откровенные вопросы и задания. Рекомендуется только для взрослых и тех, кто заранее согласен на такой формат. Особенно хорошо заходит вдвоём.

> **Важно:** Хард-режим содержит контент 18+. Используйте осознанно и только с согласия всех участников.

---

## Настройки

Настройки сохраняются и применяются ко всем новым играм:

```
.tordmode
```

Там можно выбрать:
- Режим интенсивности
- Формат (вживую / удалённо)


## Лицензия

MIT License

Copyright (c) 2026

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

## Примечания

- Модуль написан в стиле классических инлайн-игр под Heroku/Hikka.
- Вопросы и задания можно свободно дополнять — структура пулов простая.
- Если нашли баг или есть идеи по улучшению — создавайте Issue или Pull Request.

Приятной игры 🎲
