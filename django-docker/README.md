- 必要なファイル群を作成
  - docker-compose run web django-admin.py startproject mysite .
- コンテナ起動
  - docker-compose up --build
- Djangoアプリケーションの雛形を作成
  - docker-compose run web python manage.py startapp garden
- DBマイグレーション
  - docker-compose run web python manage.py makemigrations garden