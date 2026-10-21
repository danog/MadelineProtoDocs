---
title: "MadelineProto on Docker"
description: "MadelineProto offers an official MadelineProto docker image for the linux/amd64 and linux/arm64 platforms @ hub.madelineproto.xyz/danog/madelineproto."
nav_order: 8
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# MadelineProto on Docker

MadelineProto offers an official MadelineProto docker image for the `linux/amd64` and `linux/arm64` platforms @ `hub.madelineproto.xyz/danog/madelineproto`.  

The image comes with all dependencies pre-configured.  
Both opcache and JIT are enabled by default, for maximum performance.  

* [Tags](#tags)
* [User and permissions](#user-and-permissions)
* [Getting started](#getting-started)
  * [CLI bot (recommended)](#cli-bot-recommended)
  * [Databases on docker](#databases-on-docker)
  * [Web docker](#web-docker)
  * [Custom extensions](#custom-extensions)

## Tags

* `latest` (the default): the image of the latest release of MadelineProto.  
* `8.11.2`, `8.11`, `8`: the image of a specific release, of the latest release of a minor version, of the latest release of a major version.  
* `next`: the image of the latest commit of the main branch, rebuilt on every push (`debian` is an alias).  

The image contains PHP and the extensions used by MadelineProto, not MadelineProto itself: use `madeline.php` or composer to install it, as usual.  

## User and permissions

The image runs as the unprivileged `madeline` user, with UID and GID `1000` (home `/home/madeline`, working directory `/app`), not as root.  

The files and folders mounted into the container (like `./app` below) must be readable and writable by UID `1000` (sessions, `madeline.php` and the phar it downloads are written there).  
On most Linux distributions, the first user already has UID `1000`, and nothing needs to be done; otherwise, change the owner of the folder:  

```bash
sudo chown -R 1000:1000 app
```

Or run the container as your own user, with `user: "1001:1001"` in `docker-compose.yml` (or `--user 1001:1001` for `docker run`), replacing `1001` with the output of `id -u` and `id -g`.  

**Upgrading from an older image**: older images ran as root, so files they created (sessions, `madeline.php`, the phar) belong to root: run `sudo chown -R 1000:1000 app` once, or keep running as root, which is not recommended, with `user: root` in `docker-compose.yml` (or `--user root` for `docker run`).  

## Getting started

To get started, install `docker`:

```bash
curl -fsSL https://get.docker.com | sudo sh
```

Then increase the `max_map_count` sysctl configuration to avoid "Fiber stack allocate failed" and "Fiber stack protect failed" errors, since the PHP engine maps two memory regions per fiber.  

```bash
echo 262144 | sudo tee /proc/sys/vm/max_map_count
echo vm.max_map_count=262144 | sudo tee /etc/sysctl.d/40-madelineproto.conf
```

Then, increase the maximum open FD limit, to allow opening many TCP sockets for improved upload and download performance and avoid errors.  

```php
sudo mkdir -p /etc/security/limits.d/

echo '* soft nofile 1048576' | sudo tee -a /etc/security/limits.d/40-madelineproto.conf
echo '* hard nofile 1048576' | sudo tee -a /etc/security/limits.d/40-madelineproto.conf
```

Finally, follow one or more of the following guides, according to your needs:

### CLI bot (recommended)

Create the following `docker-compose.yml` file, with the following contents:

```yml
services:
  bot:
    image: hub.madelineproto.xyz/danog/madelineproto
    restart: always
    init: true
    #depends_on:
      #- mariadb
      #- postgres
      #- redis
    tty: true
    volumes:
      - ./app:/app
    command: php /app/bot.php
```

Then, create an `app` folder, and an `app/bot.php` file with your code.  

**Mac OS note**: If you encounter issues on Mac OS, make sure to enable ephemeral filesystem support with a database [as described here &raquo;](https://docs.madelineproto.xyz/docs/DATABASE.html#ephemeral-filesystems), and change the session path in `bot.php` to point to a unique path in `/tmp`, not in `/app`.  

Then, run this command to log into the bot:

```bash
docker run --rm -it --init -v $PWD/app:/app hub.madelineproto.xyz/danog/madelineproto php /app/bot.php
```

**After logging in, press ctrl-c to close the temporary container.**

**After logging in for the first time**, you can specify some custom settings to connect to a database, as described [here &raquo;](#databases-on-docker).  

Finally, simply run this command to start the bot in the background.

```bash
docker compose up --pull always -d
```

Use `docker compose logs` to view MadelineProto logs and `docker compose ps` to view the status of your bot.  

Run `docker compose restart bot` to restart the bot.  

### Databases on docker

Specifying additional containers with mariadb, postgres or redis is really easy, just add the following sections to the `docker-compose.yml` file you created in the [previous step](#cli-bot-recommended):

```yml
services:
  # Your bot or php-fpm services created in previous steps

  #mariadb:
  #  image: mariadb:latest
  #  restart: always
  #  environment:
  #    - MARIADB_ROOT_PASSWORD=replace_me_with_a_secure_password
  #  volumes:
  #    - ./mysql:/var/lib/mysql

  #postgres:
  #  image: postgres:latest
  #  restart: always
  #  environment:
  #    POSTGRES_USER: admin
  #    POSTGRES_PASSWORD: replace_me_with_a_secure_password
  #  healthcheck:
  #    test: ["CMD-SHELL", "pg_isready -U $$POSTGRES_USER -d $$POSTGRES_DB"]
  #  volumes:
  #    - ./postgres:/var/lib/postgresql/data
  
  #redis:
  #  image: redis:latest
  #  restart: always
  #  volumes:
  #    - ./redis:/data
  #  command: redis-server --save 60 1 --loglevel warning

```

If you want to use the mysql backend for lower memory usage, uncomment all `mariadb` sections and use [these MadelineProto settings to connect &raquo;](https://docs.madelineproto.xyz/docs/DATABASE.html#mysql-example-low-memory-usage).  

If you want to use the postgres backend for lower memory usage, uncomment all `postgres` sections and use [these MadelineProto settings to connect &raquo;](https://docs.madelineproto.xyz/docs/DATABASE.html#postgres-example-low-memory-usage).  

If you want to use the redis backend, uncomment all `redis` sections and use these [MadelineProto settings to connect](https://docs.madelineproto.xyz/docs/DATABASE.html#redis-example-medium-memory-usage-faster-access).  

**NOTE**: MadelineProto can also be configured to run on ephemeral filesystems (i.e. docker containers with no volumes, storing all data on MySQL/Postgres/Redis) by setting a table prefix manually in the settings, as specified [here &raquo;](https://docs.madelineproto.xyz/docs/DATABASE.html#ephemeral-filesystems).  

### Web docker

Running in [CLI mode](#cli-bot-recommended) is heavily recommended, but if web access is required, the official MadelineProto image can also function as a `php-fpm` server.  
Note that the image has opcache and JIT enabled by default, so you should restart your container with `docker compose restart php-fpm` to apply changes to your code.

Here's an example `docker-compose.yml` file for a caddy+php-fpm combo:

```yml
services:
  php-fpm:
    image: hub.madelineproto.xyz/danog/madelineproto
    restart: always
    init: true
    #depends_on:
      #- mariadb
      #- postgres
      #- redis
    volumes:
      - ./app:/app
    command: php-fpm
  
  caddy:
    image: caddy:alpine
    restart: always
    depends_on:
      - php-fpm
    ports:
      - 80:80/tcp
      - 443:443/tcp
      - 443:443/udp
    volumes:
      - ./app:/app
      - ./Caddyfile:/etc/caddy/Caddyfile
      - ./caddy_data:/data
      - ./caddy_config:/config
```

Create the following `Caddyfile` in the same folder:

```bash
{
  email daniil@daniil.it
}

example.com {
  root * /app
  php_fastcgi php-fpm:9000
  file_server
  log {
    format console
  }
}
```

Caddy will automatically configure a TLS certificate for `example.com`.  

Create an `app` folder, and put your code in that folder.  

Finally, simply run this command to start the webserver in the background.

```bash
docker compose up --pull always -d
```

You can now access your PHP code @ `https://example.com`.  

You can also add containers for mariadb, postgres or redis as [described here &raquo;](#databases-on-docker).  

Use `docker compose logs` to view webserver logs and `docker compose ps` to view the status of your webserver.  

Run `docker compose restart php-fpm` every time you change your code to reload changes.

If you want to test locally without obtaining a certificate for a domain, replace `example.com` with `http://localhost:80` in the Caddyfile.  

### Custom extensions

Optionally, you may also add custom extensions by creating a custom docker image with the following `Dockerfile`, for example to install the `apcu` extension with [PIE](https://github.com/php/pie) (shipped with the image), as root, switching back to the unprivileged user afterwards:

```bash
FROM hub.madelineproto.xyz/danog/madelineproto:latest

USER root

RUN apt-get update && \
    apt-get install -y --no-install-recommends autoconf dpkg-dev file g++ gcc libc-dev make pkg-config re2c && \
    pie install apcu/apcu && \
    apt-get purge -y autoconf dpkg-dev file g++ gcc libc-dev make pkg-config re2c && \
    rm -rf /var/lib/apt/lists/*

USER madeline
```

The image doesn't include `pecl`: use `pie` instead, with any extension [published for PIE on Packagist](https://packagist.org/extensions).  

And use the following `docker-compose.yml` file:

```yml
services:
  bot:
    build:
      context: .
      dockerfile: Dockerfile
    restart: always
    #depends_on:
      #- mariadb
      #- postgres
      #- redis
    tty: true
    volumes:
      - .:/app
    command: php /app/bot.php
```

<a href="https://docs.madelineproto.xyz/docs/METRICS.html">Next section</a>