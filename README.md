# Speech Classification
Interview grading with text to speech and text classification

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You need to install

```
laravel
composer
```

### Installing

A step by step to get development env running

laravel configuration :

```sh
laravel new speech-classification
composer require predis/predis
php artisan migrate
chmod -fr 777 storage/logs
chmod -fr 777 storage/framework/sessions
chmod -fr 777 storage/framework/views
chmod -fr 777 storage/framework/cache
```

## Running the tests

```sh
./vendor/bin/phpunit
```

## Deployment

System deploy on heroku environment

heroku configuration :

```sh
app_name=dsib
heroku apps:create $app_name
heroku addons:create cleardb:ignite --app $app_name
heroku addons:create heroku-redis:hobby-dev --app $app_name
heroku config:set APP_KEY=$(php artisan --no-ansi key:generate --show) --app $app_name
heroku config:set APP_LOG=errorlog --app $app_name
heroku config:set QUEUE_DRIVER=redis SESSION_DRIVER=redis CACHE_DRIVER=redis --app $app_name
heroku config:set APP_ENV=development APP_DEBUG=true APP_LOG_LEVEL=debug --app $app_name
```

open your heroku app in deploy tab, connect github in deployment method, enable auto deployment

additional laravel configuration in 

```sh
config/database.php
```

add code below in first line

```php
if (getenv('REDIS_URL')) {
    $redis_url = parse_url(getenv('REDIS_URL'));

    putenv('REDIS_HOST='.$redis_url['host']);
    putenv('REDIS_PORT='.$redis_url['port']);
    putenv('REDIS_PASSWORD='.$redis_url['pass']);
}

if (getenv('CLEARDB_DATABASE_URL')) {
    $db_url = parse_url(getenv('CLEARDB_DATABASE_URL'));

    putenv('DB_HOST='.$db_url['host']);
    putenv('DB_PORT='.$db_url['port']);
    putenv('DB_DATABASE='.substr($db_url['path'], 1));
    putenv('DB_USERNAME='.$db_url['user']);
    putenv('DB_PASSWORD='.$db_url['pass']);
}
```

## Built With

* [Laravel 5.5 ](https://laravel.com) - The web framework used
* [Composer](https://getcomposer.org) - Dependency Management
* [ClearDB](http://w2.cleardb.net/) - Database Management System
* [Redis](https://redis.io) - Used to handle queue, session and cache

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

Use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags](https://github.com/richasdy/speech-classification-ui/tags). 

## Authors

* **Donni Richasdy** - *Initial work* - [richasdy](https://github.com/richasdy)

See also the list of [contributors](https://github.com/richasdy/speech-classification-ui/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Kemas Muslim
* Nurul Ikhsan
* Isman Kurniawan
* Jofardo Adlinnas
* Zinedine Zidane Hanjar
* Daniel Gentha Ivan Desantha