---
title: danog\MadelineProto\Ipc\Client: IPC client.
description: 

---
# `danog\MadelineProto\Ipc\Client`
[Back to index](../../../index.md)

> Author: Daniil Gentili <daniil@daniil.it>  
  

IPC client.  




## Method list:
* `giveInstanceBySession(string $session): \danog\MadelineProto\Ipc\Client`
* `loop(callable $callback): \Generator`
* `unreference(): void`
* `isIpc(): bool`
* `uploadFromUrl(string|\danog\MadelineProto\FileCallbackInterface $url, int $size, string $fileName, callable $cb, bool $encrypted): \Generator`
* `uploadFromCallable(mixed $callable, int $size, string $mime, string $fileName, callable $cb, bool $seekable, bool $encrypted): \Generator`
* `uploadFromTgfile(mixed $media, callable $cb, bool $encrypted): \Generator`
* `methodCallAsyncRead(string $method, array|\Generator $args, array $aargs): \Generator`
* `downloadToDir(mixed $messageMedia, string|\danog\MadelineProto\FileCallbackInterface $dir, callable $cb): \Generator Downloaded file path`
* `downloadToFile(mixed $messageMedia, string|\danog\MadelineProto\FileCallbackInterface $file, callable $cb): \Generator Downloaded file path`
* `downloadToCallable(mixed $messageMedia, callable|\danog\MadelineProto\FileCallbackInterface $callable, callable $cb, bool $seekable, int $offset, int $end, int $part_size): \Generator`
* `setEventHandler(mixed $params): void`
* `getEventHandler(mixed $params): void`
* `logger(string $param, int $level, string $file): void`
* `disconnect(): \Generator`
* `start(): \Generator`
* `getWebTemplate(): string`
* `setWebTemplate(string $template): void`
* `downloadToBrowser(array|string $messageMedia, callable $cb): \Generator`
* `downloadToStream(mixed $messageMedia, mixed|\danog\MadelineProto\FileCallbackInterface $stream, callable $cb, int $offset, int $end): \Generator`
* `downloadToResponse(array|string $messageMedia, \ServerRequest $request, callable $cb): \Generator Returned response`
* `uploadEncrypted(\danog\MadelineProto\FileCallbackInterface|string|array $file, string $fileName, callable $cb): \Generator`
* `upload(\danog\MadelineProto\FileCallbackInterface|string|array $file, string $fileName, callable $cb, bool $encrypted): \Generator`
* `uploadFromStream(mixed $stream, int $size, string $mime, string $fileName, callable $cb, bool $encrypted): \Generator`

## Methods:
### `giveInstanceBySession(string $session): \danog\MadelineProto\Ipc\Client`

Returns an instance of a client by session name.


Parameters:
* `$session`: `string`   



### `loop(callable $callback): \Generator`

Run the provided async callable.


Parameters:
* `$callback`: `callable` Async callable to run  


#### See also: 
* `\Generator`




### `unreference(): void`

Unreference.



### `isIpc(): bool`

Whether we're an IPC client instance.



### `uploadFromUrl(string|\danog\MadelineProto\FileCallbackInterface $url, int $size, string $fileName, callable $cb, bool $encrypted): \Generator`

Upload file from URL.


Parameters:
* `$url`: `string|\danog\MadelineProto\FileCallbackInterface` URL of file  
* `$size`: `int` Size of file  
* `$fileName`: `string` File name  
* `$cb`: `callable` Callback (DEPRECATED, use FileCallbackInterface)  
* `$encrypted`: `bool` Whether to encrypt file for secret chats  


#### See also: 
* [`\danog\MadelineProto\FileCallbackInterface`: File callback interface.](../FileCallbackInterface.md)
* `\Generator`




### `uploadFromCallable(mixed $callable, int $size, string $mime, string $fileName, callable $cb, bool $seekable, bool $encrypted): \Generator`

Upload file from callable.
The callable must accept two parameters: int $offset, int $size
The callable must return a string with the contest of the file at the specified offset and size.

Parameters:
* `$callable`: `mixed` Callable  
* `$size`: `int` File size  
* `$mime`: `string` Mime type  
* `$fileName`: `string` File name  
* `$cb`: `callable` Callback (DEPRECATED, use FileCallbackInterface)  
* `$seekable`: `bool` Whether chunks can be fetched out of order  
* `$encrypted`: `bool` Whether to encrypt file for secret chats  


Fully typed return value:
```
\Generator<int, \Amp\Promise<\Amp\Ipc\Sync\ChannelledSocket>|\Amp\Promise<mixed>, mixed, mixed>
```
#### See also: 
* `\Amp\Ipc\Sync\ChannelledSocket`
* `\Amp\Promise`
* `\Generator`




### `uploadFromTgfile(mixed $media, callable $cb, bool $encrypted): \Generator`

Reupload telegram file.


Parameters:
* `$media`: `mixed` Telegram file  
* `$cb`: `callable` Callback (DEPRECATED, use FileCallbackInterface)  
* `$encrypted`: `bool` Whether to encrypt file for secret chats  


Fully typed return value:
```
\Generator<int, \Amp\Promise<\Amp\Ipc\Sync\ChannelledSocket>|\Amp\Promise<mixed>, mixed, mixed>
```
#### See also: 
* `\Amp\Ipc\Sync\ChannelledSocket`
* `\Amp\Promise`
* `\Generator`




### `methodCallAsyncRead(string $method, array|\Generator $args, array $aargs): \Generator`

Call method and wait asynchronously for response.
If the $aargs['noResponse'] is true, will not wait for a response.

Parameters:
* `$method`: `string` Method name  
* `$args`: `array|\Generator` Arguments  
  Full type:
  ```
  array|\Generator<mixed, mixed, mixed, array>
  ```
* `$aargs`: `array` Additional arguments  


#### See also: 
* `\Generator`




### `downloadToDir(mixed $messageMedia, string|\danog\MadelineProto\FileCallbackInterface $dir, callable $cb): \Generator Downloaded file path`

Download file to directory.


Parameters:
* `$messageMedia`: `mixed` File to download  
* `$dir`: `string|\danog\MadelineProto\FileCallbackInterface` Directory where to download the file  
* `$cb`: `callable` Callback (DEPRECATED, use FileCallbackInterface)  


Return value: Downloaded file path

Fully typed return value:
```
\Generator<int, \Amp\Promise<\Amp\Ipc\Sync\ChannelledSocket>|\Amp\Promise<mixed>, mixed, mixed>
```
#### See also: 
* [`\danog\MadelineProto\FileCallbackInterface`: File callback interface.](../FileCallbackInterface.md)
* `\Amp\Ipc\Sync\ChannelledSocket`
* `\Amp\Promise`
* `\Generator`




### `downloadToFile(mixed $messageMedia, string|\danog\MadelineProto\FileCallbackInterface $file, callable $cb): \Generator Downloaded file path`

Download file.


Parameters:
* `$messageMedia`: `mixed` File to download  
* `$file`: `string|\danog\MadelineProto\FileCallbackInterface` Downloaded file path  
* `$cb`: `callable` Callback (DEPRECATED, use FileCallbackInterface)  


Return value: Downloaded file path

Fully typed return value:
```
\Generator<int, \Amp\Promise<\Amp\Ipc\Sync\ChannelledSocket>|\Amp\Promise<mixed>, mixed, mixed>
```
#### See also: 
* [`\danog\MadelineProto\FileCallbackInterface`: File callback interface.](../FileCallbackInterface.md)
* `\Amp\Ipc\Sync\ChannelledSocket`
* `\Amp\Promise`
* `\Generator`




### `downloadToCallable(mixed $messageMedia, callable|\danog\MadelineProto\FileCallbackInterface $callable, callable $cb, bool $seekable, int $offset, int $end, int $part_size): \Generator`

Download file to callable.
The callable must accept two parameters: string $payload, int $offset
The callable will be called (possibly out of order, depending on the value of $seekable).
The callable should return the number of written bytes.

Parameters:
* `$messageMedia`: `mixed` File to download  
* `$callable`: `callable|\danog\MadelineProto\FileCallbackInterface` Chunk callback  
* `$cb`: `callable` Status callback (DEPRECATED, use FileCallbackInterface)  
* `$seekable`: `bool` Whether the callable can be called out of order  
* `$offset`: `int` Offset where to start downloading  
* `$end`: `int` Offset where to stop downloading (inclusive)  
* `$part_size`: `int` Size of each chunk  


Fully typed return value:
```
\Generator<int, \Amp\Promise<\Amp\Ipc\Sync\ChannelledSocket>|\Amp\Promise<mixed>, mixed, mixed>
```
#### See also: 
* [`\danog\MadelineProto\FileCallbackInterface`: File callback interface.](../FileCallbackInterface.md)
* `\Amp\Ipc\Sync\ChannelledSocket`
* `\Amp\Promise`
* `\Generator`




### `setEventHandler(mixed $params): void`

Placeholder.


Parameters:
* `$params`: `mixed` Params  



### `getEventHandler(mixed $params): void`

Placeholder.


Parameters:
* `$params`: `mixed` Params  



### `logger(string $param, int $level, string $file): void`

Logger.


Parameters:
* `$param`: `string` Parameter  
* `$level`: `int` Logging level  
* `$file`: `string` File where the message originated  



### `disconnect(): \Generator`

Disconnect cleanly from main instance.


Fully typed return value:
```
\Generator<int, \Amp\Promise, mixed, void>
```
#### See also: 
* `\Amp\Promise`
* `\Generator`




### `start(): \Generator`

Log in to telegram (via CLI or web).


#### See also: 
* `\Generator`




### `getWebTemplate(): string`

Get web template.



### `setWebTemplate(string $template): void`

Set web template.


Parameters:
* `$template`: `string` Template  



### `downloadToBrowser(array|string $messageMedia, callable $cb): \Generator`

Download file to browser.
Supports HEAD requests and content-ranges for parallel and resumed downloads.

Parameters:
* `$messageMedia`: `array|string` File to download  
* `$cb`: `callable` Status callback (can also use FileCallback)  


#### See also: 
* `\Generator`




### `downloadToStream(mixed $messageMedia, mixed|\danog\MadelineProto\FileCallbackInterface $stream, callable $cb, int $offset, int $end): \Generator`

Download file to stream.


Parameters:
* `$messageMedia`: `mixed` File to download  
* `$stream`: `mixed|\danog\MadelineProto\FileCallbackInterface` Stream where to download file  
* `$cb`: `callable` Callback (DEPRECATED, use FileCallbackInterface)  
* `$offset`: `int` Offset where to start downloading  
* `$end`: `int` Offset where to end download  


Fully typed return value:
```
\Generator<int, \Amp\Promise<\Amp\Ipc\Sync\ChannelledSocket>|\Amp\Promise<mixed>|mixed, mixed, mixed>
```
#### See also: 
* [`\danog\MadelineProto\FileCallbackInterface`: File callback interface.](../FileCallbackInterface.md)
* `\Amp\Ipc\Sync\ChannelledSocket`
* `\Amp\Promise`
* `\Generator`




### `downloadToResponse(array|string $messageMedia, \ServerRequest $request, callable $cb): \Generator Returned response`

Download file to amphp/http-server response.
Supports HEAD requests and content-ranges for parallel and resumed downloads.

Parameters:
* `$messageMedia`: `array|string` File to download  
* `$request`: `\ServerRequest` Request  
* `$cb`: `callable` Status callback (can also use FileCallback)  


Return value: Returned response

Fully typed return value:
```
\Generator<mixed, array, mixed, \Amp\Http\Server\Response>
```
#### See also: 
* `\ServerRequest`
* `\Amp\Http\Server\Response`
* `\Generator`




### `uploadEncrypted(\danog\MadelineProto\FileCallbackInterface|string|array $file, string $fileName, callable $cb): \Generator`

Upload file to secret chat.


Parameters:
* `$file`: `\danog\MadelineProto\FileCallbackInterface|string|array` File, URL or Telegram file to upload  
* `$fileName`: `string` File name  
* `$cb`: `callable` Callback (DEPRECATED, use FileCallbackInterface)  


Fully typed return value:
```
\Generator<int|mixed, \Amp\Promise|\Amp\Promise<\Amp\File\File>|\Amp\Promise<\Amp\Ipc\Sync\ChannelledSocket>|\Amp\Promise<int>|\Amp\Promise<mixed>|\Amp\Promise<null|string>|\danog\MadelineProto\Stream\StreamInterface|array|int|mixed, mixed, mixed>
```
#### See also: 
* [`\danog\MadelineProto\FileCallbackInterface`: File callback interface.](../FileCallbackInterface.md)
* `\Amp\Promise`
* `\Amp\File\File`
* `\Amp\Ipc\Sync\ChannelledSocket`
* [`\danog\MadelineProto\Stream\StreamInterface`: Generic stream interface.](../Stream/StreamInterface.md)
* `\Generator`




### `upload(\danog\MadelineProto\FileCallbackInterface|string|array $file, string $fileName, callable $cb, bool $encrypted): \Generator`

Upload file.


Parameters:
* `$file`: `\danog\MadelineProto\FileCallbackInterface|string|array` File, URL or Telegram file to upload  
* `$fileName`: `string` File name  
* `$cb`: `callable` Callback (DEPRECATED, use FileCallbackInterface)  
* `$encrypted`: `bool` Whether to encrypt file for secret chats  


Fully typed return value:
```
\Generator<int|mixed, \Amp\Promise|\Amp\Promise<\Amp\File\File>|\Amp\Promise<\Amp\Ipc\Sync\ChannelledSocket>|\Amp\Promise<int>|\Amp\Promise<mixed>|\Amp\Promise<null|string>|\danog\MadelineProto\Stream\StreamInterface|array|int|mixed, mixed, mixed>
```
#### See also: 
* [`\danog\MadelineProto\FileCallbackInterface`: File callback interface.](../FileCallbackInterface.md)
* `\Amp\Promise`
* `\Amp\File\File`
* `\Amp\Ipc\Sync\ChannelledSocket`
* [`\danog\MadelineProto\Stream\StreamInterface`: Generic stream interface.](../Stream/StreamInterface.md)
* `\Generator`




### `uploadFromStream(mixed $stream, int $size, string $mime, string $fileName, callable $cb, bool $encrypted): \Generator`

Upload file from stream.


Parameters:
* `$stream`: `mixed` PHP resource or AMPHP async stream  
* `$size`: `int` File size  
* `$mime`: `string` Mime type  
* `$fileName`: `string` File name  
* `$cb`: `callable` Callback (DEPRECATED, use FileCallbackInterface)  
* `$encrypted`: `bool` Whether to encrypt file for secret chats  


Fully typed return value:
```
\Generator<int|mixed, \Amp\Promise|\Amp\Promise<int>|\Amp\Promise<null|string>|\danog\MadelineProto\Stream\StreamInterface|array|int|mixed, mixed, mixed>
```
#### See also: 
* `\Amp\Promise`
* [`\danog\MadelineProto\Stream\StreamInterface`: Generic stream interface.](../Stream/StreamInterface.md)
* `\Generator`




---
Generated by [danog/phpdoc](https://phpdoc.daniil.it)
