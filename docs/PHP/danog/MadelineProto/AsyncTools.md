---
title: "danog\\MadelineProto\\AsyncTools: Async tools."
description: ""
image: "https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png"
parent: "MadelineProto API"

---
# `danog\MadelineProto\AsyncTools`
[Back to index](../../index.html)

> Author: Daniil Gentili <daniil@daniil.it>  
  

Async tools.  




## Constants
* `danog\MadelineProto\AsyncTools::ALL_MIMES`: 


## Method list:
* [`rethrow(\Throwable $e): void`](#rethrowthrowable-e-void)
* [`flock(string $file, int $operation, float $polling, ?\Amp\Cancellation $token, ?\Closure $failureCb): mixed`](#flockstring-file-int-operation-float-polling-ampcancellation-token-closure-failurecb-mixed)
* [`sleep(float $time): void`](#sleepfloat-time-void)
* [`readLine(string $prompt): string`](#readlinestring-prompt-string)
* [`echo(string $string): void`](#echostring-string-void)
* [`mbStrlen(string $text): int`](#mbstrlenstring-text-int)
* [`mbSubstr(string $text, int $offset, null|int $length): string`](#mbsubstrstring-text-int-offset-nullint-length-string)
* [`mbStrSplit(string $text, int $length): string[]`](#mbstrsplitstring-text-int-length-string)
* [`toCamelCase(string $input): string`](#tocamelcasestring-input-string)
* [`toSnakeCase(string $input): string`](#tosnakecasestring-input-string)
* [`markdownEscape(string $hwat): string`](#markdownescapestring-hwat-string)
* [`typeEscape(string $type): string`](#typeescapestring-type-string)
* [`methodEscape(string $method): string`](#methodescapestring-method-string)
* [`getMimeFromExtension(string $extension, string $default): string`](#getmimefromextensionstring-extension-string-default-string)
* [`getExtensionFromMime(string $mime): string`](#getextensionfrommimestring-mime-string)
* [`getExtensionFromLocation(mixed $location, string $default): string`](#getextensionfromlocationmixed-location-string-default-string)
* [`getMimeFromFile(string $file): string`](#getmimefromfilestring-file-string)
* [`getMimeFromBuffer(string $buffer): string`](#getmimefrombufferstring-buffer-string)

## Methods:
### `rethrow(\Throwable $e): void`

Rethrow exception into event loop.


Parameters:

* `$e`: `\Throwable`   


#### See also: 
* `\Throwable`




### `flock(string $file, int $operation, float $polling, ?\Amp\Cancellation $token, ?\Closure $failureCb): mixed`

Asynchronously lock a file
Resolves with a callbable that MUST eventually be called in order to release the lock.


Parameters:

* `$file`: `string` File to lock  
* `$operation`: `int` Locking mode  
* `$polling`: `float` Polling interval  
* `$token`: `?\Amp\Cancellation` Cancellation token  
* `$failureCb`: `?\Closure` Failure callback, called only once if the first locking attempt fails.  


#### See also: 
* `\Amp\Cancellation`
* `\Closure`




### `sleep(float $time): void`

Asynchronously sleep.


Parameters:

* `$time`: `float` Number of seconds to sleep for  



### `readLine(string $prompt): string`

Asynchronously read line.


Parameters:

* `$prompt`: `string` Prompt  



### `echo(string $string): void`

Asynchronously write to stdout/browser.


Parameters:

* `$string`: `string` Message to echo  



### `mbStrlen(string $text): int`

Get Telegram UTF-8 length of string.


Parameters:

* `$text`: `string` Text  



### `mbSubstr(string $text, int $offset, null|int $length): string`

Telegram UTF-8 multibyte substring.


Parameters:

* `$text`: `string` Text to substring  
* `$offset`: `int` Offset  
* `$length`: `null|int` Length  



### `mbStrSplit(string $text, int $length): string[]`

Telegram UTF-8 multibyte split.


Parameters:

* `$text`: `string` Text  
* `$length`: `int` Length  



### `toCamelCase(string $input): string`

Convert to camelCase.


Parameters:

* `$input`: `string` String  



### `toSnakeCase(string $input): string`

Convert to snake_case.


Parameters:

* `$input`: `string` String  



### `markdownEscape(string $hwat): string`

Escape string for markdown.


Parameters:

* `$hwat`: `string` String to escape  



### `typeEscape(string $type): string`

Escape type name.


Parameters:

* `$type`: `string` String to escape  



### `methodEscape(string $method): string`

Escape method name.


Parameters:

* `$method`: `string` Method name  



### `getMimeFromExtension(string $extension, string $default): string`

Get mime type from file extension.


Parameters:

* `$extension`: `string` File extension  
* `$default`: `string` Default mime type  



### `getExtensionFromMime(string $mime): string`

Get extension from mime type.


Parameters:

* `$mime`: `string` MIME type  



### `getExtensionFromLocation(mixed $location, string $default): string`

Get extension from file location.


Parameters:

* `$location`: `mixed` File location  
* `$default`: `string` Default extension  



### `getMimeFromFile(string $file): string`

Get mime type of file.


Parameters:

* `$file`: `string` File  



### `getMimeFromBuffer(string $buffer): string`

Get mime type from buffer.


Parameters:

* `$buffer`: `string` Buffer  



---
Generated by [danog/phpdoc](https://phpdoc.daniil.it)
