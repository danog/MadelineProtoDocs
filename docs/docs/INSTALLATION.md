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
```json
{
    "name": "yourname/yourproject",
    "description": "Project description",
    "type": "project",
    "require": {
        "danog/madelineproto": "^6"
    },
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

Simply require the package:  

```bash
composer require danog/madelineproto
```

<a href="https://docs.madelineproto.xyz/docs/UPDATES.html">Next section</a>