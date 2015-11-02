Щоб розгорнути локально виконайте:
1. Встановіть python3.4 (якщо ще не встановлено)
2. Встановіть залежності: pip install -r requirements.txt
3. Створіть структуру базу даних: python manage.py migrate - запустити в корені проекту(тільки 1 раз).
4. В settings.py додайте свої CONSUMER_KEY, CONSUMER_SECRET, 
ACCESS_KEY, ACCESS_SECRET
5. Для запуску локального сервера виконати: python manage.py runserver