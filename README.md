             Учебный материал по Python

***IT-отдел крупного банка делает новую
фичу для личного кабинета клиента.***

***Это виджет, который показывает несколько
последних успешных банковских операций клиента.***

**Зависимости:**

pyproject.toml

**Программа:**

1. В файле masks.py функции маскировки номеров
   карты и счета. Создан логер.

2. В файл widget.py импортированы функции и
   написана функция для работы с типами
   и номерами карт и счетов.

3. В файле processing.py функции сортировки
   по заданному значению и дат.

4. В файле generators.py функции фильтрации
   по валюте, описанию и функция генерации номеров карт.

5. В файле decorators.py функции для записи в файл - 
начало и конец работы программы.

6. В файле utils.py функция принимающая путь до файла 
и возвращающая python объект. Создан логер.

7. В файле external_api.py функция, обращается к API для получения курса.




**Тестирование:**

1. Произведено тестирование в test_masks.py для модуля masks.py

2. Произведено тестирование в test_widget.py для модуля widget.py

3. Произведено тестирование в test_processing.py для модуля processing.py.

4. Произведено тестирование в test_generators.py для модуля generators.py

5. Произведено тестирование в test_decorators.py для модуля decorators.py

6. Произведено тестирование в test_utils.py для модуля utils.py

7. Произведено тестирование в test_external_api.py для модуля external_api.py

В файле conftest.py все фикстуры.
В папке data json файлы.
В папке logs логи.
В папке test_files файлы json для тестирования.