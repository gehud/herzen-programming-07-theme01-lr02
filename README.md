# Гроздов Николай Алексеевич

## Получить данные о погоде для Москвы
```
curl "http://localhost:5000/weather/current?city=Moscow&units=metric&user_id=user123"
```

## Получить рекомендации (используя данные о погоде из предыдущего вызова)
```
curl -X POST -H "Content-Type: application/json" -d '{"weather":[{"main":"Rain"}],"main":{"temp":12}}' http://localhost:5000/recommendations/get
```

## Получить историю пользователя
```
curl "http://localhost:5000/history/user/user123"
```

## Получить статистику
```
curl "http://localhost:5000/history/statistics?limit=3"
```
