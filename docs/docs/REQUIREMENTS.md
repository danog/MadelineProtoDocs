---
title: Requirements
description: MadelineProto requires the `mbstring`, `xml`, `json`, `fileinfo`, `gmp` extensions to function properly.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Requirements

MadelineProto requires the `mbstring`, `xml`, `json`, `fileinfo`, `gmp` extensions to function properly.

PHP 7.1+ is supported, PHP 8.0+ is recommended.

To install MadelineProto dependencies on `Ubuntu`, `Debian`, `Devuan`, or any other `Debian-based` distro, run the following command in your command line:

```bash
sudo apt-get install python-software-properties software-properties-common
sudo LC_ALL=C.UTF-8 add-apt-repository ppa:ondrej/php
sudo apt-get update
sudo apt-get install php8.0 php8.0-dev php8.0-xml php8.0-zip php8.0-gmp php8.0-cli php8.0-mbstring git -y
```

Next, follow the instructions on [voip.madelineproto.xyz](https://voip.madelineproto.xyz) and [prime.madelineproto.xyz](https://prime.madelineproto.xyz) to install libtgvoip and PrimeModule.

<a href="https://docs.madelineproto.xyz/docs/INSTALLATION.html">Next section</a>