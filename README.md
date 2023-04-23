# kaspersky_test

Неопходимо склонировать репозиторий и перейти в папку kaspersky_test
В качестве процесса была взята пользовательская функция, которая выводит число Пи по 6 символов каждую секунду

## Сборка

```shell
docker build -t kaspersky_image
```

## Запуск

```shell
docker run -d --name kaspersky_container -p 8000:80 kaspersky_image
```

## Остановка

```shell
docker stop kaspersky_container
```

## Удаление

```shell
docker rm kaspersky_container
```

## Использовать

```shell
http://127.0.0.1:8000/docs
```