# Кожевников Арсений АТ-08
## Задание по работе с SQLite в Python

### 1. Для начала при помощи SQLiteStudio убедимся в том, что созданная база данных пуста и готова работе (отсутствуют таблицы)
![](https://github.com/flexiG17/homework12_SQL/blob/main/screenshots/1.PNG?raw=true)

### 2. Далее подключаем базу данных к проекту и при помощи библиотеки pandas считываем таблицу works.csv с предыдщух занятий. Используя метод .head() просматриваем первые 10 записей дабы убедиться, что таблица перенесена корректно.
![](https://github.com/flexiG17/homework12_SQL/blob/main/screenshots/2.PNG?raw=true)

### 3. Очищаем столбцы skills и otherInfo от ненужной HTML разметки, используя apply (применяет созданную функцию/метод к выбранным столбцам)
![](https://github.com/flexiG17/homework12_SQL/blob/main/screenshots/4.PNG?raw=true)
#### В результате получаем очищенные записи в данных столбцах:
![](https://github.com/flexiG17/homework12_SQL/blob/main/screenshots/11.PNG?raw=true)


### 4. Создаем sql запросы для создания таблиц, связей, внешних ключей, работы с данными 
![](https://github.com/flexiG17/homework12_SQL/blob/main/screenshots/3.PNG?raw=true)
#### (все пояснения к запросам в коммитах, чтобы не засорять readme)

### 5. В результате работы файла create_database имеем структуру базы данных, включающую в себя конвертированную из csv таблицу works, таблицы education и genders
![](https://github.com/flexiG17/homework12_SQL/blob/main/screenshots/5.PNG?raw=true)

### 6. Таблица works в базе данных database.sqlite имеет следующую структуру и набор данных
![](https://github.com/flexiG17/homework12_SQL/blob/main/screenshots/6.PNG?raw=true)
![](https://github.com/flexiG17/homework12_SQL/blob/main/screenshots/7.PNG?raw=true)

### 7. Таблица genders имеет следующие столбцы с полученными из works['gender'] гендерами, с присвоением им индексов, выставлен первичный ключ полю id.
![](https://github.com/flexiG17/homework12_SQL/blob/main/screenshots/8.PNG?raw=true)

### 8. Таблица education включает в себя два поля id (первычный ключ) и level_of_education, куда входят все уникальные уровни обучения из works.csv с присвоением им индексов 
![](https://github.com/flexiG17/homework12_SQL/blob/main/screenshots/9.PNG?raw=true)
![](https://github.com/flexiG17/homework12_SQL/blob/main/screenshots/10.PNG?raw=true)


