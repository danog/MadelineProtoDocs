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
* `testFibers(): array{maxFibers: int, realMemoryMb: int, maps: ?int, maxMaps: ?int}`
* `getMaps()`
* `getMaxMaps()`
* `genVectorHash(array $ints): \string Vector hash`
* `randomInt(int $modulus)`
* `random(int $length): \string Random string`
* `posmod(int $a, int $b): \int Modulo`
* `unpackSignedInt(string $value)`
* `unpackSignedLong(string $value)`
* `unpackSignedLongString(string|int|array $value)`
* `packSignedInt(int $value)`
* `packSignedLong(int $value)`
* `packUnsignedInt(int $value)`
* `packDouble(float $value)`
* `unpackDouble(string $value)`
* `isArrayOrAlike(mixed $var)`
* `arr(mixed $params)`
* `base64urlDecode(string $data)`
* `base64urlEncode(string $data)`
* `rleDecode(string $string)`
* `rleEncode(string $string)`
* `inflateStripped(string $stripped): \string JPG payload`
* `closeConnection(string $message)`
* `end(array $what)`
* `isAltervista()`
* `hasVar(object $obj, string $var)`
* `getVar(object $obj, string $var)`
* `setVar(object $obj, string $var, mixed $val)`
* `rethrow()`
* `flock(string $file, int $operation, float $polling, ?\Amp\Cancellation $token, ?\Closure $failureCb): mixed`
* `sleep(float $time)`
* `readLine(string $prompt)`
* `echo(string $string)`
* `mbStrlen(string $text)`
* `mbSubstr(string $text, int $offset, null|int $length)`
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
### `testFibers(): array{maxFibers: int, realMemoryMb: int, maps: ?int, maxMaps: ?int}`

Test fibers.



### `getMaps()`

Get current number of memory-mapped regions, UNIX only.



### `getMaxMaps()`

Get maximum number of memory-mapped regions, UNIX only.
Use testFibers to get the maximum number of fibers on any platform.


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


### `unpackSignedInt(string $value)`

Unpack base256 signed int.


Parameters:

* `$value`: `string` base256 int  



### `unpackSignedLong(string $value)`

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



### `isArrayOrAlike(mixed $var)`

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


### `closeConnection(string $message)`

Close connection with client, connected via web.


Parameters:

* `$message`: `string` Message  



### `end(array $what)`

Get final element of array.


Parameters:

* `$what`: `array` Array  



### `isAltervista()`

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



### `rethrow()`

Rethrow exception into event loop.



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




### `sleep(float $time)`

Asynchronously sleep.


Parameters:

* `$time`: `float` Number of seconds to sleep for  



### `readLine(string $prompt)`

Asynchronously read line.


Parameters:

* `$prompt`: `string` Prompt  



### `echo(string $string)`

Asynchronously write to stdout/browser.


Parameters:

* `$string`: `string` Message to echo  



### `mbStrlen(string $text)`

Get Telegram UTF-8 length of string.


Parameters:

* `$text`: `string` Text  



### `mbSubstr(string $text, int $offset, null|int $length)`

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
