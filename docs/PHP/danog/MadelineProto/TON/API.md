---
title: "danog\\MadelineProto\\TON\\API: TON API."
description: ""
image: "https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png"
parent: "MadelineProto API"

---
# `danog\MadelineProto\TON\API`
[Back to index](../../../index.html)

> Author: Daniil Gentili <daniil@daniil.it>  
  

TON API.  




## Method list:
* `after(\Generator|\Promise $a, \Generator|\Promise $b): \Amp\Promise`
* `all((\Generator|\Promise)[] $promises): \Amp\Promise`
* `any((\Promise|\Generator)[] $promises): \Amp\Promise`
* `arr(mixed $params)`
* `base64urlDecode(string $data)`
* `base64urlEncode(string $data)`
* `botAPItoMTProto(array $parameters): \Amp\Promise`
* `call(\Generator|\Promise|mixed $promise): \Amp\Promise`
* `callFork(\Generator|\Promise $promise, ?\Generator|\Promise $actual, string $file): \Amp\Promise|mixed`
* `callForkDefer(\Generator|\Promise $promise)`
* `closeConnection(string $message): void`
* `connect(string $config): \Amp\Promise`
* `echo(string $string): \Amp\Promise`
* `end(array $what)`
* `first((\Promise|\Generator)[] $promises): \Amp\Promise`
* `flock(string $file, int $operation, float $polling, ?\Promise $token, ?callable $failureCb)`
* `genVectorHash(array $ints): \string Vector hash`
* `getExtensionFromLocation(mixed $location, string $default)`
* `getExtensionFromMime(string $mime)`
* `getMethodNamespaces()`
* `getMimeFromBuffer(string $buffer)`
* `getMimeFromExtension(string $extension, string $default)`
* `getMimeFromFile(string $file)`
* `getVar(object $obj, string $var)`
* `hasVar(object $obj, string $var)`
* `inflateStripped(string $stripped): \string JPG payload`
* `isAltervista(): bool`
* `isArrayOrAlike(mixed $var): bool`
* `logger(string $param, int $level, string $file)`
* `loop(callable $func): \Amp\Promise`
* `markdownEscape(string $hwat)`
* `methodCall(string $methodName, array $args): \Amp\Promise`
* `methodEscape(string $method)`
* `packDouble(float $value)`
* `packSignedInt(int $value)`
* `packSignedLong(int $value)`
* `packUnsignedInt(int $value)`
* `posmod(int $a, int $b): \int Modulo`
* `random(int $length): \string Random string`
* `randomInt(int $modulus)`
* `readLine(string $prompt): \Amp\Promise<string>`
* `rethrow(\Throwable $e, string $file)`
* `rleDecode(string $string)`
* `rleEncode(string $string)`
* `setVar(object $obj, string $var, mixed $val)`
* `sleep(int|float $time): \Amp\Promise`
* `some((\Promise|\Generator)[] $promises): \Amp\Promise`
* `timeout(\Generator|\Promise $promise, int $timeout): \Amp\Promise`
* `timeoutWithDefault(\Promise|\Generator $promise, int $timeout): \Amp\Promise<\TReturn>|\Promise<\TReturnAlt>`
* `toCamelCase(string $input)`
* `toSnakeCase(string $input)`
* `typeEscape(string $type)`
* `unpackDouble(string $value)`
* `unpackSignedInt(string $value): int`
* `unpackSignedLong(string $value): int`
* `unpackSignedLongString(string|int|array $value)`
* `wait(\Generator|\Promise $promise, bool $ignoreSignal)`
* `async(bool $async)`
* `init()`
* `initAsynchronously()`
* `inited(): bool`
* `forceInit(bool $inited)`

## Methods:
### `after(\Generator|\Promise $a, \Generator|\Promise $b): \Amp\Promise`

Call promise $b after promise $a.


Parameters:

* `$a`: `\Generator|\Promise` Promise A  
* `$b`: `\Generator|\Promise` Promise B  


#### See also: 
* `\Generator`
* `\Promise`
* `\Amp\Promise`




### `all((\Generator|\Promise)[] $promises): \Amp\Promise`

Returns a promise that succeeds when all promises succeed, and fails if any promise fails.
Returned promise succeeds with an array of values used to succeed each contained promise, with keys corresponding to the array of promises.

Parameters:

* `$promises`: `(\Generator|\Promise)[]` Promises  


#### See also: 
* `\Generator`
* `\Promise`
* `\Amp\Promise`




### `any((\Promise|\Generator)[] $promises): \Amp\Promise`

Returns a promise that is resolved when all promises are resolved. The returned promise will not fail.


Parameters:

* `$promises`: `(\Promise|\Generator)[]` Promises  


#### See also: 
* `\Promise`
* `\Generator`
* `\Amp\Promise`




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



### `botAPItoMTProto(array $parameters): \Amp\Promise`

Convert parameters.


Parameters:

* `$parameters`: `array` Parameters  


#### See also: 
* `\Amp\Promise`




### `call(\Generator|\Promise|mixed $promise): \Amp\Promise`

Convert generator, promise or any other value to a promise.


Parameters:

* `$promise`: `\Generator|\Promise|mixed`   
  Full type:
  ```
  \Generator<mixed, mixed, mixed, \TReturn>|\Promise<\TReturn>|\TReturn
  ```


Fully typed return value:
```
\Promise<\TReturn>
```
#### See also: 
* `\Generator`
* `\Promise`
* `\TReturn`
* `\Amp\Promise`




### `callFork(\Generator|\Promise $promise, ?\Generator|\Promise $actual, string $file): \Amp\Promise|mixed`

Call promise in background.


Parameters:

* `$promise`: `\Generator|\Promise` Promise to resolve  
* `$actual`: `?\Generator|\Promise` Promise to resolve instead of $promise  
* `$file`: `string` File  


#### See also: 
* `\Generator`
* `\Promise`
* `\Amp\Promise`




### `callForkDefer(\Generator|\Promise $promise)`

Call promise in background, deferring execution.


Parameters:

* `$promise`: `\Generator|\Promise` Promise to resolve  


#### See also: 
* `\Generator`
* `\Promise`




### `closeConnection(string $message): void`

Close connection with client, connected via web.


Parameters:

* `$message`: `string` Message  



### `connect(string $config): \Amp\Promise`

Connect to the lite endpoints specified in the config file.


Parameters:

* `$config`: `string` Path to config file  


#### See also: 
* `\Amp\Promise`




### `echo(string $string): \Amp\Promise`

Asynchronously write to stdout/browser.


Parameters:

* `$string`: `string` Message to echo  


#### See also: 
* `\Amp\Promise`




### `end(array $what)`

Get final element of array.


Parameters:

* `$what`: `array` Array  



### `first((\Promise|\Generator)[] $promises): \Amp\Promise`

Returns a promise that succeeds when the first promise succeeds, and fails only if all promises fail.


Parameters:

* `$promises`: `(\Promise|\Generator)[]` Promises  


#### See also: 
* `\Promise`
* `\Generator`
* `\Amp\Promise`




### `flock(string $file, int $operation, float $polling, ?\Promise $token, ?callable $failureCb)`

Asynchronously lock a file
Resolves with a callbable that MUST eventually be called in order to release the lock.


Parameters:

* `$file`: `string` File to lock  
* `$operation`: `int` Locking mode  
* `$polling`: `float` Polling interval  
* `$token`: `?\Promise` Cancellation token  
* `$failureCb`: `?callable` Failure callback, called only once if the first locking attempt fails.  


#### See also: 
* `\Promise`




### `genVectorHash(array $ints): \string Vector hash`

Generate MTProto vector hash.


Parameters:

* `$ints`: `array` IDs  


Return value: Vector hash


### `getExtensionFromLocation(mixed $location, string $default)`

Get extension from file location.


Parameters:

* `$location`: `mixed` File location  
* `$default`: `string` Default extension  



### `getExtensionFromMime(string $mime)`

Get extension from mime type.


Parameters:

* `$mime`: `string` MIME type  



### `getMethodNamespaces()`

Get TL method namespaces.


Fully typed return value:
```
array|\Amp\Promise<array>
```
#### See also: 
* `\Amp\Promise`




### `getMimeFromBuffer(string $buffer)`

Get mime type from buffer.


Parameters:

* `$buffer`: `string` Buffer  



### `getMimeFromExtension(string $extension, string $default)`

Get mime type from file extension.


Parameters:

* `$extension`: `string` File extension  
* `$default`: `string` Default mime type  



### `getMimeFromFile(string $file)`

Get mime type of file.


Parameters:

* `$file`: `string` File  



### `getVar(object $obj, string $var)`

Accesses a private variable from an object.


Parameters:

* `$obj`: `object` Object  
* `$var`: `string` Attribute name  



### `hasVar(object $obj, string $var)`

Checks private property exists in an object.


Parameters:

* `$obj`: `object` Object  
* `$var`: `string` Attribute name  



### `inflateStripped(string $stripped): \string JPG payload`

Inflate stripped photosize to full JPG payload.


Parameters:

* `$stripped`: `string` Stripped photosize  


Return value: JPG payload


### `isAltervista(): bool`

Whether this is altervista.



### `isArrayOrAlike(mixed $var): bool`

Check if is array or similar (traversable && countable && arrayAccess).


Parameters:

* `$var`: `mixed` Value to check  



### `logger(string $param, int $level, string $file)`

Logger.


Parameters:

* `$param`: `string` Parameter  
* `$level`: `int` Logging level  
* `$file`: `string` File where the message originated  


Fully typed return value:
```
void|\Amp\Promise<void>
```
#### See also: 
* `\Amp\Promise`




### `loop(callable $func): \Amp\Promise`

Asynchronously run async callable.


Parameters:

* `$func`: `callable` Function  


#### See also: 
* `\Amp\Promise`




### `markdownEscape(string $hwat)`

Escape string for markdown.


Parameters:

* `$hwat`: `string` String to escape  



### `methodCall(string $methodName, array $args): \Amp\Promise`

Call lite method.


Parameters:

* `$methodName`: `string` Method name  
* `$args`: `array` Arguments  


#### See also: 
* `\Amp\Promise`




### `methodEscape(string $method)`

Escape method name.


Parameters:

* `$method`: `string` Method name  



### `packDouble(float $value)`

Convert double to binary version.


Parameters:

* `$value`: `float` Value to convert  



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



### `posmod(int $a, int $b): \int Modulo`

Positive modulo
Works just like the % (modulus) operator, only returns always a postive number.


Parameters:

* `$a`: `int` A  
* `$b`: `int` B  


Return value: Modulo


### `random(int $length): \string Random string`

Get random string of specified length.


Parameters:

* `$length`: `int` Length  


Return value: Random string


### `randomInt(int $modulus)`

Get random integer.


Parameters:

* `$modulus`: `int` Modulus  



### `readLine(string $prompt): \Amp\Promise<string>`

Asynchronously read line.


Parameters:

* `$prompt`: `string` Prompt  


#### See also: 
* `\Amp\Promise`




### `rethrow(\Throwable $e, string $file)`

Rethrow error catched in strand.


Parameters:

* `$e`: `\Throwable` Exception  
* `$file`: `string` File where the strand started  


#### See also: 
* `\Throwable`




### `rleDecode(string $string)`

null-byte RLE decode.


Parameters:

* `$string`: `string` Data to decode  



### `rleEncode(string $string)`

null-byte RLE encode.


Parameters:

* `$string`: `string` Data to encode  



### `setVar(object $obj, string $var, mixed $val)`

Sets a private variable in an object.


Parameters:

* `$obj`: `object` Object  
* `$var`: `string` Attribute name  
* `$val`: `mixed` Attribute value  



### `sleep(int|float $time): \Amp\Promise`

Asynchronously sleep.


Parameters:

* `$time`: `int|float` Number of seconds to sleep for  


#### See also: 
* `\Amp\Promise`




### `some((\Promise|\Generator)[] $promises): \Amp\Promise`

Resolves with a two-item array delineating successful and failed Promise results.
The returned promise will only fail if the given number of required promises fail.

Parameters:

* `$promises`: `(\Promise|\Generator)[]` Promises  


#### See also: 
* `\Promise`
* `\Generator`
* `\Amp\Promise`




### `timeout(\Generator|\Promise $promise, int $timeout): \Amp\Promise`

Create an artificial timeout for any \Generator or Promise.


Parameters:

* `$promise`: `\Generator|\Promise`   
* `$timeout`: `int`   


#### See also: 
* `\Generator`
* `\Promise`
* `\Amp\Promise`




### `timeoutWithDefault(\Promise|\Generator $promise, int $timeout): \Amp\Promise<\TReturn>|\Promise<\TReturnAlt>`

Creates an artificial timeout for any `Promise`.
If the promise is resolved before the timeout expires, the result is returned

If the timeout expires before the promise is resolved, a default value is returned

Parameters:

* `$promise`: `\Promise|\Generator` Promise to which the timeout is applied.  
  Full type:
  ```
  \Promise<\TReturn>|\TGenerator
  ```
* `$timeout`: `int` Timeout in milliseconds.  


#### See also: 
* `\Promise`
* `\Generator`
* `\TReturn`
* `\TGenerator`
* `\TReturnAlt`
* `\Amp\Promise`




### `toCamelCase(string $input)`

Convert to camelCase.


Parameters:

* `$input`: `string` String  



### `toSnakeCase(string $input)`

Convert to snake_case.


Parameters:

* `$input`: `string` String  



### `typeEscape(string $type)`

Escape type name.


Parameters:

* `$type`: `string` String to escape  



### `unpackDouble(string $value)`

Unpack binary double.


Parameters:

* `$value`: `string` Value to unpack  



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



### `wait(\Generator|\Promise $promise, bool $ignoreSignal)`

Synchronously wait for a promise|generator.


Parameters:

* `$promise`: `\Generator|\Promise` The promise to wait for  
* `$ignoreSignal`: `bool` Whether to ignore shutdown signals  


#### See also: 
* `\Generator`
* `\Promise`




### `async(bool $async)`

Enable or disable async.


Parameters:

* `$async`: `bool` Whether to enable or disable async  



### `init()`

Blockingly init.



### `initAsynchronously()`

Asynchronously init.



### `inited(): bool`

Check if we've already inited.



### `forceInit(bool $inited)`

Mark instance as (de)inited forcefully.


Parameters:

* `$inited`: `bool` Whether to mark the instance as inited or deinited  



---
Generated by [danog/phpdoc](https://phpdoc.daniil.it)
