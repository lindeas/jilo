requirements

- web server (deb: apache | nginx)

- php support in the web server (deb: php-fpm | libapache2-mod-php)

- pdo and pdo_sqlite support in php (deb: php-db, php-sqlite3) uncomment in php.ini: ;extension=pdo_sqlite

TODO

- jilo-web.db outside web root

- jilo-web.db writable by web server user
