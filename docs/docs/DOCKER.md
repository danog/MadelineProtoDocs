---
title: "MadelineProto on Docker"
description: "MadelineProto offers an official MadelineProto docker image for the linux/amd64, linux/arm64 and linux/riscv64 platforms @ hub.madelineproto.xyz/danog/madelineproto.  "
nav_order: 8
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# MadelineProto on Docker

MadelineProto offers an official MadelineProto docker image for the `linux/amd64`, `linux/arm64` and `linux/riscv64` platforms @ `hub.madelineproto.xyz/danog/madelineproto`.  

The image comes with all dependencies pre-configured.  
Both opcache and JIT are enabled by default, for maximum performance.  

To get started, install `docker`:

```bash
curl -fsSL https://get.docker.com | sudo sh
```

Then increase the `max_map_count` sysctl configuration to avoid "Fiber stack allocate failed" and "Fiber stack protect failed" errors, since the PHP engine mmaps two memory regions per fiber.  

```bash
echo 262144 | sudo tee /proc/sys/vm/max_map_count
echo vm.max_map_count=262144 | sudo tee /etc/sysctl.d/40-madelineproto.conf
```

Then, create the following `docker-compose.yml` file:

```yml
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
docker compose up --pull always -d
```

Use `docker compose logs` to view MadelineProto logs and `docker compose ps` to view the status of your bot.  

### Web docker

Running in CLI mode (`command: php /app/bot.php`) is heavily recommended, but if web access is required, the official MadelineProto image can also function as a `php-fpm` server if `command: /usr/local/sbin/php-fpm` is passed, exposing a fastcgi socket on port 9000.  
Note that the image has opcache and JIT enabled by default, so you should restart your container with `docker compose restart` to apply changes to your code.

<a href="https://docs.madelineproto.xyz/docs/INSTALLATION.html">Next section</a>