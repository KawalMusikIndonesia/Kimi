#Web Server

Untuk di `/var/www/kimi/` kita masukkan file berikut:

`kimisubmit.php`

## Install RabbitMQ
Kemudian, kita install Rabbit MQ dengan cara:

`sudo apt-get install rabbitmq-server`

Cek status:

`sudo rabbitmqctl status`

## Install Composer
Untuk install dependencies RabbitMQ
```
php -r "readfile('https://getcomposer.org/installer');" > composer-setup.php
php -r "if (hash('SHA384', file_get_contents('composer-setup.php')) === '41e71d86b40f28e771d4bb662b997f79625196afcca95a5abf44391188c695c6c1456e16154c75a211d238cc3bc5cb47') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); }"
php composer-setup.php
php -r "unlink('composer-setup.php');"
```
di directory `/var/www/kimi/` buat file `composer.json`:
```
$ touch composer.json
$ nano composer.json
```
Dan isi dengan ini:
```
{
    "require": {
        "php-amqplib/php-amqplib": "2.5.*"
    }
}
```
Kemudian jalankan:
`$ php composer.phar install`
