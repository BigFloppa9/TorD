# Commands: .TorD | .endgame (.end) | .TorDmode
# meta developer: @RoKrz

__version__ = (1, 2)

import asyncio
import random
from .. import loader, utils

RULES_URL = "https://ru.wikipedia.org/wiki/Правда_или_действие"


@loader.tds
class TorDMod(loader.Module):
    """Truth or Dare game with inline buttons, in the style of the RPS module"""

    strings = {
        "name": "TorD",
        "lang_code": "en",
        "_cls_doc": "Truth or Dare game with inline buttons (light / hot / hard modes, in-person or remote)",
        "already_running": "⚠ A game is already running in this chat, use <code>{}endgame</code> to end it.",
        "no_active_game": "⚠ There's no active game in this chat",
        "wait_title": "<b>🎭 The game «Truth or Dare» begins!</b>",
        "wait_title_dm": "<b>🎭 The game «Truth or Dare» begins!</b>\n👀 Waiting for the second player...",
        "players_label": "<b>Players:</b>",
        "wait_footer": "👀 Waiting for players...",
        "btn_rules": "📄 How to play",
        "btn_join": "🎲 Join",
        "btn_begin": "▶️ Start",
        "already_joined": "⚠ You're already in the game",
        "game_started": "⚠ The game has already started",
        "not_owner": "⚠ Only whoever started the game can begin it",
        "error_play_yourself": "⚠ You can't play against yourself",
        "turn": "<b>🎯 {}'s turn.</b>\nChoose...",
        "truth": "🤍 Truth",
        "dare": "🔥 Dare",
        "btn_random": "🎲 Random",
        "btn_leave": "🚪 Leave",
        "not_in_lobby": "⚠ You're not in the game",
        "lobby_closed": "<b>🏁 Lobby closed — everyone left.</b>",
        "random_tag": " [🎲RANDOM]",
        "not_your_turn": "⚠ It's not your turn",
        "truth_locked": "⚠ You can only choose Truth for the next few turns",
        "no_permission": "⚠ This isn't for you",
        "chosen": "<b>{} chose: {}.</b>",
        "ask_prompt_truth": "{}, ask your question...",
        "ask_prompt_dare": "{}, give your dare...",
        "label_truth": "Question: {}",
        "label_dare": "Dare: {}",
        "btn_take_truth": "🎴 Random question",
        "btn_take_dare": "🎴 Random dare",
        "btn_answered": "✅ Answered",
        "btn_failed": "❌ Couldn't answer (Punishment)",
        "punishment_intro": "<b>🔥 Punishment.</b>\nThis can't be declined — refuse it and you're out of the game.",
        "punishment_header": "<b>🔥 Punishment ({})</b>",
        "btn_back": "◀️ Back",
        "game_ended": "<b>🏁 Game over!</b>",
        "game_ended_few": "<b>🏁 Game over — fewer than 2 players left.</b>",
        "btn_close": "🔻 Close",
        "mode_title": "<b>🎮 Choose the game intensity</b>",
        "btn_select": "✅ Select",
        "mode_light": "🍃 Light",
        "mode_light_desc": "🍃 <b>Light mode</b>\n\nSimple, friendly questions and dares, no awkwardness — works for any group.",
        "mode_hot": "🌶 Hot",
        "mode_hot_desc": "🌶 <b>Hot mode</b>\n\nA bit of spice — compliments, flirting, some closeness. For friends who are comfortable with that.",
        "mode_hard": "🔥 Hard",
        "mode_hard_desc": "🔥 <b>Hard mode (18+)</b>\n\nBolder and more intimate — kisses, closeness, spicy questions. Only for adults who are genuinely up for it (especially couples).",
        "realism_real": "🏠 In person",
        "realism_virtual": "💻 Remote",
        "player_n": "Player {}",
    }

    strings_ru = {
        "lang_code": "ru",
        "_cls_doc": "Игра «Правда или действие» с инлайн-кнопками (режимы лёгкий / хот / хард, вживую или удалённо)",
        "already_running": "⚠ Игра уже идёт в этом чате, используйте <code>{}endgame</code>, чтобы завершить её.",
        "no_active_game": "⚠ Сейчас нет активной игры в этом чате",
        "wait_title": "<b>🎭 Игра «Правда или действие» начинается!</b>",
        "wait_title_dm": "<b>🎭 Игра «Правда или действие» начинается!</b>\n👀 Ожидание второго игрока...",
        "players_label": "<b>Игроки:</b>",
        "wait_footer": "👀 Ожидание игроков...",
        "btn_rules": "📄 Как играть",
        "btn_join": "🎲 Присоединиться",
        "btn_begin": "▶️ Начать",
        "already_joined": "⚠ Вы уже в игре",
        "game_started": "⚠ Игра уже началась",
        "not_owner": "⚠ Начать игру может только тот, кто её запустил",
        "error_play_yourself": "⚠ Нельзя играть самому с собой",
        "turn": "<b>🎯 Ход {}.</b>\nВыбирай...",
        "truth": "🤍 Правда",
        "dare": "🔥 Действие",
        "btn_random": "🎲 Случайно",
        "btn_leave": "🚪 Выйти",
        "not_in_lobby": "⚠ Вы не участвуете",
        "lobby_closed": "<b>🏁 Лобби закрыто — все вышли.</b>",
        "random_tag": " [🎲RANDOM]",
        "not_your_turn": "⚠ Сейчас не ваш ход",
        "truth_locked": "⚠ Следующие несколько ходов доступна только Правда",
        "no_permission": "⚠ Это не для вас",
        "chosen": "<b>{} выбрал(-а): {}.</b>",
        "ask_prompt_truth": "{}, задавайте ваш вопрос...",
        "ask_prompt_dare": "{}, давайте ваше задание...",
        "label_truth": "Вопрос: {}",
        "label_dare": "Задание: {}",
        "btn_take_truth": "🎴 Взять случайный вопрос",
        "btn_take_dare": "🎴 Взять случайное задание",
        "btn_answered": "✅ Ответил(-а)",
        "btn_failed": "❌ Не смог(-ла) ответить (Наказание)",
        "punishment_intro": "<b>🔥 Наказание.</b>\nОт этого нельзя отказаться — откажешься, и вылетаешь из игры.",
        "punishment_header": "<b>🔥 Наказание ({})</b>",
        "btn_back": "◀️ Назад",
        "game_ended": "<b>🏁 Игра завершена!</b>",
        "game_ended_few": "<b>🏁 Игра завершена — осталось меньше 2 игроков.</b>",
        "btn_close": "🔻 Закрыть",
        "mode_title": "<b>🎮 Выберите режим игры</b>",
        "btn_select": "✅ Выбрать",
        "mode_light": "🍃 Лёгкий",
        "mode_light_desc": "🍃 <b>Лёгкий режим</b>\n\nПростые, дружеские вопросы и задания без неловкости — подходит для любой компании.",
        "mode_hot": "🌶 Хот",
        "mode_hot_desc": "🌶 <b>Хот режим</b>\n\nС лёгкой перчинкой — комплименты, флирт, немного близости. Для друзей, которым это комфортно.",
        "mode_hard": "🔥 Хард",
        "mode_hard_desc": "🔥 <b>Хард режим (18+)</b>\n\nСмелее и откровеннее — поцелуи, близость, острые вопросы. Только для взрослых, которые точно готовы (особенно для парочек).",
        "realism_real": "🏠 Вживую",
        "realism_virtual": "💻 Удалённо",
        "player_n": "Игрок {}",
    }

    MODES = ("light", "hot", "hard")

    QUESTIONS = {
        "ru": {
            "light_truth": [
                "Какое твоё самое странное детское воспоминание?",
                "Кого из присутствующих ты знаешь дольше всех?",
                "Какая твоя худшая привычка?",
                "Если бы ты мог(-ла) прожить один день кем-то другим, кем бы ты стал(-а)?",
                "Какой твой самый нелепый страх?",
                "За что тебе стыдно, о чём ты никогда никому не рассказывал(-а)?",
                "Какую песню ты стесняешься признать, что любишь?",
                "Самое странное блюдо, которое ты пробовал(-а)?",
                "Если бы ты выиграл(-а) в лотерею 100 000 ₽, на что потратил(-а) бы их первым делом?",
                "О чём ты в последний раз безобидно соврал(-а)?",
                "В детстве какой мультфильм был твоим любимым?",
                "Кем ты мечтал(-а) стать в детстве?",
                "Было ли что-то, что ты взял(-а) без спроса и никому не признался(-лась)?",
                "Убегал(-а) ли ты когда-нибудь от охраны магазина или строгого учителя?",
                "Какая твоя самая нелепая привычка, о которой не знают родители?",
                "Если бы ты мог(-ла) узнать ответ на один вопрос о своём будущем, что бы спросил(-а)?",
                "Какое дело или домашнее задание ты откладывал(-а) дольше всего?",
                "Какой самый нелепый секрет о тебе знает твой лучший друг?",
                "Какой самый странный сон тебе снился за последний месяц?",
                "Если бы у тебя была машина времени на один час — куда бы отправился(-ась)?",
                "Какая самая глупая покупка в твоей жизни?",
                "Что ты обычно делаешь, когда остаёшься дома один(-а)?",
                "Какой фильм или сериал ты пересматривал(-а) больше всего раз?",
            ],
            "light_dare": [
                "Спой куплет любой песни голосовым сообщением",
                "Расскажи анекдот",
                "Сделай скриншот и покажи свои обои рабочего стола телефона",
                "Покажи последнее фото в своей галерее, если оно не личное",
                "Напиши самое странное слово, которое выдаёт автозаполнение твоего телефона",
                "Съешь что-нибудь с закрытыми глазами и угадай, что это",
                "Покажи, сколько непрочитанных чатов у тебя в мессенджере",
                "Отправь голосовое, в котором рассказываешь стих из школьной программы",
                "Найди самое старое фото в галерее и опиши его одним предложением",
                "Покажи, сколько у тебя сейчас открыто вкладок в браузере",
                "Напиши любому контакту случайный милый комплимент",
                "Отправь голосовое с фразой из любимого фильма максимально драматично",
                "Смени имя в чате на что-то максимально глупое на 3 хода",
                "Отправь голосовое, где 20 секунд рассказываешь о своём дне голосом робота",
                ("Изобрази любимое животное без слов, пока остальные угадывают", "REAL_ONLY"),
                ("Станцуй 15 секунд под музыку, которую поставят остальные", "REAL_ONLY"),
                ("Изобрази походку робота через всю комнату", "REAL_ONLY"),
                ("Покажи самое смешное выражение лица, на которое способен(-на)", "REAL_ONLY"),
            ],
            "light_truth_punish": [
                "Какая самая постыдная вещь, которую ты когда-либо делал(-а) на людях?",
                "Что самое отвратительное ты когда-либо ел(-а) не по своей воле?",
                "Расскажи о моменте, когда тебе было максимально стыдно за себя",
                "Какую свою вредную привычку ты скрываешь от всех?",
                "За что тебя последний раз ругали родители или близкие?",
                "Что бы ты никогда не хотел(-а), чтобы узнали присутствующие о тебе?",
                "Расскажи о самой глупой ошибке, которую ты совершил(-а)",
                "Какой твой самый неловкий момент в общественном месте?",
                "Что ты делаешь, когда думаешь, что никто не видит?",
                "Какая самая большая ложь, в которую все поверили?",
                "Какая оценка или результат тебя больше всего расстроили за последний год?",
                "Расскажи о самом неловком сообщении, которое ты случайно отправил(-а) не тому человеку",
            ],
            "light_dare_punish": [
                "Спой любую песню оперным голосом голосовым сообщением",
                "Позвони случайному контакту, скажи «я тебя люблю» и попрощайся",
                "Отправь голосовое, где 30 секунд без остановки хвалишь самого себя",
                "Смени аватарку на самую нелепую картинку, какую найдёшь, на 10 минут",
                "Напиши в статусе мессенджера что-то максимально нелепое на 5 минут",
                "Отправь голосовое с самым детским стихом, какой вспомнишь, максимально серьёзно",
                "Покажи все закреплённые сообщения в самом заспамленном своём чате",
                "Съешь ложку любой приправы, какую найдёшь, без вреда для здоровья",
                "Напиши случайному контакту максимально странный вопрос",
                "Отправь голосовое, где изображаешь 3 разных животных подряд",
                "На 2 хода пиши все сообщения только ЗАГЛАВНЫМИ БУКВАМИ",
                ("Изобрази истерику двухлетнего ребёнка 20 секунд", "REAL_ONLY"),
                ("Дай любому желающему нарисовать что-то у тебя на руке ручкой", "REAL_ONLY"),
            ],
            "hot_truth": [
                "Кто из присутствующих тебе симпатичен чисто внешне?",
                "Расскажи про свой первый поцелуй",
                "Самое романтичное, что ты когда-либо делал(-а) ради кого-то?",
                "Какая черта во внешности человека для тебя самая привлекательная?",
                "Была ли у тебя влюблённость в друга или подругу, и в кого?",
                "Куда тебя целовали, и тебе это понравилось больше всего?",
                "Что тебя смущает больше всего в разговорах о чувствах?",
                "Какое было самое неловкое свидание в твоей жизни?",
                "Какой комплимент о своей внешности ты любишь получать больше всего?",
                "Ты когда-нибудь носил(-а) одежду своего парня или девушки?",
                "Кого ты предпочтёшь: красивого, но глупого, или умного, но невзрачного?",
                "Кто из присутствующих лучше всех умеет флиртовать, на твой взгляд?",
                "Какой самый милый комплимент тебе когда-либо говорили?",
                "Было ли у тебя «любовь с первого взгляда»?",
                "Что для тебя важнее в отношениях: внешность или характер?",
                "Какой жест заботы от партнёра тебя больше всего растапливает?",
            ],
            "hot_dare": [
                "Сделай комплимент внешности {target}",
                "Напиши {target} самое доброе, что можешь сказать прямо сейчас",
                "Отправь {target} голосовое с комплиментом",
                "Напиши {target}, как будто шепчешь ей/ему на ухо что-то приятное",
                "Скажи {target}, почему он/она тебе нравится",
                "Отправь {target} стикер, который лучше всего описывает твои чувства к нему/ней сейчас",
                "Напиши {target}: «*обнимает*» — и опиши это действие одним предложением",
                "Позвони {target} и продержи разговор 30 секунд ни о чём",
                "Придумай для {target} ласковое прозвище и используй его до конца игры",
                "Скажи {target} комплимент, которого ты никогда раньше не говорил(-а)",
                "Напиши {target} сообщение так, будто вы уже встречаетесь уже месяц",
                ("В следующих 3 своих ходах ты сможешь выбирать только «Правда»", "TRUTH_LOCK_3"),
                ("Обними {target} по-настоящему", "REAL_ONLY"),
                ("Подержи за руку {target} один круг", "REAL_ONLY"),
                ("Посмотри в глаза {target} 20 секунд, не отводя взгляд", "REAL_ONLY"),
                ("Пригласи {target} на медленный танец на 10 секунд", "REAL_ONLY"),
            ],
            "hot_truth_punish": [
                "Расскажи о своём самом неловком свидании в подробностях",
                "Кто из присутствующих был бы твоим идеальным партнёром, и почему именно он/она?",
                "Расскажи о моменте, когда тебя отвергли романтически",
                "Какая твоя главная неуверенность в отношениях?",
                "Опиши свой первый влюблённый взгляд в этой компании, если он был",
                "Расскажи максимально честно про свои прошлые отношения — что пошло не так",
                "Кто из присутствующих тебе нравился раньше, но ты никогда не признавался(-лась)?",
                "Какое самое неловкое сообщение ты когда-либо отправлял(-а) человеку, который тебе нравился?",
                "Расскажи, как ты обычно проявляешь симпатию к человеку",
                "Какой самый неудачный флирт с твоей стороны был в жизни?",
                "Что тебя больше всего пугает в серьёзных отношениях?",
            ],
            "hot_dare_punish": [
                "Напиши каждому игроку по одному комплименту об их внешности",
                "Отправь {target} голосовое с комплиментом",
                "Позволь {target} выбрать тебе имя в чате на следующие 2 хода",
                "Скажи вслух три вещи, которые тебе нравятся во внешности {target}",
                "Напиши каждому игроку одно доброе слово в личные сообщения",
                "Придумай ласковое прозвище для {target} и используй его до конца игры",
                "Отправь {target} голосовое, где серенадишь любой строчкой песни",
                "Позволь {target} написать за тебя один следующий ответ в игре",
                "Напиши {target} признание в стиле «я всегда хотел(а) сказать...»",
                ("Обними каждого игрока по кругу", "REAL_ONLY"),
                ("Держи за руку {target} до конца следующего полного круга", "REAL_ONLY"),
                ("Пройдись «модельной» походкой через комнату", "REAL_ONLY"),
            ],
            "hard_truth": [
                "О ком из присутствующих у тебя были романтические мысли?",
                "Расскажи о самом неловком романтическом моменте в своей жизни",
                "Кого из присутствующих ты бы поцеловал(-а) прямо сейчас, если бы мог(-ла)?",
                "Опиши свой идеальный первый вечер наедине с кем-то",
                "Было ли у тебя романтическое чувство к другу из этой компании?",
                "Какое место тебе больше всего нравится, когда его целуют?",
                "Расскажи о самом смелом флирте, который ты когда-либо предпринимал(-а)",
                "Если бы нужно было выбрать, с кем из присутствующих провести романтический вечер, кого бы выбрал(-а)?",
                "Какая твоя самая смелая романтическая фантазия, в общих чертах?",
                "Кому из присутствующих ты бы разрешил(-а) себя поцеловать без раздумий?",
                "Опиши свою самую горячую фантазию, которую готов(-а) рассказать вслух",
                "Что тебя сильнее всего возбуждает в партнёре (характер / внешность / поведение)?",
                "Какой самый интимный комплимент тебе когда-либо говорили?",
                "Ты предпочитаешь быть сверху или снизу? Или как получится?",
                "Какая часть тела у тебя самая чувствительная?",
                "Расскажи о самом страстном поцелуе в своей жизни",
                "Было ли у тебя желание прямо сейчас с кем-то из присутствующих?",
                "Что бы ты сделал(-а) с партнёром, если бы у вас была целая ночь наедине без ограничений?",
                "Какой самый смелый поступок в постели ты когда-либо совершал(-а)?",
                "Скинь (или опиши) фото своей самой сексуальной, на твой взгляд, части тела",
            ],
            "hard_dare": [
                "Напиши {target}: «*целует в щёку*»",
                "Напиши {target} самое смелое признание, на которое способен(-на) прямо сейчас",
                "Отправь {target} голосовое, в котором прошепчешь что-то романтичное",
                "Придумай для {target} романтичное прозвище и используй его до конца игры",
                "Напиши {target}: «*обнимает и не отпускает 15 секунд*»",
                "Скажи {target} самый смелый комплимент, какой только придумаешь",
                "Позвони {target} и скажи вслух одно романтичное предложение",
                "Напиши {target}, каким было бы твоё идеальное свидание с ним/ней",
                "Отправь {target} голосовое, где медленно и тихо описываешь, что бы ты с ним/ней сделал(-а)",
                "Напиши {target}: «Скинь что-нибудь горячее» и дождись реакции",
                "Скинь {target} фото в белье / самом открытом наряде, который готов(-а) показать (можно частичное)",
                "Опиши голосом {target}, что бы ты сделал(-а) с ним/ней прямо сейчас, если бы вы были наедине",
                "Напиши {target} самое грязное сообщение, на которое хватит смелости",
                ("Поцелуй {target} в щёку", "REAL_ONLY"),
                ("Поцелуй {target} в губы, только если оба согласны", "REAL_ONLY"),
                ("Сядь на колени {target} на следующие 2 своих хода", "REAL_ONLY"),
                ("Потанцуй медленный танец с {target} 20 секунд, глядя друг другу в глаза", "REAL_ONLY"),
                ("Проведи рукой по волосам {target}", "REAL_ONLY"),
                ("Позволь {target} поцеловать тебя в шею", "REAL_ONLY"),
            ],
            "hard_truth_punish": [
                "Расскажи максимально подробно и честно про свою самую смелую романтическую фантазию",
                "Кого из присутствующих ты бы выбрал(-а) для романтического вечера без раздумий, и почему?",
                "Расскажи про самый смелый поступок, который ты совершил(-а) ради романтического интереса",
                "Опиши в деталях идеальный поцелуй, каким ты его представляешь",
                "Кто из присутствующих, по-твоему, лучше всех целуется? Предположи, если не знаешь",
                "Расскажи максимально честно, что тебя больше всего привлекает в людях физически",
                "Была ли у тебя фантазия про кого-то из присутствующих? Признай честно, без деталей",
                "Расскажи про самый романтичный или смелый момент близости в твоей жизни, без интимных подробностей",
                "Если бы можно было провести романтический вечер с кем угодно из присутствующих без последствий, кого бы выбрал(-а)?",
                "Признай честно, кто из присутствующих тебе кажется самым привлекательным",
                "Опиши свою самую грязную фантазию, которую готов(-а) озвучить",
                "Какой самый интимный опыт ты готов(-а) рассказать прямо сейчас?",
                "Что ты обычно делаешь, когда очень сильно возбуждён(-а) и партнёра рядом нет?",
                "Скинь или подробно опиши самое откровенное фото/видео, которое у тебя есть (можно с лица, можно без)",
            ],
            "hard_dare_punish": [
                "Напиши {target}: «*целует в губы*»",
                "Отправь {target} голосовое с самым смелым признанием, какое придумаешь",
                "Придумай для {target} романтичное прозвище на весь остаток игры",
                "Позволь {target} придумать тебе следующее задание хард-режима",
                "Напиши {target} самый долгий комплимент, какой только сможешь, не останавливаясь минуту",
                "Скажи вслух, с кем из присутствующих ты бы хотел(-а) провести романтический вечер",
                "Отправь {target} голосовое, где очень тихо и горячо описываешь, что хочешь с ним/ней сделать",
                "Скинь {target} интимное фото (в белье / без верха / что готов(-а) показать). Можно с пометкой «только для тебя»",
                "Напиши {target} сообщение, после которого ему/ей должно стать очень жарко",
                "Позволь {target} выбрать, какое именно интимное задание ты выполнишь следующим",
                ("Поцелуй {target} в губы", "REAL_ONLY"),
                ("Сядь на колени {target} до конца игры или на следующие 3 хода", "REAL_ONLY"),
                ("Позволь {target} поцеловать тебя туда, куда он выберет — щека, лоб, шея или рука", "REAL_ONLY"),
                ("Потанцуй медленный танец с {target} под романтичную музыку, глядя друг другу в глаза", "REAL_ONLY"),
                ("Поцелуй в щёку каждого игрока по кругу", "REAL_ONLY"),
                ("Сними один предмет одежды на следующие 2 хода (в рамках приличия компании)", "REAL_ONLY"),
            ],
        },
        "en": {
            "light_truth": [
                "What's your strangest childhood memory?",
                "Who here have you known the longest?",
                "What's your worst habit?",
                "If you could live one day as someone else, who would you pick?",
                "What's your most ridiculous fear?",
                "What's a small thing you've never told anyone about?",
                "What song are you embarrassed to admit you love?",
                "What's the strangest food you've ever tried?",
                "If you won $10,000 in the lottery, what would you buy first?",
                "What's the last harmless lie you told?",
                "What was your favorite cartoon as a kid?",
                "What did you dream of becoming when you grew up?",
                "Have you ever taken something without asking and never admitted it?",
                "Have you ever run from store security or a strict teacher?",
                "What's a silly habit your parents don't know about?",
                "If you could learn the answer to one question about your future, what would you ask?",
                "What chore or assignment have you put off the longest?",
                "What's the silliest secret your best friend knows about you?",
                "What's the weirdest dream you've had this month?",
                "If you had a time machine for one hour, where would you go?",
                "What's the dumbest purchase you've ever made?",
                "What do you usually do when you're home alone?",
                "What movie or show have you rewatched the most?",
            ],
            "light_dare": [
                "Sing a verse of any song as a voice message",
                "Tell a joke",
                "Take a screenshot and show your phone wallpaper",
                "Show the last photo in your gallery, if it's not private",
                "Type out the weirdest word your phone's autocomplete suggests",
                "Eat something with your eyes closed and guess what it is",
                "Show how many unread chats you have",
                "Send a voice message reciting a nursery rhyme",
                "Find the oldest photo in your gallery and describe it in one sentence",
                "Show how many browser tabs you have open right now",
                "Message a random contact a random nice compliment",
                "Send a voice message quoting your favorite movie line as dramatically as possible",
                "Change your chat name to something ridiculous for 3 turns",
                "Send a voice message describing your day in a robot voice for 20 seconds",
                ("Act out your favorite animal without speaking while others guess", "REAL_ONLY"),
                ("Dance for 15 seconds to whatever song the group picks", "REAL_ONLY"),
                ("Do a robot walk across the room", "REAL_ONLY"),
                ("Show off the funniest face you can make", "REAL_ONLY"),
            ],
            "light_truth_punish": [
                "What's the most embarrassing thing you've ever done in public?",
                "What's the most disgusting thing you've ever eaten against your will?",
                "Tell us about a moment you were maximally ashamed of yourself",
                "What bad habit do you hide from everyone?",
                "What did your parents or someone close last scold you for?",
                "What's something you never want people here to find out about you?",
                "Tell us about the dumbest mistake you've ever made",
                "What's your most awkward moment in public?",
                "What do you do when you think nobody's watching?",
                "What's the biggest lie you've ever gotten away with?",
                "What grade or result upset you the most in the last year?",
                "Tell us about the most awkward message you accidentally sent to the wrong person",
            ],
            "light_dare_punish": [
                "Sing any song in full opera voice as a voice message",
                "Call a random contact, say \"I love you\", then hang up",
                "Send a voice message praising yourself non-stop for 30 seconds",
                "Change your avatar to the silliest picture you can find for 10 minutes",
                "Set your status to something as ridiculous as possible for 5 minutes",
                "Send a voice message reciting the most childish rhyme you remember, dead serious",
                "Show every pinned message in your most cluttered chat",
                "Eat a spoonful of any condiment you can find, nothing unsafe",
                "Message a random contact the weirdest question you can think of",
                "Send a voice message acting out 3 different animals in a row",
                "For the next 2 turns type everything in ALL CAPS",
                ("Throw a 20-second toddler tantrum", "REAL_ONLY"),
                ("Let anyone here draw something on your arm with a pen", "REAL_ONLY"),
            ],
            "hot_truth": [
                "Who here do you find attractive, purely looks-wise?",
                "Tell us about your first kiss",
                "What's the most romantic thing you've ever done for someone?",
                "What physical feature do you find most attractive in a person?",
                "Have you ever had a crush on a friend? Who?",
                "Where's your favorite place to be kissed?",
                "What makes you most uncomfortable when talking about feelings?",
                "What's the most awkward date you've ever been on?",
                "What kind of compliment about your looks do you love hearing most?",
                "Have you ever worn your partner's clothes?",
                "Would you rather date someone attractive but dull, or plain but brilliant?",
                "Who here do you think is the best flirt?",
                "What's the sweetest compliment you've ever received?",
                "Have you ever experienced love at first sight?",
                "What's more important to you in a relationship: looks or personality?",
                "What caring gesture from a partner melts you the most?",
            ],
            "hot_dare": [
                "Compliment {target}'s looks",
                "Send {target} the nicest thing you can think of right now",
                "Send {target} a voice message with a compliment",
                "Write to {target} as if whispering something nice in their ear",
                "Tell {target} why you like them",
                "Send {target} the sticker that best describes how you feel about them right now",
                "Message {target}: \"*hugs*\" and describe it in one sentence",
                "Call {target} and keep the conversation going for 30 seconds about nothing",
                "Come up with a nickname for {target} and use it for the rest of the game",
                "Give {target} a compliment you've never said before",
                "Message {target} as if you've already been dating for a month",
                ("For your next 3 turns, you can only choose «Truth»", "TRUTH_LOCK_3"),
                ("Actually hug {target}", "REAL_ONLY"),
                ("Hold {target}'s hand for one full round", "REAL_ONLY"),
                ("Hold eye contact with {target} for 20 seconds", "REAL_ONLY"),
                ("Ask {target} to slow dance with you for 10 seconds", "REAL_ONLY"),
            ],
            "hot_truth_punish": [
                "Describe your most awkward date in detail",
                "Who here would be your ideal partner, and why?",
                "Tell us about a time you got romantically rejected",
                "What's your biggest insecurity in relationships?",
                "Describe the first time you had a crush in this group, if ever",
                "Be brutally honest about your past relationship — what went wrong",
                "Who here did you used to like but never admitted it?",
                "What's the most awkward message you've ever sent to a crush?",
                "Tell us how you usually show someone you like them",
                "What's your most embarrassing flirting fail?",
                "What scares you the most about serious relationships?",
            ],
            "hot_dare_punish": [
                "Compliment every player's looks, one message each",
                "Send {target} a voice message with a compliment",
                "Let {target} pick your chat name for your next 2 turns",
                "Say three things out loud that you like about {target}'s looks",
                "Send every player one kind word in DMs",
                "Come up with a nickname for {target} and use it for the rest of the game",
                "Send {target} a voice message serenading them with any song lyric",
                "Let {target} write your next answer in the game for you",
                "Write {target} a confession starting with \"I've always wanted to say...\"",
                ("Hug every player in the circle", "REAL_ONLY"),
                ("Hold {target}'s hand until the end of the next full round", "REAL_ONLY"),
                ("Do a runway walk across the room", "REAL_ONLY"),
            ],
            "hard_truth": [
                "Who here have you had romantic thoughts about?",
                "Tell us about your most awkward romantic moment",
                "Who here would you kiss right now if you could?",
                "Describe your ideal first night alone with someone",
                "Have you ever had feelings for a friend in this group?",
                "Where do you like being kissed the most?",
                "Tell us about the boldest flirting move you've ever made",
                "If you had to pick someone here for a romantic evening, who would it be?",
                "What's your boldest romantic fantasy, in general terms?",
                "Who here would you let kiss you without a second thought?",
                "Describe your hottest fantasy that you're willing to say out loud",
                "What turns you on the most in a partner (personality / looks / behaviour)?",
                "What's the most intimate compliment you've ever received?",
                "Do you prefer to be on top or bottom? Or does it depend?",
                "What's your most sensitive body part?",
                "Tell us about the most passionate kiss of your life",
                "Have you felt desire for anyone here right now?",
                "What would you do with a partner if you had a whole night alone with no limits?",
                "What's the boldest thing you've ever done in bed?",
                "Send (or describe) a photo of the body part you find most sexy on yourself",
            ],
            "hard_dare": [
                "Message {target}: \"*kisses on the cheek*\"",
                "Send {target} the boldest confession you're willing to make right now",
                "Send {target} a voice message whispering something romantic",
                "Come up with a romantic nickname for {target} and use it for the rest of the game",
                "Message {target}: \"*hugs and doesn't let go for 15 seconds*\"",
                "Give {target} the boldest compliment you can think of",
                "Call {target} and say one romantic sentence out loud",
                "Tell {target} what your ideal date with them would look like",
                "Send {target} a voice message slowly and quietly describing what you'd do to them",
                "Message {target}: \"Send me something hot\" and wait for the reaction",
                "Send {target} a photo in lingerie / the most revealing outfit you're comfortable with (partial is fine)",
                "Describe to {target} in a voice message what you would do to them right now if you were alone",
                "Write {target} the dirtiest message you have the guts for",
                ("Kiss {target} on the cheek", "REAL_ONLY"),
                ("Kiss {target} on the lips, only if both agree", "REAL_ONLY"),
                ("Sit on {target}'s lap for your next 2 turns", "REAL_ONLY"),
                ("Slow dance with {target} for 20 seconds, looking into each other's eyes", "REAL_ONLY"),
                ("Run your hand through {target}'s hair", "REAL_ONLY"),
                ("Let {target} kiss your neck", "REAL_ONLY"),
            ],
            "hard_truth_punish": [
                "Describe your boldest romantic fantasy in as much detail as you're willing to",
                "Who here would you pick for a romantic evening without hesitation, and why?",
                "Tell us about the boldest thing you've done for a romantic interest",
                "Describe your idea of a perfect kiss in detail",
                "Who here do you think is the best kisser? Guess if you don't know",
                "Be completely honest about what physically attracts you most in people",
                "Have you ever had a fantasy about someone here? Admit it honestly, no details needed",
                "Tell us about the most romantic or bold moment of intimacy in your life, keep it non-explicit",
                "If you could spend a romantic evening with anyone here, no consequences, who would it be?",
                "Be honest — who here do you find the most attractive?",
                "Describe your dirtiest fantasy that you're willing to voice",
                "What's the most intimate experience you're ready to share right now?",
                "What do you usually do when you're extremely turned on and your partner isn't around?",
                "Send or describe in detail the most revealing photo/video you have (face optional)",
            ],
            "hard_dare_punish": [
                "Message {target}: \"*kisses on the lips*\"",
                "Send {target} a voice message with the boldest confession you can think of",
                "Come up with a romantic nickname for {target} for the rest of the game",
                "Let {target} come up with your next hard-mode dare",
                "Give {target} the longest compliment you can, without stopping, for a full minute",
                "Say out loud who here you'd want to spend a romantic evening with",
                "Send {target} a voice message very quietly and hotly describing what you want to do to them",
                "Send {target} an intimate photo (lingerie / topless / whatever you're comfortable with). You can mark it \"only for you\"",
                "Write {target} a message that should make them feel very hot",
                "Let {target} choose exactly which intimate task you will do next",
                ("Kiss {target} on the lips", "REAL_ONLY"),
                ("Sit on {target}'s lap for the rest of the game or your next 3 turns", "REAL_ONLY"),
                ("Let {target} kiss you wherever they choose — cheek, forehead, neck or hand", "REAL_ONLY"),
                ("Slow dance with {target} to romantic music, looking into each other's eyes", "REAL_ONLY"),
                ("Kiss every player on the cheek, one by one", "REAL_ONLY"),
                ("Remove one piece of clothing for the next 2 turns (within the group's comfort level)", "REAL_ONLY"),
            ],
        },
    }

    def __init__(self):
        self.games = {}

    def _lang(self):
        return self.strings["lang_code"]

    async def _mention(self, user_id, fallback_n):
        try:
            entity = await self._client.get_entity(user_id)
            username = getattr(entity, "username", None)
            label = f"@{username}" if username else self.strings["player_n"].format(fallback_n)
            return f'<a href="tg://user?id={user_id}">{label}</a>'
        except Exception:
            return self.strings["player_n"].format(fallback_n)

    async def _display(self, game, user_id):
        return await self._mention(user_id, game["players"].index(user_id) + 1)

    def _asker_id(self, game):
        return game["players"][(game["idx"] - 1) % len(game["players"])]

    def _pick(self, game, pool_key):
        pool = self.QUESTIONS[game["lang"]][pool_key]
        allowed = [
            i for i, item in enumerate(pool)
            if game["realism"] == "real" or not (isinstance(item, tuple) and item[1] == "REAL_ONLY")
        ]
        used = game["used"].setdefault(pool_key, set())
        available = [i for i in allowed if i not in used]
        if not available:
            used.clear()
            available = allowed
        idx = random.choice(available)
        used.add(idx)
        return pool[idx]

    async def _draw(self, game, pool_key):
        item = self._pick(game, pool_key)
        text, tag = item if isinstance(item, tuple) else (item, None)
        if tag == "TRUTH_LOCK_3":
            game.setdefault("truth_lock", {})[game["players"][game["idx"]]] = 3
        if "{target}" in text:
            others = [p for p in game["players"] if p != game["players"][game["idx"]]]
            if others:
                target_id = random.choice(others)
                text = text.format(target=await self._mention(target_id, game["players"].index(target_id) + 1))
        return text

    async def _group_wait_text(self, game):
        lines = [self.strings["wait_title"], "", self.strings["players_label"]]
        for i, uid in enumerate(game["pending"], 1):
            lines.append(f"{i}. {await self._mention(uid, i)}")
        lines += ["", self.strings["wait_footer"]]
        return "\n".join(lines)

    def _group_wait_markup(self, chat_id):
        return [
            [{"text": self.strings["btn_rules"], "url": RULES_URL}],
            [{"text": self.strings["btn_join"], "callback": self._join, "args": (chat_id,)}],
            [{"text": self.strings["btn_begin"], "callback": self._begin_click, "args": (chat_id,)}],
            [{"text": self.strings["btn_leave"], "callback": self._lobby_leave, "args": (chat_id,)}],
        ]

    def _dm_wait_markup(self, chat_id):
        return [
            [{"text": self.strings["btn_rules"], "url": RULES_URL}],
            [{"text": self.strings["btn_join"], "callback": self._join, "args": (chat_id,)}],
        ]

    async def _send_new(self, call, game, text, markup):
        try:
            await call.delete()
        except Exception:
            pass
        await self.inline.form(
            message=game["orig_message"],
            text=text,
            reply_markup=markup,
            disable_security=True,
        )

    async def _turn_text(self, game):
        return self.strings["turn"].format(await self._display(game, game["players"][game["idx"]]))

    def _turn_markup(self, chat_id, game):
        active = game["players"][game["idx"]]
        locked = game.get("truth_lock", {}).get(active, 0) > 0
        if locked:
            rows = [[{"text": self.strings["truth"], "callback": self._choose, "args": (chat_id, "truth")}]]
        else:
            rows = [
                [
                    {"text": self.strings["truth"], "callback": self._choose, "args": (chat_id, "truth")},
                    {"text": self.strings["dare"], "callback": self._choose, "args": (chat_id, "dare")},
                ],
                [{"text": self.strings["btn_random"], "callback": self._choose, "args": (chat_id, "random")}],
            ]
        rows.append([{"text": self.strings["btn_leave"], "callback": self._leave, "args": (chat_id,)}])
        return rows

    async def _asking_text(self, game):
        if game.get("punishment"):
            head = self.strings["punishment_header"].format(self.strings[game["type"]])
        else:
            type_label = self.strings[game["type"]]
            if game.get("type_was_random"):
                type_label += self.strings["random_tag"]
            head = self.strings["chosen"].format(await self._display(game, game["players"][game["idx"]]), type_label)
        if game["question"]:
            return head + "\n" + self.strings[f"label_{game['type']}"].format(game["question"])
        asker = await self._display(game, self._asker_id(game))
        return head + "\n" + self.strings[f"ask_prompt_{game['type']}"].format(asker)

    def _asking_markup(self, chat_id, game):
        rows = []
        if not game["question"]:
            rows.append(
                [{"text": self.strings[f"btn_take_{game['type']}"], "callback": self._take_question, "args": (chat_id,)}]
            )
        rows.append([{"text": self.strings["btn_answered"], "callback": self._answered, "args": (chat_id,)}])
        if not game.get("punishment"):
            rows.append([{"text": self.strings["btn_failed"], "callback": self._failed, "args": (chat_id,)}])
        rows.append([{"text": self.strings["btn_leave"], "callback": self._leave, "args": (chat_id,)}])
        return rows

    def _punishment_choice_markup(self, chat_id):
        # Always show Back. Only the person who pressed "Failed" can actually use it.
        return [
            [
                {"text": self.strings["truth"], "callback": self._punishment_type, "args": (chat_id, "truth")},
                {"text": self.strings["dare"], "callback": self._punishment_type, "args": (chat_id, "dare")},
            ],
            [{"text": self.strings["btn_back"], "callback": self._punishment_back, "args": (chat_id,)}],
        ]

    @loader.command(ru_doc="начать игру в правду или действие")
    async def tord(self, message):
        """start a game of truth or dare"""
        chat_id = message.chat_id
        if chat_id in self.games:
            prefix = utils.escape_html(self.get_prefix())
            await utils.answer(message, self.strings["already_running"].format(prefix))
            return

        try:
            message.reply_to_msg_id = None
            message.reply_to = None
        except Exception:
            pass

        owner_id = message.sender_id
        is_private = message.is_private
        game = {
            "chat_id": chat_id,
            "orig_message": message,
            "owner_id": owner_id,
            "is_private": is_private,
            "started": False,
            "pending": [owner_id],
            "players": [],
            "idx": 0,
            "mode": self.get("mode", "light"),
            "realism": self.get("realism", "virtual"),
            "lang": self._lang(),
            "type": None,
            "type_was_random": False,
            "punishment": False,
            "punishment_by": None,
            "question": None,
            "used": {},
            "lock": asyncio.Lock(),
        }
        self.games[chat_id] = game

        if is_private:
            await self.inline.form(
                message=message,
                text=self.strings["wait_title_dm"],
                reply_markup=self._dm_wait_markup(chat_id),
                disable_security=True,
            )
        else:
            await self.inline.form(
                message=message,
                text=await self._group_wait_text(game),
                reply_markup=self._group_wait_markup(chat_id),
                disable_security=True,
            )

    @loader.command(ru_doc="завершить текущую игру", alias="end")
    async def endgame(self, message):
        """end the current truth or dare game"""
        chat_id = message.chat_id
        if chat_id not in self.games:
            await utils.answer(message, self.strings["no_active_game"])
            return
        del self.games[chat_id]
        await self.inline.form(
            message=message,
            text=self.strings["game_ended"],
            reply_markup=[[{"text": self.strings["btn_close"], "action": "close"}]],
        )

    @loader.command(ru_doc="выбрать интенсивность игры и формат: лёгкий/хот/хард, вживую/удалённо")
    async def tordmode(self, message):
        """choose the game intensity and format: light/hot/hard, in person/remote"""
        await self.inline.form(
            message=message,
            text=self.strings["mode_title"],
            reply_markup=self._mode_main_markup(),
        )

    def _mode_main_markup(self):
        current = self.get("mode", "light")
        realism = self.get("realism", "virtual")
        mode_row = [
            {"text": f"{self.strings[f'mode_{m}']}{' ✅' if m == current else ''}", "callback": self._mode_detail, "args": (m,)}
            for m in self.MODES
        ]
        realism_label = self.strings["realism_real"] if realism == "real" else self.strings["realism_virtual"]
        return [
            mode_row,
            [
                {"text": realism_label, "callback": self._toggle_realism},
                {"text": self.strings["btn_close"], "action": "close"},
            ],
        ]

    async def _mode_detail(self, call, mode):
        await call.edit(
            text=self.strings[f"mode_{mode}_desc"],
            reply_markup=[
                [
                    {"text": self.strings["btn_back"], "callback": self._mode_back},
                    {"text": self.strings["btn_select"], "callback": self._mode_select, "args": (mode,)},
                ]
            ],
        )

    async def _mode_select(self, call, mode):
        self.set("mode", mode)
        await call.edit(text=self.strings["mode_title"], reply_markup=self._mode_main_markup())

    async def _mode_back(self, call):
        await call.edit(text=self.strings["mode_title"], reply_markup=self._mode_main_markup())

    async def _toggle_realism(self, call):
        current = self.get("realism", "virtual")
        self.set("realism", "virtual" if current == "real" else "real")
        await call.edit(text=self.strings["mode_title"], reply_markup=self._mode_main_markup())

    async def _join(self, call, chat_id):
        game = self.games.get(chat_id)
        if not game:
            await call.answer(self.strings["no_active_game"])
            return
        async with game["lock"]:
            if game["started"]:
                await call.answer(self.strings["game_started"])
                return
            uid = call.from_user.id
            if game["is_private"] and uid == game["owner_id"]:
                await call.answer(self.strings["error_play_yourself"])
                return
            if uid in game["pending"]:
                await call.answer(self.strings["already_joined"])
                return
            game["pending"].append(uid)
            if game["is_private"]:
                await self._begin(call, game)
            else:
                await call.edit(text=await self._group_wait_text(game), reply_markup=self._group_wait_markup(chat_id))

    async def _lobby_leave(self, call, chat_id):
        game = self.games.get(chat_id)
        if not game:
            await call.answer(self.strings["no_active_game"])
            return
        async with game["lock"]:
            if game["started"]:
                await call.answer(self.strings["game_started"])
                return
            uid = call.from_user.id
            if uid not in game["pending"]:
                await call.answer(self.strings["not_in_lobby"])
                return
            game["pending"].remove(uid)
            if not game["pending"]:
                del self.games[chat_id]
                await self._send_new(call, game, self.strings["lobby_closed"], [[{"text": self.strings["btn_close"], "action": "close"}]])
                return
            await call.edit(text=await self._group_wait_text(game), reply_markup=self._group_wait_markup(chat_id))

    async def _begin_click(self, call, chat_id):
        game = self.games.get(chat_id)
        if not game:
            await call.answer(self.strings["no_active_game"])
            return
        async with game["lock"]:
            if game["started"]:
                await call.answer(self.strings["game_started"])
                return
            if call.from_user.id != game["owner_id"]:
                await call.answer(self.strings["not_owner"])
                return
            if len(game["pending"]) < 2:
                await call.answer(self.strings["error_play_yourself"])
                return
            await self._begin(call, game)

    async def _begin(self, call, game):
        game["players"] = game["pending"][:]
        random.shuffle(game["players"])
        game["started"] = True
        game["idx"] = 0
        game["type"] = None
        game["type_was_random"] = False
        game["punishment"] = False
        game["punishment_by"] = None
        game["question"] = None
        game["used"] = {}
        game["truth_lock"] = {}
        await self._send_new(call, game, await self._turn_text(game), self._turn_markup(game["chat_id"], game))

    async def _choose(self, call, chat_id, choice):
        game = self.games.get(chat_id)
        if not game:
            await call.answer(self.strings["no_active_game"])
            return
        async with game["lock"]:
            if call.from_user.id != game["players"][game["idx"]]:
                await call.answer(self.strings["not_your_turn"])
                return
            if choice != "truth" and game.get("truth_lock", {}).get(call.from_user.id, 0) > 0:
                await call.answer(self.strings["truth_locked"])
                return
            game["type"] = random.choice(["truth", "dare"]) if choice == "random" else choice
            game["type_was_random"] = choice == "random"
            game["question"] = None
            game["punishment"] = False
            game["punishment_by"] = None
            await self._send_new(call, game, await self._asking_text(game), self._asking_markup(chat_id, game))

    async def _take_question(self, call, chat_id):
        game = self.games.get(chat_id)
        if not game:
            await call.answer(self.strings["no_active_game"])
            return
        async with game["lock"]:
            if call.from_user.id not in (game["players"][game["idx"]], self._asker_id(game)):
                await call.answer(self.strings["no_permission"])
                return
            pool_key = f"{game['mode']}_{game['type']}" + ("_punish" if game.get("punishment") else "")
            game["question"] = await self._draw(game, pool_key)
            await self._send_new(call, game, await self._asking_text(game), self._asking_markup(chat_id, game))

    async def _answered(self, call, chat_id):
        game = self.games.get(chat_id)
        if not game:
            await call.answer(self.strings["no_active_game"])
            return
        async with game["lock"]:
            active = game["players"][game["idx"]]
            if call.from_user.id not in (active, self._asker_id(game)):
                await call.answer(self.strings["no_permission"])
                return
            if game.get("truth_lock", {}).get(active, 0) > 0:
                game["truth_lock"][active] -= 1
            game["idx"] = (game["idx"] + 1) % len(game["players"])
            game["type"] = None
            game["type_was_random"] = False
            game["punishment"] = False
            game["punishment_by"] = None
            game["question"] = None
            await self._send_new(call, game, await self._turn_text(game), self._turn_markup(chat_id, game))

    async def _failed(self, call, chat_id):
        game = self.games.get(chat_id)
        if not game:
            await call.answer(self.strings["no_active_game"])
            return
        async with game["lock"]:
            active = game["players"][game["idx"]]
            clicker = call.from_user.id
            if clicker not in (active, self._asker_id(game)):
                await call.answer(self.strings["no_permission"])
                return
            # Remember who initiated the punishment screen — only they can press Back
            game["punishment_by"] = clicker
            await self._send_new(
                call, game, self.strings["punishment_intro"], self._punishment_choice_markup(chat_id)
            )

    async def _punishment_type(self, call, chat_id, ptype):
        game = self.games.get(chat_id)
        if not game:
            await call.answer(self.strings["no_active_game"])
            return
        async with game["lock"]:
            if call.from_user.id != game["players"][game["idx"]]:
                await call.answer(self.strings["no_permission"])
                return
            game["type"] = ptype
            game["type_was_random"] = False
            game["punishment"] = True
            game["question"] = None
            # Keep punishment_by so Back still works only for the initiator if they return
            await self._send_new(call, game, await self._asking_text(game), self._asking_markup(chat_id, game))

    async def _punishment_back(self, call, chat_id):
        game = self.games.get(chat_id)
        if not game:
            await call.answer(self.strings["no_active_game"])
            return
        async with game["lock"]:
            # Strict: ONLY the person who pressed "Couldn't answer" can go back.
            # Owner and the other player are blocked.
            if call.from_user.id != game.get("punishment_by"):
                await call.answer(self.strings["no_permission"])
                return
            game["question"] = None
            game["punishment"] = False
            # Return to the previous asking state (before punishment choice)
            await self._send_new(call, game, await self._asking_text(game), self._asking_markup(chat_id, game))

    async def _leave(self, call, chat_id):
        game = self.games.get(chat_id)
        if not game:
            await call.answer(self.strings["no_active_game"])
            return
        async with game["lock"]:
            active = game["players"][game["idx"]]
            clicker = call.from_user.id
            if clicker not in (active, game["owner_id"]):
                await call.answer(self.strings["no_permission"])
                return
            close_markup = [[{"text": self.strings["btn_close"], "action": "close"}]]
            if clicker != active:
                # Owner force-ends the whole game
                del self.games[chat_id]
                await self._send_new(call, game, self.strings["game_ended"], close_markup)
                return
            # Active player leaves
            left_id = game["players"].pop(game["idx"])
            # Clean up truth_lock for the leaving player
            if "truth_lock" in game and left_id in game["truth_lock"]:
                del game["truth_lock"][left_id]
            if len(game["players"]) < 2:
                del self.games[chat_id]
                await self._send_new(call, game, self.strings["game_ended_few"], close_markup)
                return
            if game["idx"] >= len(game["players"]):
                game["idx"] = 0
            game["type"] = None
            game["type_was_random"] = False
            game["punishment"] = False
            game["punishment_by"] = None
            game["question"] = None
            await self._send_new(call, game, await self._turn_text(game), self._turn_markup(chat_id, game))
