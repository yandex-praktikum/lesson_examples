# Примеры спринта 21

Python 3.14. Установите зависимости: `python -m pip install -r requirements.txt`.

`work_with_db.py` создаёт SQLite-базу с тремя записями для разбора CRUD.
`parser_with_authorization.py` читает готовый локальный блог (он должен быть запущен).
`dynamic_parsing.py` получает динамический HTML httpbin.org; нужен установленный Chrome или Chromium. Если браузер
установлен в нестандартном месте, передайте его путь через `PARSING_BROWSER_PATH`.

Файлы можно добавить в учебный `training_parsing_yap` из спринта 20. `browser_session.py` — готовая настройка
requests-html для Python 3.14 и установленного браузера.
