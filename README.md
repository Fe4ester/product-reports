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
  - сейчас это выводит заглушку, сам отчет будет добавлен дальше

### требования
- python 3.10+
- csv формат входных файлов: `name,brand,price,rating`