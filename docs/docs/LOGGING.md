---
title: "Logging"
description: "MadelineProto provides a unified class for logging messages to the logging destination defined in settings.  "
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Logging

MadelineProto provides a unified class for logging messages to the logging destination defined in [settings](SETTINGS.html).  

Use the [settings class](../PHP/danog/MadelineProto/Settings/Logger.md) to modify the default logging destination and log verbosity:  

## Example:  
```php
use danog\MadelineProto\Logger;
use danog\MadelineProto\Settings\Logger as LoggerSettings;

$settings = (new LoggerSettings)
    ->setType(Logger::FILE_LOGGER)
    ->setExtra('custom.log')
    ->setMaxSize(50*1024*1024);
$MadelineProto->updateSettings($settings);
```

Note: when running from web, MadelineProto will also automatically enable logging of **PHP errors** (not MadelineProto logs) to `MadelineProto.log`, located in the same directory as the script that loaded MadelineProto.  

## Usage:

```php
$MadelineProto->logger($message, $level);
```

`$message` is a string, an integer, an array, or any json-encodable object.  
`$level` (optional) is one of the following constants:
* `\danog\MadelineProto\Logger::FATAL_ERROR` - Indicates a fatal error
* `\danog\MadelineProto\Logger::ERROR` - Indicates a recoverable error
* `\danog\MadelineProto\Logger::NOTICE` - Indicates an info message
* `\danog\MadelineProto\Logger::VERBOSE` - Indicates a verbose info message
* `\danog\MadelineProto\Logger::ULTRA_VERBOSE` - Indicates an ultra verbose


By default, `$level` is `\danog\MadelineProto\Logger::NOTICE`.


## Error reporting

MadelineProto now can report errors automatically to the bot admin.  
Simply use the following method:

```php
// $message = (string) $exception, for example
$MadelineProto->report($message);
```

This will automatically report the error (and send the logfile!) to the bot admin, set using the `setReportPeers` method:

```php
$MadelineProto->setReportPeers(['danogentili']);
```

**OR** using the `getReportPeers` method of [the event handler](https://docs.madelineproto.xyz/docs/UPDATES.html#async-event-driven).  

```php

    /**
     * Get peer(s) where to report errors
     *
     * @return int|string|array
     */
    public function getReportPeers()
    {
        return [self::ADMIN];
    }
```

If you use the [`startAndLoop`](https://docs.madelineproto.xyz/docs/UPDATES.html#async-event-driven) method to start update handling, all errors surfacing from the loop will be reported automatically.  

<a href="https://docs.madelineproto.xyz/docs/CALLS.html">Next section</a>