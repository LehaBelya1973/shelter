**Работа с ORM в Django**

+ Создать новое приложение "собаки"
+ Описать модель "Собаки" с полями: кличка собаки, порода, фото, дата рождения
+ Добавить модель "Порода" с полями: название, описание
+ В модели "Собака" заменить поле "порода" на модель "Порода"
+ В админку вынести список пород, а также список собак
+ У списка собак добавить фильтрацию по породам
+ Сформировать фикстуры для наполнения базы пород и собак 

**Шаблонизация**

+ Подключить Bootstrap к проекту
+ Сделать главную страницу с тремя породами из базы
+ Полный список пород вывести на отдельную страницу
+ Для каждой породы реализовать возможность перехода к списку собак, которые относятся к выбранной породе
+ Каждая кличка должна быть выведена начиная с заглавной буквы, например "Маленькая Леди"
+ Выделить общий базовый шаблон
+ Вынести в подшаблоны с карточками пород и подключить их на главной странице и на странице со списком пород
- Добавить шаблонный фильтр, который убирает необходимость выводить картинку с припиской '/media/' в начале пути
