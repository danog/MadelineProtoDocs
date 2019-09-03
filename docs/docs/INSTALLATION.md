---
title: Installation
description: There are various ways to install MadelineProto:
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Installation

There are various ways to install MadelineProto:

* [Simple](#simple)
* [Simple (manual)](#simple-manual)
* [Composer from scratch](#composer-from-scratch)
* [Composer from existing project](#composer-from-existing-project)


## Simple

```php
<?php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
require_once 'madeline.php';
```

This code will automatically download, auto-update and include MadelineProto.

If you want, you can set a `MADELINE_BRANCH` constant before including `madeline.php`, that will define which branch of MadelineProto madeline.php should load.  
When the constant is not set, the latest stable release is loaded.  
If the value is an empty string, the `master` branch is loaded.
Otherwise, the selected branch name or tag is loaded.  


## Simple (manual)

Download [madeline.php](https://phar.madelineproto.xyz/madeline.php), put it in the same directory as your script, and then put the following code in your PHP file:
```php
<?php
require_once 'madeline.php';
```

## Composer from scratch

composer.json:
```
{
    "name": "yourname/yourproject",
    "description": "Project description",
    "type": "project",
    "require": {
        "danog/madelineproto": "dev-master",
        "amphp/dns": "dev-master#aa1892bd as 0.9",
        "amphp/socket": "0.10.12 as 1",
        "amphp/websocket": "dev-master#db2da8c5b3ed22eae37da5ffa10ab3ea8de19342 as 1",
        "amphp/websocket-client": "dev-master#aff808025637bd705672338b4904ad03a4dbdc04 as 1"
    },
    "repositories": [
        {
            "type": "git",
            "url": "https://github.com/danog/phpseclib"
        }
    ],
    "minimum-stability": "dev",
    "license": "AGPL-3.0-only",
    "authors": [
        {
            "name": "Daniil Gentili",
            "email": "daniil.gentili.dg@gmail.com"
        }
    ],
    "autoload": {
        "psr-0": {
            "Your\\Project\\": "src/"
        }
    }
}
```

Then run:
```bash
composer update
```

Put the following code in your PHP file:
```php
<?php
require_once 'vendor/autoload.php';
```

## Composer from existing project

Once you have all the requirements installed properly (on dev as well as production), add this to the ```composer.json``` file:

```
"repositories": [
    {
        "type": "git",
        "url": "https://github.com/danog/phpseclib"
    }
],
```

Make sure you also have these set in the composer.json:

```
"minimum-stability": "dev",
```

Then you can require the package by addding the following lines to the require section:

```
"danog/madelineproto":"^4",
"amphp/dns": "dev-master#aa1892bd as 0.9",
"amphp/socket": "0.10.12 as 1",
"amphp/websocket": "dev-master#db2da8c5b3ed22eae37da5ffa10ab3ea8de19342 as 1",
"amphp/websocket-client": "dev-master#aff808025637bd705672338b4904ad03a4dbdc04 as 1"
```

<a href="https://docs.madelineproto.xyz/docs/UPDATES.html">Next section</a>
