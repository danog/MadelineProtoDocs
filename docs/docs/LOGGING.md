---
title: Logging
description: MadelineProto provides a unified class for logging messages to the logging destination defined in [settings](SETTINGS.html#settingslogger).  
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Logging

MadelineProto provides a unified class for logging messages to the logging destination defined in [settings](SETTINGS.html#settingslogger).  

Use the [settings](SETTINGS.html#settingslogger) to modify the default logging destination and log verbosity:  

## `$settings['logger']` 

Logger settings

### `$settings['logger']['logger']`
Default: `\danog\MadelineProto\Logger::ECHO_LOGGER` if running from CLI, `\danog\MadelineProto\Logger::FILE_LOGGER` if running from browser  
Description: logger mode, available logger modes:

* `\danog\MadelineProto\Logger::DEFAULT_LOGGER` - Log to the default logger destination
* `\danog\MadelineProto\Logger::FILE_LOGGER` - Log to file in `$settings['logger']['logger_param']`
* `\danog\MadelineProto\Logger::ECHO_LOGGER` - Echo logs
* `\danog\MadelineProto\Logger::CALLABLE_LOGGER` - Call callable provided in `$settings['logger']['logger_param']`. logger_param must accept two parameters: array $message, int $level

### `$settings['logger']['param']`
Default: `__DIR__.'/Madeline.log'`  
Description: optional logger parameter, for modes that require it

### `$settings['logger']['logger_level']`
Default: `\danog\MadelineProto\Logger::VERBOSE`  
Description: What logger messages to show

## Example:  
```php
use danog\MadelineProto\Logger;

$settings = [
    'logger' => [
        'logger_level' => Logger::VERBOSE,
        //'logger' => Logger::ECHO_LOGGER // Can be omitted to use default values
    ]
];
$MadelineProto = new \danog\MadelineProto\API('session.madeline', $settings);
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