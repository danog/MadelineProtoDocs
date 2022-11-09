---
title: "Requirements"
description: "MadelineProto requires the mbstring, xml, json, fileinfo, gmp, ffi, openssl extensions to function properly."
nav_order: 7
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Requirements

MadelineProto requires the `mbstring`, `xml`, `json`, `fileinfo`, `gmp`, `ffi`, `openssl` extensions to function properly.

The `ev` and `event` extensions are highly recommended to improve performance.

PHP 7.1+ is supported, PHP 8.1+ is recommended.

**Please note that the next version of MadelineProto (December 2022) will only support PHP 8.1+**.

MadelineProto explicitly supports Linux and UNIX systems (including Mac OS).  
MadelineProto generally works on Windows, though there might be some random issues caused by AV engines, so I personally recommend using Linux.  

To install MadelineProto dependencies on `Ubuntu`, `Debian`, `Devuan`, or any other `Debian-based` distro, run the following command in your command line:

```bash
sudo apt-get install python-software-properties software-properties-common
sudo LC_ALL=C.UTF-8 add-apt-repository ppa:ondrej/php
sudo apt-get update
sudo apt-get install php8.1 php8.1-dev php8.1-xml php8.1-zip php8.1-gmp php8.1-cli php8.1-mbstring php8.1-ffi php8.1-ev git -y
```

The `ev` and `event` extensions can be installed via PECL.

Next, follow the instructions on [prime.madelineproto.xyz](https://prime.madelineproto.xyz) to install PrimeModule.

<a href="https://docs.madelineproto.xyz/docs/INSTALLATION.html">Next section</a>
