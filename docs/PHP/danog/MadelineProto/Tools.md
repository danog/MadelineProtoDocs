---
title: "danog\\MadelineProto\\Tools: Some tools."
description: ""
image: "https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png"
parent: "MadelineProto API"

---
# `danog\MadelineProto\Tools`
[Back to index](../../index.html)

> Author: Daniil Gentili <daniil@daniil.it>  
  

Some tools.  




## Constants
* `danog\MadelineProto\Tools::ALL_MIMES`: 


## Method list:
* `genVectorHash(array $ints): \string Vector hash`
* `randomInt(int $modulus)`
* `random(int $length): \string Random string`
* `posmod(int $a, int $b): \int Modulo`
* `unpackSignedInt(string $value): int`
* `unpackSignedLong(string $value): int`
* `unpackSignedLongString(string|int|array $value)`
* `packSignedInt(int $value)`
* `packSignedLong(int $value)`
* `packUnsignedInt(int $value)`
* `packDouble(float $value)`
* `unpackDouble(string $value)`
* `wait(\Generator|\Amp\Promise $promise, bool $ignoreSignal)`
* `all((\Generator|\Amp\Promise)[] $promises)`
* `any((\Amp\Promise|\Generator)[] $promises)`
* `some((\Amp\Promise|\Generator)[] $promises)`
* `first((\Amp\Promise|\Generator)[] $promises)`
* `timeout(\Generator|\Amp\Promise $promise, int $timeout)`
* `timeoutWithDefault(\Amp\Promise|\Generator $promise, int $timeout): \Amp\Promise<\TReturn>|\Amp\Promise<\TReturnAlt>`
* `call(\Generator|\Amp\Promise|mixed $promise)`
* `callFork(\Generator|\Amp\Promise $promise, ?\Generator|\Amp\Promise $actual, string $file): \Amp\Promise|mixed`
* `callForkDefer(\Generator|\Amp\Promise $promise)`
* `rethrow(\Throwable $e, string $file)`
* `after(\Generator|\Amp\Promise $a, \Generator|\Amp\Promise $b)`
* `flock(string $file, int $operation, float $polling, ?\Amp\Promise $token, ?callable $failureCb)`
* `sleep(int|float $time)`
* `readLine(string $prompt): \Amp\Promise<string>`
* `echo(string $string)`
* `isArrayOrAlike(mixed $var): bool`
* `arr(mixed $params)`
* `base64urlDecode(string $data)`
* `base64urlEncode(string $data)`
* `rleDecode(string $string)`
* `rleEncode(string $string)`
* `inflateStripped(string $stripped): \string JPG payload`
* `closeConnection(string $message): void`
* `end(array $what)`
* `isAltervista(): bool`
* `hasVar(object $obj, string $var)`
* `getVar(object $obj, string $var)`
* `setVar(object $obj, string $var, mixed $val)`
* `mbStrlen(string $text): float|int`
* `mbSubstr(string $text, int $offset, ?int $length)`
* `mbStrSplit(string $text, int $length): string[]`
* `toCamelCase(string $input)`
* `toSnakeCase(string $input)`
* `markdownEscape(string $hwat)`
* `typeEscape(string $type)`
* `methodEscape(string $method)`
* `getMimeFromExtension(string $extension, string $default)`
* `getExtensionFromMime(string $mime)`
* `getExtensionFromLocation(mixed $location, string $default)`
* `getMimeFromFile(string $file)`
* `getMimeFromBuffer(string $buffer)`

## Methods:
### `genVectorHash(array $ints): \string Vector hash`

Generate MTProto vector hash.


Parameters:

* `$ints`: `array` IDs  


Return value: Vector hash


### `randomInt(int $modulus)`

Get random integer.


Parameters:

* `$modulus`: `int` Modulus  



### `random(int $length): \string Random string`

Get random string of specified length.


Parameters:

* `$length`: `int` Length  


Return value: Random string


### `posmod(int $a, int $b): \int Modulo`

Positive modulo
Works just like the % (modulus) operator, only returns always a postive number.


Parameters:

* `$a`: `int` A  
* `$b`: `int` B  


Return value: Modulo


### `unpackSignedInt(string $value): int`

Unpack base256 signed int.


Parameters:

* `$value`: `string` base256 int  



### `unpackSignedLong(string $value): int`

Unpack base256 signed long.


Parameters:

* `$value`: `string` base256 long  



### `unpackSignedLongString(string|int|array $value)`

Unpack base256 signed long to string.


Parameters:

* `$value`: `string|int|array` base256 long  



### `packSignedInt(int $value)`

Convert integer to base256 signed int.


Parameters:

* `$value`: `int` Value to convert  



### `packSignedLong(int $value)`

Convert integer to base256 long.


Parameters:

* `$value`: `int` Value to convert  



### `packUnsignedInt(int $value)`

Convert value to unsigned base256 int.


Parameters:

* `$value`: `int` Value  



### `packDouble(float $value)`

Convert double to binary version.


Parameters:

* `$value`: `float` Value to convert  



### `unpackDouble(string $value)`

Unpack binary double.


Parameters:

* `$value`: `string` Value to unpack  



### `wait(\Generator|\Amp\Promise $promise, bool $ignoreSignal)`

Synchronously wait for a promise|generator.


Parameters:

* `$promise`: `\Generator|\Amp\Promise` The promise to wait for  
* `$ignoreSignal`: `bool` Whether to ignore shutdown signals  


#### See also: 
* `\Generator`
* `\Amp\Promise`




### `all((\Generator|\Amp\Promise)[] $promises)`

Returns a promise that succeeds when all promises succeed, and fails if any promise fails.
Returned promise succeeds with an array of values used to succeed each contained promise, with keys corresponding to the array of promises.

Parameters:

* `$promises`: `(\Generator|\Amp\Promise)[]` Promises  


#### See also: 
* `\Generator`
* `\Amp\Promise`




### `any((\Amp\Promise|\Generator)[] $promises)`

Returns a promise that is resolved when all promises are resolved. The returned promise will not fail.


Parameters:

* `$promises`: `(\Amp\Promise|\Generator)[]` Promises  


#### See also: 
* `\Amp\Promise`
* `\Generator`




### `some((\Amp\Promise|\Generator)[] $promises)`

Resolves with a two-item array delineating successful and failed Promise results.
The returned promise will only fail if the given number of required promises fail.

Parameters:

* `$promises`: `(\Amp\Promise|\Generator)[]` Promises  


#### See also: 
* `\Amp\Promise`
* `\Generator`




### `first((\Amp\Promise|\Generator)[] $promises)`

Returns a promise that succeeds when the first promise succeeds, and fails only if all promises fail.


Parameters:

* `$promises`: `(\Amp\Promise|\Generator)[]` Promises  


#### See also: 
* `\Amp\Promise`
* `\Generator`




### `timeout(\Generator|\Amp\Promise $promise, int $timeout)`

Create an artificial timeout for any \Generator or Promise.


Parameters:

* `$promise`: `\Generator|\Amp\Promise`   
* `$timeout`: `int`   


#### See also: 
* `\Generator`
* `\Amp\Promise`




### `timeoutWithDefault(\Amp\Promise|\Generator $promise, int $timeout): \Amp\Promise<\TReturn>|\Amp\Promise<\TReturnAlt>`

Creates an artificial timeout for any `Promise`.
If the promise is resolved before the timeout expires, the result is returned

If the timeout expires before the promise is resolved, a default value is returned

Parameters:

* `$promise`: `\Amp\Promise|\Generator` Promise to which the timeout is applied.  
  Full type:
  ```
  \Amp\Promise<\TReturn>|\TGenerator
  ```
* `$timeout`: `int` Timeout in milliseconds.  


#### See also: 
* `\Amp\Promise`
* `\Generator`
* `\TReturn`
* `\TGenerator`
* `\TReturnAlt`




### `call(\Generator|\Amp\Promise|mixed $promise)`

Convert generator, promise or any other value to a promise.


Parameters:

* `$promise`: `\Generator|\Amp\Promise|mixed`   
  Full type:
  ```
  \Generator<mixed, mixed, mixed, \TReturn>|\Amp\Promise<\TReturn>|\TReturn
  ```


Fully typed return value:
```
\Amp\Promise<\TReturn>
```
#### See also: 
* `\Generator`
* `\Amp\Promise`
* `\TReturn`




### `callFork(\Generator|\Amp\Promise $promise, ?\Generator|\Amp\Promise $actual, string $file): \Amp\Promise|mixed`

Call promise in background.


Parameters:

* `$promise`: `\Generator|\Amp\Promise` Promise to resolve  
* `$actual`: `?\Generator|\Amp\Promise` Promise to resolve instead of $promise  
* `$file`: `string` File  


#### See also: 
* `\Generator`
* `\Amp\Promise`




### `callForkDefer(\Generator|\Amp\Promise $promise)`

Call promise in background, deferring execution.


Parameters:

* `$promise`: `\Generator|\Amp\Promise` Promise to resolve  


#### See also: 
* `\Generator`
* `\Amp\Promise`




### `rethrow(\Throwable $e, string $file)`

Rethrow error catched in strand.


Parameters:

* `$e`: `\Throwable` Exception  
* `$file`: `string` File where the strand started  


#### See also: 
* `\Throwable`




### `after(\Generator|\Amp\Promise $a, \Generator|\Amp\Promise $b)`

Call promise $b after promise $a.


Parameters:

* `$a`: `\Generator|\Amp\Promise` Promise A  
* `$b`: `\Generator|\Amp\Promise` Promise B  


#### See also: 
* `\Generator`
* `\Amp\Promise`




### `flock(string $file, int $operation, float $polling, ?\Amp\Promise $token, ?callable $failureCb)`

Asynchronously lock a file
Resolves with a callbable that MUST eventually be called in order to release the lock.


Parameters:

* `$file`: `string` File to lock  
* `$operation`: `int` Locking mode  
* `$polling`: `float` Polling interval  
* `$token`: `?\Amp\Promise` Cancellation token  
* `$failureCb`: `?callable` Failure callback, called only once if the first locking attempt fails.  


#### See also: 
* `\Amp\Promise`




### `sleep(int|float $time)`

Asynchronously sleep.


Parameters:

* `$time`: `int|float` Number of seconds to sleep for  



### `readLine(string $prompt): \Amp\Promise<string>`

Asynchronously read line.


Parameters:

* `$prompt`: `string` Prompt  


#### See also: 
* `\Amp\Promise`




### `echo(string $string)`

Asynchronously write to stdout/browser.


Parameters:

* `$string`: `string` Message to echo  



### `isArrayOrAlike(mixed $var): bool`

Check if is array or similar (traversable && countable && arrayAccess).


Parameters:

* `$var`: `mixed` Value to check  



### `arr(mixed $params)`

Create array.


Parameters:

* `$params`: `mixed` Params  



### `base64urlDecode(string $data)`

base64URL decode.


Parameters:

* `$data`: `string` Data to decode  



### `base64urlEncode(string $data)`

Base64URL encode.


Parameters:

* `$data`: `string` Data to encode  



### `rleDecode(string $string)`

null-byte RLE decode.


Parameters:

* `$string`: `string` Data to decode  



### `rleEncode(string $string)`

null-byte RLE encode.


Parameters:

* `$string`: `string` Data to encode  



### `inflateStripped(string $stripped): \string JPG payload`

Inflate stripped photosize to full JPG payload.


Parameters:

* `$stripped`: `string` Stripped photosize  


Return value: JPG payload


### `closeConnection(string $message): void`

Close connection with client, connected via web.


Parameters:

* `$message`: `string` Message  



### `end(array $what)`

Get final element of array.


Parameters:

* `$what`: `array` Array  



### `isAltervista(): bool`

Whether this is altervista.



### `hasVar(object $obj, string $var)`

Checks private property exists in an object.


Parameters:

* `$obj`: `object` Object  
* `$var`: `string` Attribute name  



### `getVar(object $obj, string $var)`

Accesses a private variable from an object.


Parameters:

* `$obj`: `object` Object  
* `$var`: `string` Attribute name  



### `setVar(object $obj, string $var, mixed $val)`

Sets a private variable in an object.


Parameters:

* `$obj`: `object` Object  
* `$var`: `string` Attribute name  
* `$val`: `mixed` Attribute value  



### `mbStrlen(string $text): float|int`

Get Telegram UTF-8 length of string.


Parameters:

* `$text`: `string` Text  



### `mbSubstr(string $text, int $offset, ?int $length)`

Telegram UTF-8 multibyte substring.


Parameters:

* `$text`: `string` Text to substring  
* `$offset`: `int` Offset  
* `$length`: `?int` Length  



### `mbStrSplit(string $text, int $length): string[]`

Telegram UTF-8 multibyte split.


Parameters:

* `$text`: `string` Text  
* `$length`: `int` Length  



### `toCamelCase(string $input)`

Convert to camelCase.


Parameters:

* `$input`: `string` String  



### `toSnakeCase(string $input)`

Convert to snake_case.


Parameters:

* `$input`: `string` String  



### `markdownEscape(string $hwat)`

Escape string for markdown.


Parameters:

* `$hwat`: `string` String to escape  



### `typeEscape(string $type)`

Escape type name.


Parameters:

* `$type`: `string` String to escape  



### `methodEscape(string $method)`

Escape method name.


Parameters:

* `$method`: `string` Method name  



### `getMimeFromExtension(string $extension, string $default)`

Get mime type from file extension.


Parameters:

* `$extension`: `string` File extension  
* `$default`: `string` Default mime type  



### `getExtensionFromMime(string $mime)`

Get extension from mime type.


Parameters:

* `$mime`: `string` MIME type  



### `getExtensionFromLocation(mixed $location, string $default)`

Get extension from file location.


Parameters:

* `$location`: `mixed` File location  
* `$default`: `string` Default extension  



### `getMimeFromFile(string $file)`

Get mime type of file.


Parameters:

* `$file`: `string` File  



### `getMimeFromBuffer(string $buffer)`

Get mime type from buffer.


Parameters:

* `$buffer`: `string` Buffer  



---
Generated by [danog/phpdoc](https://phpdoc.daniil.it)
