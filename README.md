# university-files

### Зависимости
- docker 18.06.3-ce
- docker-compose 1.21.0


### Запуск приложения
```
cp conf/env-example conf/.env
cp devops/env-compose devops/.env
cd devops && docker-compose -p university-files up
```
