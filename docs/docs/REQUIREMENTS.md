---
title: "Requirements"
description: "MadelineProto requires the mbstring, xml, json, fileinfo, gmp, ffi, openssl extensions to function properly."
nav_order: 7
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Requirements

MadelineProto requires the `mbstring`, `xml`, `json`, `fileinfo`, `gmp`, `ffi`, `openssl` extensions to function properly.

The `ev` and `event` extensions are highly recommended to improve performance.

**PHP 8.1+ is required**.

MadelineProto explicitly supports Linux and UNIX systems (including Mac OS).  
I **don't recommend using Windows**: MadelineProto generally works on Windows, though there might be some random issues caused by AV engines, so I personally recommend using Linux.  

Running on webservers and webhosts is fully supported, but I highly recommend running long-running applications like [event handler bots](https://docs.madelineproto.xyz/docs/UPDATES.html) via CLI.  

Running via docker is highly recommended, see [here &raquo;] for more info on how to run MadelineProto in docker, on any Linux distro.  

Otherwise, see [here &raquo;]() for more info on how to install MadelineProto dependencies on Ubuntu.  

## Docker (recommended)

MadelineProto offers an official MadelineProto docker image for the `linux/amd64`, `linux/arm64` and `linux/riscv64` platforms.  

To get started, install `docker` and `docker-compose`:

Ubuntu:

```bash
sudo apt-get update
sudo apt-get install docker.io docker-compose -y
```

Then increase the `max_map_count` sysctl configuration to avoid "Fiber stack allocate failed" and "Fiber stack protect failed" errors, since the PHP engine mmaps two memory regions per fiber.  

```bash
echo 262144 | sudo tee /proc/sys/vm/max_map_count
echo vm.max_map_count=262144 | sudo tee /etc/sysctl.d/40-madelineproto.conf
```

Then, create the following `docker-compose.yml` file:

```yml
version: "3.7"

services:
  bot:
    image: hub.madelineproto.xyz/danog/madelineproto
    restart: unless-stopped
    tty: true
    volumes:
      - .:/app
    command: php /app/bot.php
```

Then, create a `bot.php` file with your code, and run this command to log into the bot:

```bash
docker run --rm -it --init -v $PWD:/app hub.madelineproto.xyz/danog/madelineproto php /app/bot.php
```

After logging in, press ctrl-c to close the temporary container.

Finally, simply run this command to start the bot in the background.

```bash
docker-compose up --pull always -d
```

Use `docker-compose logs` to view MadelineProto logs and `docker-compose ps` to view the status of your bot.  

## Ubuntu

To install MadelineProto dependencies on Ubuntu, run the following command in your command line:

```bash
sudo apt-get update
sudo apt-get install software-properties-common -y
sudo LC_ALL=C.UTF-8 add-apt-repository -y ppa:ondrej/php
sudo apt-get update
sudo apt-get install php8.2 php8.2-dev php8.2-xml php8.2-zip php8.2-gmp php8.2-cli php8.2-mbstring php8.2-ffi php-pear libevent-dev -y
sudo pecl install event ev

echo 262144 | sudo tee /proc/sys/vm/max_map_count
echo vm.max_map_count=262144 | sudo tee /etc/sysctl.d/40-madelineproto.conf

```

Next, add `extension=event.so` and `extension=ev.so` to php.ini.  

Finally, follow the instructions on [prime.madelineproto.xyz](https://prime.madelineproto.xyz) to install PrimeModule.

The `max_map_count` sysctl configuration is required to avoid "Fiber stack allocate failed" and "Fiber stack protect failed" errors, since the PHP engine mmaps two memory regions per fiber.  

<a href="https://docs.madelineproto.xyz/docs/INSTALLATION.html">Next section</a>
