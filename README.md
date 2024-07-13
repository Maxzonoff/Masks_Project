             Учебный материал по Python

IT-отдел крупного банка делает новую 
фичу для личного кабинета клиента. 

Это виджет, который показывает несколько 
последних успешных банковских операций клиента.

**1. В файле masks.py функции маскировки номеров 
карты и счета.**

**2. В файл widget.py импортированы функции и 
написана функция для работы с типами 
и номерами карт и счетов.**

**3. В файле processing.py функции сортировки 
по заданному значению и дат.**

 4. Зависимости с настройками
[tool.poetry]
name = "masks-project"
version = "0.1.0"
description = ""
authors = ["MaxZ <maxzonoff@gmail.com>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.12"


[tool.poetry.group.lint.dependencies]
flake8 = "^7.1.0"
black = "^24.4.2"
isort = "^5.13.2"
mypy = "^1.10.1"


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"


[tool.mypy]
disallow_untyped_defs = true
no_implicit_optional = true
warn_return_any = true
check_untyped_defs = true
strict = true
warn_unreachable = true
exclude = 'venv'

[tool.black]
line-length = 119
exclude = '''
(
  /(
      \.eggs
    | \.git
    | \.hg
    | \.mypy_cache
    | \.tox
    | \.venv
    | dist
  )/
  | foo.py
)
'''

[tool.isort]
line_length = 119 

