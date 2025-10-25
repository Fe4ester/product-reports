## product-reports

микроутилита для генерации отчетов по брендам из csv  
используются только stdlib и `tabulate` для вывода

### установка и запуск

- установить зависимости
    - `poetry install`
- помощь
    - `poetry run brand-report -h`
- пример запуска
    - `poetry run brand-report --files examples/a.csv examples/b.csv --report average-rating`

### формат входных данных

- csv колонки: `name,brand,price,rating`
- пример:
    - `name,brand,price,rating`
    - `iphone 15 pro,apple,999,4.9`
    - `galaxy s23 ultra,samsung,1199,4.8`
    - `redmi note 12,xiaomi,199,4.6`

### требования

- python 3.10+
- csv формат входных файлов: `name,brand,price,rating`