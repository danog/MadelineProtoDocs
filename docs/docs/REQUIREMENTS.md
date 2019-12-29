---
title: Requirements
description: MadelineProto requires the `mbstring`, `xml`, `json`, `fileinfo`, `gmp` extensions to function properly.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Requirements

MadelineProto requires the `mbstring`, `xml`, `json`, `fileinfo`, `gmp` extensions to function properly.

To install MadelineProto dependencies on `Ubuntu`, `Debian`, `Devuan`, or any other `Debian-based` distro, run the following command in your command line:

```bash
sudo apt-get install python-software-properties software-properties-common
sudo LC_ALL=C.UTF-8 add-apt-repository ppa:ondrej/php
sudo apt-get update
sudo apt-get install php7.4 php7.4-dev php7.4-fpm php7.4-xml php7.4-zip php7.4-gmp php7.4-cli php7.4-mbstring php7.4-json git -y
```

Next, follow the instructions on [voip.madelineproto.xyz](https://voip.madelineproto.xyz) and [prime.madelineproto.xyz](https://prime.madelineproto.xyz) to install libtgvoip and PrimeModule.

<a href="https://docs.madelineproto.xyz/docs/INSTALLATION.html">Next section</a>
