---
title: "Installation"
description: "There are various ways to install MadelineProto:"
nav_order: 9
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Installation

There are various ways to install MadelineProto:

* [Simple](#simple)
* [Composer from existing project](#composer-from-existing-project)
* [Composer from scratch](#composer-from-scratch)


## Simple

```php
<?php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
require_once 'madeline.php';
```

This code will automatically download, auto-update and include MadelineProto.

**Warning**: NEVER use this install method in production.  
The `madeline.php` install script is as an alpha/beta-level distribution channel for MadelineProto with frequent breaking changes distributed with automatic updates.  
If you require a stable, semantically versioned install of MadelineProto with no automatic updates, [please install MadelineProto using composer &raquo;](#composer-from-existing-project).

For this reason, `madeline.php` is not compatible with pre-existing composer installs, [please install MadelineProto using composer](#composer-from-existing-project) if you already have a composer project.  

## Phar file

Head over to the [GitHub releases section](https://github.com/danog/MadelineProto/releases) and download the `madeline81.phar` from the latest release, and include it in your project:

```php
require_once 'madeline81.phar';
```

**Warning:** `madeline81.phar` is not compatible with pre-existing composer installs, [please install MadelineProto using composer](#composer-from-existing-project) if you already have a composer project.  

## Composer from existing project

Simply require the package (composer v2+ is required):  

```bash
composer config minimum-stability beta
composer require "danog/madelineproto:^8"
```

### Composer from scratch

composer.json:
```json
{
    "name": "yourname/yourproject",
    "description": "Project description",
    "type": "project",
    "minimum-stability": "beta",
    "require": {
        "danog/madelineproto": "^8"
    },
    "license": "AGPL-3.0-only",
    "authors": [
        {
            "name": "Daniil Gentili",
            "email": "daniil@daniil.it"
        }
    ],
    "autoload": {
        "psr-0": {
            "Your\\Project\\": "src/"
        }
    }
}
```

Then run (composer v2+ is required):
```bash
composer update
```

Put the following code in your PHP file:
```php
<?php
require_once 'vendor/autoload.php';
```

<a href="https://docs.madelineproto.xyz/docs/BROADCAST.html">Next section</a>