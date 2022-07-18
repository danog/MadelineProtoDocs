---
title: "danog\\MadelineProto\\EventHandler: Event handler."
description: ""
image: "https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png"
parent: "MadelineProto API"

---
# `danog\MadelineProto\EventHandler`
[Back to index](../../index.md)

> Author: Daniil Gentili <daniil@daniil.it>  
  

Event handler.  




## Method list:
* `startAndLoop(string $session, \danog\MadelineProto\SettingsAbstract $settings): void`
* `getReportPeers(): array|string|int`
* `getAPI(): \danog\MadelineProto\MTProto`
* `MTProtoToBotAPI(array $data): \Amp\Promise<array>`
* `MTProtoToTd(mixed $params): \Amp\Promise`
* `MTProtoToTdcli(mixed $params): \Amp\Promise`
* `acceptCall(array $call): \Amp\Promise`
* `acceptSecretChat(array $params): \Amp\Promise`
* `acceptTos(): \Amp\Promise`
* `addUser(array $user): \Amp\Promise`
* `after(\Generator|\Promise $a, \Generator|\Promise $b): \Amp\Promise`
* `all((\Generator|\Promise)[] $promises): \Amp\Promise`
* `any((\Promise|\Generator)[] $promises): \Amp\Promise`
* `arr(mixed $params): array`
* `base64urlDecode(string $data): string`
* `base64urlEncode(string $data): string`
* `botAPIToMTProto(array $arguments): \Amp\Promise<array>`
* `botLogin(string $token): \Amp\Promise`
* `call(\Generator|\Promise|mixed $promise): \Amp\Promise`
* `callFork(\Generator|\Promise $promise, ?\Generator|\Promise $actual, string $file): \Amp\Promise|mixed`
* `callForkDefer(\Generator|\Promise $promise): void`
* `callStatus(int $id): mixed`
* `checkTos(): \Amp\Promise`
* `cleanup(): \Amp\Promise`
* `closeConnection(string $message): void`
* `complete2faLogin(string $password): \Amp\Promise`
* `completeCall(array $params): \Amp\Promise`
* `completePhoneLogin(string $code): \Amp\Promise`
* `completeSignup(string $first_name, string $last_name): \Amp\Promise`
* `confirmCall(array $params): \Amp\Promise`
* `connectToAllDcs(bool $reconnectAll): \Amp\Promise`
* `declineTos(): \Amp\Promise`
* `discardCall(array $call, array $reason, array $rating, bool $need_debug): \Amp\Promise`
* `discardSecretChat(int $chat): \Amp\Promise`
* `downloadToBrowser(array|string $messageMedia, callable $cb): \Amp\Promise`
* `downloadToCallable(mixed $messageMedia, callable|\danog\MadelineProto\FileCallbackInterface $callable, callable $cb, bool $seekable, int $offset, int $end, int $part_size): \Amp\Promise`
* `downloadToDir(mixed $messageMedia, string|\danog\MadelineProto\FileCallbackInterface $dir, callable $cb): \Amp\Promise`
* `downloadToFile(mixed $messageMedia, string|\danog\MadelineProto\FileCallbackInterface $file, callable $cb): \Amp\Promise Downloaded file path`
* `downloadToResponse(array|string $messageMedia, \ServerRequest $request, callable $cb): \Amp\Promise Returned response`
* `downloadToStream(mixed $messageMedia, mixed|\danog\MadelineProto\FileCallbackInterface $stream, callable $cb, int $offset, int $end): \Amp\Promise`
* `echo(string $string): \Amp\Promise`
* `end(array $what): mixed`
* `exportAuthorization(): \Amp\Promise`
* `extractBotAPIFile(array $info): ?array`
* `fileGetContents(string $url): \Amp\Promise`
* `first((\Promise|\Generator)[] $promises): \Amp\Promise`
* `flock(string $file, int $operation, float $polling, ?\Promise $token, ?callable $failureCb)`
* `fromSupergroup(int $id): int`
* `fullChatLastUpdated(mixed $id): \Amp\Promise<int>`
* `fullGetSelf(): \Amp\Promise<array|bool>`
* `genVectorHash(array $ints): \string Vector hash`
* `getAllMethods(): mixed`
* `getAuthorization(): mixed`
* `getCachedConfig(): mixed`
* `getCall(int $call): mixed`
* `getCdnConfig(string $datacenter): \Amp\Promise`
* `getConfig(array $config, array $options): \Amp\Promise`
* `getDNSClient(): mixed`
* `getDataCenterConnections(): mixed`
* `getDataCenterId(): int|string`
* `getDialogs(bool $force): \Amp\Promise`
* `getDownloadInfo(mixed $messageMedia): \Amp\Promise<array>`
* `getEventHandler(): mixed`
* `getExtensionFromLocation(mixed $location, string $default): string`
* `getExtensionFromMime(string $mime): string`
* `getFileInfo(mixed $constructor): \Amp\Promise<array>`
* `getFolderId(mixed $id): ?int`
* `getFullDialogs(bool $force): \Amp\Promise`
* `getFullInfo(mixed $id): \Amp\Promise FullInfo object`
* `getHTTPClient(): mixed`
* `getHint(): mixed`
* `getId(mixed $id): int`
* `getInfo(mixed $id, bool $recursive): \Amp\Promise Info object`
* `getLogger()`
* `getMethodNamespaces(): mixed`
* `getMethodsNamespaced(): mixed`
* `getMimeFromBuffer(string $buffer): string`
* `getMimeFromExtension(string $extension, string $default): string`
* `getMimeFromFile(string $file): string`
* `getPropicInfo(mixed $messageMedia): \Amp\Promise<array>`
* `getPsrLogger()`
* `getPwrChat(mixed $id): \Amp\Promise Chat object`
* `getSecretChat(array|int $chat): mixed`
* `getSelf(): mixed`
* `getSettings(): mixed`
* `getSponsoredMessages(int|array $peer): \Amp\Promise`
* `getTL(): mixed`
* `getVar(object $obj, string $var): mixed`
* `getWebMessage(string $message)`
* `getWebTemplate(): mixed`
* `hasAllAuth(): mixed`
* `hasEventHandler(): mixed`
* `hasReportPeers(): mixed`
* `hasSecretChat(array|int $chat): mixed`
* `hasVar(object $obj, string $var): bool`
* `importAuthorization(array<int, string> $authorization, int $mainDcID): \Amp\Promise`
* `inflateStripped(string $stripped): \string JPG payload`
* `initSelfRestart(): mixed`
* `isAltervista(): bool`
* `isArrayOrAlike(mixed $var): bool`
* `isIpc(): mixed`
* `isIpcWorker(): mixed`
* `isPremium()`
* `isSupergroup(int $id): bool`
* `logger(string $param, int $level, string $file): mixed`
* `logout(): \Amp\Promise`
* `loop(callable|null $callback): \Amp\Promise`
* `loopFork(): \Amp\Promise`
* `markdownEscape(string $hwat): string`
* `mbStrSplit(string $text, int $length): array`
* `mbStrlen(string $text): float|int`
* `mbSubstr(string $text, int $offset, ?int $length): string`
* `methodCall(string $method, array|\Generator $args, array $aargs): \Amp\Promise`
* `methodCallWrite(string $method, array|\Generator $args, array $aargs): \Amp\Promise`
* `methodEscape(string $method): string`
* `packDouble(float $value): string`
* `packSignedInt(int $value): string`
* `packSignedLong(int $value): string`
* `packUnsignedInt(int $value): string`
* `peerIsset(mixed $id): \Amp\Promise`
* `phoneLogin(string $number, int $sms_type): \Amp\Promise`
* `posmod(int $a, int $b): \int Modulo`
* `random(int $length): \string Random string`
* `randomInt(int $modulus): int`
* `readLine(string $prompt): \Amp\Promise<string>`
* `refreshFullPeerCache(mixed $id): \Amp\Promise`
* `refreshPeerCache(mixed $id): \Amp\Promise`
* `rekey(int $chat): \Amp\Promise`
* `report(string $message, string $parseMode): \Amp\Promise`
* `requestCall(mixed $user): \Amp\Promise`
* `requestSecretChat(mixed $user): \Amp\Promise`
* `resetUpdateState(): mixed`
* `resolveUsername(string $username): \Amp\Promise`
* `restart(): void`
* `rethrow(\Throwable $e, string $file): void`
* `rleDecode(string $string): string`
* `rleEncode(string $string): string`
* `secretChatStatus(int $chat): mixed`
* `serializeAll(): void`
* `setCallback(callable $callback): mixed`
* `setEventHandler(class-string<\danog\MadelineProto\EventHandler> $eventHandler): \Amp\Promise`
* `setNoop(): mixed`
* `setReportPeers(int|string $userOrId): \Amp\Promise`
* `setVar(object $obj, string $var, mixed $val): void`
* `setWebTemplate(string $template): mixed`
* `setWebhook(string $hook_url, string $pem_path): mixed`
* `setupLogger(): mixed`
* `sleep(int|float $time): \Amp\Promise`
* `some((\Promise|\Generator)[] $promises): \Amp\Promise`
* `start(): \Amp\Promise`
* `stop(): void`
* `tdToMTProto(array $params): \Amp\Promise<array>`
* `tdToTdcli(mixed $params): mixed`
* `tdcliToTd(array $params, array $key): mixed`
* `timeout(\Generator|\Promise $promise, int $timeout): \Amp\Promise`
* `timeoutWithDefault(\Promise|\Generator $promise, int $timeout, mixed $default): \Amp\Promise<\TReturn>|\Promise<\TReturnAlt>`
* `toCamelCase(string $input): string`
* `toSnakeCase(string $input): string`
* `toSupergroup(int $id): int`
* `typeEscape(string $type): string`
* `unpackDouble(string $value): float`
* `unpackFileId(string $fileId): mixed`
* `unpackSignedInt(string $value): int`
* `unpackSignedLong(string $value): int`
* `unpackSignedLongString(string|int|array $value): string`
* `unsetEventHandler(bool $disableUpdateHandling): mixed`
* `update2fa(array $params): \Amp\Promise`
* `updateSettings(\danog\MadelineProto\SettingsAbstract $settings): \Amp\Promise`
* `upload(\danog\MadelineProto\FileCallbackInterface|string|array $file, string $fileName, callable $cb, bool $encrypted): \Amp\Promise`
* `uploadEncrypted(\danog\MadelineProto\FileCallbackInterface|string|array $file, string $fileName, callable $cb): \Amp\Promise`
* `uploadFromCallable(mixed $callable, int $size, string $mime, string $fileName, callable $cb, bool $seekable, bool $encrypted): \Amp\Promise`
* `uploadFromStream(mixed $stream, int $size, string $mime, string $fileName, callable $cb, bool $encrypted): \Amp\Promise`
* `uploadFromTgfile(mixed $media, callable $cb, bool $encrypted): \Amp\Promise`
* `uploadFromUrl(string|\danog\MadelineProto\FileCallbackInterface $url, int $size, string $fileName, callable $cb, bool $encrypted): \Amp\Promise`
* `viewSponsoredMessage(int|array $peer): \Amp\Promise Bool`
* `wait(\Generator|\Promise $promise, bool $ignoreSignal): mixed`
* `async(bool $async): void`
* `init(): void`
* `initAsynchronously(): \Generator`
* `inited(): bool`
* `forceInit(bool $inited): void`

## Methods:
### `startAndLoop(string $session, \danog\MadelineProto\SettingsAbstract $settings): void`

Start MadelineProto and the event handler (enables async).
Also initializes error reporting, catching and reporting all errors surfacing from the event loop.

Parameters:

* `$session`: `string` Session name  
* `$settings`: `\danog\MadelineProto\SettingsAbstract` Settings  


#### See also: 
* `\danog\MadelineProto\SettingsAbstract`




### `getReportPeers(): array|string|int`

Get peers where to send error reports.



### `getAPI(): \danog\MadelineProto\MTProto`

Get API instance.


#### See also: 
* `\danog\MadelineProto\MTProto`




### `MTProtoToBotAPI(array $data): \Amp\Promise<array>`

Convert MTProto parameters to bot API parameters.


Parameters:

* `$data`: `array` Data  


#### See also: 
* `\Amp\Promise`




### `MTProtoToTd(mixed $params): \Amp\Promise`

MTProto to TD params.


Parameters:

* `$params`: `mixed` Params  


#### See also: 
* `\Amp\Promise`




### `MTProtoToTdcli(mixed $params): \Amp\Promise`

MTProto to TDCLI params.


Parameters:

* `$params`: `mixed` Params  


#### See also: 
* `\Amp\Promise`




### `acceptCall(array $call): \Amp\Promise`

Accept call.


Parameters:

* `$call`: `array` Call  


#### See also: 
* `\Amp\Promise`




### `acceptSecretChat(array $params): \Amp\Promise`

Accept secret chat.


Parameters:

* `$params`: `array` Secret chat ID  


#### See also: 
* `\Amp\Promise`




### `acceptTos(): \Amp\Promise`

Accept terms of service update.


#### See also: 
* `\Amp\Promise`




### `addUser(array $user): \Amp\Promise`

Add user info.


Parameters:

* `$user`: `array` User info  


#### See also: 
* `\Amp\Promise`




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




### `arr(mixed $params): array`

Create array.


Parameters:

* `$params`: `mixed` Params  



### `base64urlDecode(string $data): string`

base64URL decode.


Parameters:

* `$data`: `string` Data to decode  



### `base64urlEncode(string $data): string`

Base64URL encode.


Parameters:

* `$data`: `string` Data to encode  



### `botAPIToMTProto(array $arguments): \Amp\Promise<array>`

Convert bot API parameters to MTProto parameters.


Parameters:

* `$arguments`: `array` Arguments  


#### See also: 
* `\Amp\Promise`




### `botLogin(string $token): \Amp\Promise`

Login as bot.


Parameters:

* `$token`: `string` Bot token  


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




### `callForkDefer(\Generator|\Promise $promise): void`

Call promise in background, deferring execution.


Parameters:

* `$promise`: `\Generator|\Promise` Promise to resolve  


#### See also: 
* `\Generator`
* `\Promise`




### `callStatus(int $id): mixed`

Get call status.


Parameters:

* `$id`: `int` Call ID  


Fully typed return value:
```
int|\Amp\Promise<int>
```
#### See also: 
* `\Amp\Promise`




### `checkTos(): \Amp\Promise`

Check for terms of service update.


#### See also: 
* `\Amp\Promise`




### `cleanup(): \Amp\Promise`

Cleanup memory and session file.


#### See also: 
* `\Amp\Promise`




### `closeConnection(string $message): void`

Close connection with client, connected via web.


Parameters:

* `$message`: `string` Message  



### `complete2faLogin(string $password): \Amp\Promise`

Complete 2FA login.


Parameters:

* `$password`: `string` Password  


#### See also: 
* `\Amp\Promise`




### `completeCall(array $params): \Amp\Promise`

Complete call handshake.


Parameters:

* `$params`: `array` Params  


#### See also: 
* `\Amp\Promise`




### `completePhoneLogin(string $code): \Amp\Promise`

Complet user login using login code.


Parameters:

* `$code`: `string` Login code  


#### See also: 
* `\Amp\Promise`




### `completeSignup(string $first_name, string $last_name): \Amp\Promise`

Complete signup to Telegram.


Parameters:

* `$first_name`: `string` First name  
* `$last_name`: `string` Last name  


#### See also: 
* `\Amp\Promise`




### `confirmCall(array $params): \Amp\Promise`

Confirm call.


Parameters:

* `$params`: `array` Params  


#### See also: 
* `\Amp\Promise`




### `connectToAllDcs(bool $reconnectAll): \Amp\Promise`

Connects to all datacenters and if necessary creates authorization keys, binds them and writes client info.


Parameters:

* `$reconnectAll`: `bool` Whether to reconnect to all DCs  


#### See also: 
* `\Amp\Promise`




### `declineTos(): \Amp\Promise`

Decline terms of service update.
THIS WILL DELETE YOUR ACCOUNT!

#### See also: 
* `\Amp\Promise`




### `discardCall(array $call, array $reason, array $rating, bool $need_debug): \Amp\Promise`

Discard call.


Parameters:

* `$call`: `array` Call  
* `$reason`: `array`   
* `$rating`: `array` Rating  
* `$need_debug`: `bool` Need debug?  


#### See also: 
* `\Amp\Promise`




### `discardSecretChat(int $chat): \Amp\Promise`

Discard secret chat.


Parameters:

* `$chat`: `int` Secret chat ID  


#### See also: 
* `\Amp\Promise`




### `downloadToBrowser(array|string $messageMedia, callable $cb): \Amp\Promise`

Download file to browser.
Supports HEAD requests and content-ranges for parallel and resumed downloads.

Parameters:

* `$messageMedia`: `array|string` File to download  
* `$cb`: `callable` Status callback (can also use FileCallback)  


#### See also: 
* `\Amp\Promise`




### `downloadToCallable(mixed $messageMedia, callable|\danog\MadelineProto\FileCallbackInterface $callable, callable $cb, bool $seekable, int $offset, int $end, int $part_size): \Amp\Promise`

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
\Amp\Promise<true>
```
#### See also: 
* [`\danog\MadelineProto\FileCallbackInterface`: File callback interface.](../../danog/MadelineProto/FileCallbackInterface.md)
* `\Amp\Promise`




### `downloadToDir(mixed $messageMedia, string|\danog\MadelineProto\FileCallbackInterface $dir, callable $cb): \Amp\Promise`

Download file to directory.


Parameters:

* `$messageMedia`: `mixed` File to download  
* `$dir`: `string|\danog\MadelineProto\FileCallbackInterface` Directory where to download the file  
* `$cb`: `callable` Callback (DEPRECATED, use FileCallbackInterface)  


Fully typed return value:
```
\Amp\Promise<false|string>
```
#### See also: 
* [`\danog\MadelineProto\FileCallbackInterface`: File callback interface.](../../danog/MadelineProto/FileCallbackInterface.md)
* `\Amp\Promise`




### `downloadToFile(mixed $messageMedia, string|\danog\MadelineProto\FileCallbackInterface $file, callable $cb): \Amp\Promise Downloaded file path`

Download file.


Parameters:

* `$messageMedia`: `mixed` File to download  
* `$file`: `string|\danog\MadelineProto\FileCallbackInterface` Downloaded file path  
* `$cb`: `callable` Callback (DEPRECATED, use FileCallbackInterface)  


Return value: Downloaded file path

Fully typed return value:
```
\Amp\Promise<false|string>
```
#### See also: 
* [`\danog\MadelineProto\FileCallbackInterface`: File callback interface.](../../danog/MadelineProto/FileCallbackInterface.md)
* `\Amp\Promise`




### `downloadToResponse(array|string $messageMedia, \ServerRequest $request, callable $cb): \Amp\Promise Returned response`

Download file to amphp/http-server response.
Supports HEAD requests and content-ranges for parallel and resumed downloads.

Parameters:

* `$messageMedia`: `array|string` File to download  
* `$request`: `\ServerRequest` Request  
* `$cb`: `callable` Status callback (can also use FileCallback)  


Return value: Returned response

Fully typed return value:
```
\Amp\Promise<\Amp\Http\Server\Response>
```
#### See also: 
* `\ServerRequest`
* `\Amp\Http\Server\Response`
* `\Amp\Promise`




### `downloadToStream(mixed $messageMedia, mixed|\danog\MadelineProto\FileCallbackInterface $stream, callable $cb, int $offset, int $end): \Amp\Promise`

Download file to stream.


Parameters:

* `$messageMedia`: `mixed` File to download  
* `$stream`: `mixed|\danog\MadelineProto\FileCallbackInterface` Stream where to download file  
* `$cb`: `callable` Callback (DEPRECATED, use FileCallbackInterface)  
* `$offset`: `int` Offset where to start downloading  
* `$end`: `int` Offset where to end download  


Fully typed return value:
```
\Amp\Promise<mixed>
```
#### See also: 
* [`\danog\MadelineProto\FileCallbackInterface`: File callback interface.](../../danog/MadelineProto/FileCallbackInterface.md)
* `\Amp\Promise`




### `echo(string $string): \Amp\Promise`

Asynchronously write to stdout/browser.


Parameters:

* `$string`: `string` Message to echo  


#### See also: 
* `\Amp\Promise`




### `end(array $what): mixed`

Get final element of array.


Parameters:

* `$what`: `array` Array  



### `exportAuthorization(): \Amp\Promise`

Export authorization.


Fully typed return value:
```
\Amp\Promise<array{0: int|string, 1: string}>
```
#### See also: 
* `\Amp\Promise`




### `extractBotAPIFile(array $info): ?array`

Extract file info from bot API message.


Parameters:

* `$info`: `array` Bot API message object  



### `fileGetContents(string $url): \Amp\Promise`

Get contents of remote file asynchronously.


Parameters:

* `$url`: `string` URL  


Fully typed return value:
```
\Amp\Promise<string>
```
#### See also: 
* `\Amp\Promise`




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




### `fromSupergroup(int $id): int`

Convert bot API channel ID to MTProto channel ID.


Parameters:

* `$id`: `int` Bot API channel ID  



### `fullChatLastUpdated(mixed $id): \Amp\Promise<int>`

When were full info for this chat last cached.


Parameters:

* `$id`: `mixed` Chat ID  


#### See also: 
* `\Amp\Promise`




### `fullGetSelf(): \Amp\Promise<array|bool>`

Get info about the logged-in user, not cached.


#### See also: 
* `\Amp\Promise`




### `genVectorHash(array $ints): \string Vector hash`

Generate MTProto vector hash.


Parameters:

* `$ints`: `array` IDs  


Return value: Vector hash


### `getAllMethods(): mixed`

Get full list of MTProto and API methods.


Fully typed return value:
```
array|\Amp\Promise<array>
```
#### See also: 
* `\Amp\Promise`




### `getAuthorization(): mixed`

Get authorization info.


Fully typed return value:
```
int|\Amp\Promise<int>
```
#### See also: 
* `\Amp\Promise`




### `getCachedConfig(): mixed`

Get cached server-side config.


Fully typed return value:
```
array|\Amp\Promise<array>
```
#### See also: 
* `\Amp\Promise`




### `getCall(int $call): mixed`

Get call info.


Parameters:

* `$call`: `int` Call ID  


Fully typed return value:
```
array|\Amp\Promise<array>
```
#### See also: 
* `\Amp\Promise`




### `getCdnConfig(string $datacenter): \Amp\Promise`

Store RSA keys for CDN datacenters.


Parameters:

* `$datacenter`: `string` DC ID  


#### See also: 
* `\Amp\Promise`




### `getConfig(array $config, array $options): \Amp\Promise`

Get cached (or eventually re-fetch) server-side config.


Parameters:

* `$config`: `array` Current config  
* `$options`: `array` Options for method call  


#### See also: 
* `\Amp\Promise`




### `getDNSClient(): mixed`

Get async DNS client.


Fully typed return value:
```
\Amp\Dns\Resolver|\Amp\Promise<\Amp\Dns\Resolver>
```
#### See also: 
* `\Amp\Dns\Resolver`
* `\Amp\Promise`




### `getDataCenterConnections(): mixed`

Get all datacenter connections.


Fully typed return value:
```
array<\danog\MadelineProto\DataCenterConnection>|\Amp\Promise<array<\danog\MadelineProto\DataCenterConnection>>
```
#### See also: 
* `\danog\MadelineProto\DataCenterConnection`
* `\Amp\Promise`




### `getDataCenterId(): int|string`

Get main DC ID.



### `getDialogs(bool $force): \Amp\Promise`

Get dialog peers.


Parameters:

* `$force`: `bool` Whether to refetch all dialogs ignoring cache  


Fully typed return value:
```
\Amp\Promise<list<mixed>>
```
#### See also: 
* `\Amp\Promise`




### `getDownloadInfo(mixed $messageMedia): \Amp\Promise<array>`

Get download info of file
Returns an array with the following structure:.
`$info['ext']` - The file extension
`$info['name']` - The file name, without the extension
`$info['mime']` - The file mime type
`$info['size']` - The file size

Parameters:

* `$messageMedia`: `mixed` File ID  


#### See also: 
* `\Amp\Promise`




### `getEventHandler(): mixed`

Get event handler.


Fully typed return value:
```
\danog\MadelineProto\EventHandler|\Amp\Promise<\danog\MadelineProto\EventHandler>
```
#### See also: 
* [`\danog\MadelineProto\EventHandler`: Event handler.](../../danog/MadelineProto/EventHandler.md)
* `\Amp\Promise`




### `getExtensionFromLocation(mixed $location, string $default): string`

Get extension from file location.


Parameters:

* `$location`: `mixed` File location  
* `$default`: `string` Default extension  



### `getExtensionFromMime(string $mime): string`

Get extension from mime type.


Parameters:

* `$mime`: `string` MIME type  



### `getFileInfo(mixed $constructor): \Amp\Promise<array>`

Get info about file.


Parameters:

* `$constructor`: `mixed` File ID  


#### See also: 
* `\Amp\Promise`




### `getFolderId(mixed $id): ?int`

Get folder ID from object.


Parameters:

* `$id`: `mixed` Object  



### `getFullDialogs(bool $force): \Amp\Promise`

Get full info of all dialogs.


Parameters:

* `$force`: `bool` Whether to refetch all dialogs ignoring cache  


#### See also: 
* `\Amp\Promise`




### `getFullInfo(mixed $id): \Amp\Promise FullInfo object`

Get full info about peer, returns an FullInfo object.


Parameters:

* `$id`: `mixed` Peer  


Return value: FullInfo object

Fully typed return value:
```
\Amp\Promise<array>
```
#### See also: 
* [https://docs.madelineproto.xyz/FullInfo.html](https://docs.madelineproto.xyz/FullInfo.html)
* `\Amp\Promise`




### `getHTTPClient(): mixed`

Get async HTTP client.


Fully typed return value:
```
\Amp\Http\Client\HttpClient|\Amp\Promise<\Amp\Http\Client\HttpClient>
```
#### See also: 
* `\Amp\Http\Client\HttpClient`
* `\Amp\Promise`




### `getHint(): mixed`

Get current password hint.


Fully typed return value:
```
string|\Amp\Promise<string>
```
#### See also: 
* `\Amp\Promise`




### `getId(mixed $id): int`

Get bot API ID from peer object.


Parameters:

* `$id`: `mixed` Peer  



### `getInfo(mixed $id, bool $recursive): \Amp\Promise Info object`

Get info about peer, returns an Info object.


Parameters:

* `$id`: `mixed` Peer  
  Full type:
  ```
  array{_: \TConstructor}|mixed
  ```
* `$recursive`: `bool` Internal  


Return value: Info object

Fully typed return value:
```
\Generator<int|mixed, \Amp\Promise|\Amp\Promise<string>|array, mixed, array{TConstructor: \array
     InputPeer: array{_: string, user_id?: mixed, access_hash?: mixed, min?: mixed, chat_id?: mixed, channel_id?: mixed}, Peer: array{_: string, user_id?: mixed, chat_id?: mixed, channel_id?: mixed}, DialogPeer: array{_: string, peer: array{_: string, user_id?: mixed, chat_id?: mixed, channel_id?: mixed}}, NotifyPeer: array{_: string, peer: array{_: string, user_id?: mixed, chat_id?: mixed, channel_id?: mixed}}, InputDialogPeer: array{_: string, peer: array{_: string, user_id?: mixed, access_hash?: mixed, min?: mixed, chat_id?: mixed, channel_id?: mixed}}, InputNotifyPeer: array{_: string, peer: array{_: string, user_id?: mixed, access_hash?: mixed, min?: mixed, chat_id?: mixed, channel_id?: mixed}}, bot_api_id: int|string, user_id?: int, chat_id?: int, channel_id?: int, InputUser?: array{_: string, user_id?: int, access_hash?: mixed, min?: bool}, InputChannel?: array{_: string, channel_id: int, access_hash: mixed, min: bool}, type: string}>|int|array{_: string, user_id?: mixed, access_hash?: mixed, min?: mixed, chat_id?: mixed, channel_id?: mixed}|array{_: string, user_id?: int, access_hash?: mixed, min?: bool}|array{_: string, channel_id: int, access_hash: mixed, min: bool}
```
#### See also: 
* [https://docs.madelineproto.xyz/Info.html](https://docs.madelineproto.xyz/Info.html)
* `\TConstructor`
* `\Amp\Promise`
* `\Generator`




### `getLogger()`

Get logger.



### `getMethodNamespaces(): mixed`

Get TL namespaces.


Fully typed return value:
```
array|\Amp\Promise<array>
```
#### See also: 
* `\Amp\Promise`




### `getMethodsNamespaced(): mixed`

Get namespaced methods (method => namespace).


Fully typed return value:
```
array|\Amp\Promise<array>
```
#### See also: 
* `\Amp\Promise`




### `getMimeFromBuffer(string $buffer): string`

Get mime type from buffer.


Parameters:

* `$buffer`: `string` Buffer  



### `getMimeFromExtension(string $extension, string $default): string`

Get mime type from file extension.


Parameters:

* `$extension`: `string` File extension  
* `$default`: `string` Default mime type  



### `getMimeFromFile(string $file): string`

Get mime type of file.


Parameters:

* `$file`: `string` File  



### `getPropicInfo(mixed $messageMedia): \Amp\Promise<array>`

Get download info of the propic of a user
Returns an array with the following structure:.
`$info['ext']` - The file extension
`$info['name']` - The file name, without the extension
`$info['mime']` - The file mime type
`$info['size']` - The file size

Parameters:

* `$messageMedia`: `mixed` File ID  


#### See also: 
* `\Amp\Promise`




### `getPsrLogger()`

Get PSR logger.



### `getPwrChat(mixed $id): \Amp\Promise Chat object`

Get full info about peer (including full list of channel members), returns a Chat object.


Parameters:

* `$id`: `mixed` Peer  


Return value: Chat object

#### See also: 
* [https://docs.madelineproto.xyz/Chat.html](https://docs.madelineproto.xyz/Chat.html)




### `getSecretChat(array|int $chat): mixed`

Get secret chat.


Parameters:

* `$chat`: `array|int` Secret chat ID  


Fully typed return value:
```
array|\Amp\Promise<array>
```
#### See also: 
* `\Amp\Promise`




### `getSelf(): mixed`

Get info about the logged-in user, cached.
Use fullGetSelf to bypass the cache.

Fully typed return value:
```
array|false|\Amp\Promise<array|false>
```
#### See also: 
* `\Amp\Promise`




### `getSettings(): mixed`

Return current settings.


Fully typed return value:
```
\danog\MadelineProto\Settings|\Amp\Promise<\danog\MadelineProto\Settings>
```
#### See also: 
* [`\danog\MadelineProto\Settings`: Settings class used for configuring MadelineProto.](../../danog/MadelineProto/Settings.md)
* `\Amp\Promise`




### `getSponsoredMessages(int|array $peer): \Amp\Promise`

Get sponsored messages for channel.
This method will return an array of [sponsored message objects](https://docs.madelineproto.xyz/API_docs/constructors/sponsoredMessage.html).

See [the API documentation](https://core.telegram.org/api/sponsored-messages) for more info on how to handle sponsored messages.

Parameters:

* `$peer`: `int|array` Channel ID, or Update, or Message, or Peer.  


#### See also: 
* `\Amp\Promise`




### `getTL(): mixed`

Get TL serializer.


Fully typed return value:
```
\danog\MadelineProto\TL\TL|\Amp\Promise<\danog\MadelineProto\TL\TL>
```
#### See also: 
* `\danog\MadelineProto\TL\TL`
* `\Amp\Promise`




### `getVar(object $obj, string $var): mixed`

Accesses a private variable from an object.


Parameters:

* `$obj`: `object` Object  
* `$var`: `string` Attribute name  



### `getWebMessage(string $message)`

Get a message to show to the user when starting the bot.


Parameters:

* `$message`: `string`   



### `getWebTemplate(): mixed`

Get web template.


Fully typed return value:
```
string|\Amp\Promise<string>
```
#### See also: 
* `\Amp\Promise`




### `hasAllAuth(): mixed`

Checks whether all datacenters are authorized.


Fully typed return value:
```
bool|\Amp\Promise<bool>
```
#### See also: 
* `\Amp\Promise`




### `hasEventHandler(): mixed`

Check if an event handler instance is present.


Fully typed return value:
```
bool|\Amp\Promise<bool>
```
#### See also: 
* `\Amp\Promise`




### `hasReportPeers(): mixed`

Check if has report peers.


Fully typed return value:
```
bool|\Amp\Promise<bool>
```
#### See also: 
* `\Amp\Promise`




### `hasSecretChat(array|int $chat): mixed`

Check whether secret chat exists.


Parameters:

* `$chat`: `array|int` Secret chat ID  


Fully typed return value:
```
bool|\Amp\Promise<bool>
```
#### See also: 
* `\Amp\Promise`




### `hasVar(object $obj, string $var): bool`

Checks private property exists in an object.


Parameters:

* `$obj`: `object` Object  
* `$var`: `string` Attribute name  



### `importAuthorization(array<int, string> $authorization, int $mainDcID): \Amp\Promise`

Import authorization.


Parameters:

* `$authorization`: `array<int, string>` Authorization info  
* `$mainDcID`: `int` Main DC ID  


#### See also: 
* `\Amp\Promise`




### `inflateStripped(string $stripped): \string JPG payload`

Inflate stripped photosize to full JPG payload.


Parameters:

* `$stripped`: `string` Stripped photosize  


Return value: JPG payload


### `initSelfRestart(): mixed`

Initialize self-restart hack.


Fully typed return value:
```
void|\Amp\Promise<void>
```
#### See also: 
* `\Amp\Promise`




### `isAltervista(): bool`

Whether this is altervista.



### `isArrayOrAlike(mixed $var): bool`

Check if is array or similar (traversable && countable && arrayAccess).


Parameters:

* `$var`: `mixed` Value to check  



### `isIpc(): mixed`

Whether we're an IPC client instance.


Fully typed return value:
```
bool|\Amp\Promise<bool>
```
#### See also: 
* `\Amp\Promise`




### `isIpcWorker(): mixed`

Whether we're an IPC server process (as opposed to an event handler).


Fully typed return value:
```
bool|\Amp\Promise<bool>
```
#### See also: 
* `\Amp\Promise`




### `isPremium()`

Returns whether the current user is a premium user, cached.



### `isSupergroup(int $id): bool`

Check whether provided bot API ID is a channel.


Parameters:

* `$id`: `int` Bot API ID  



### `logger(string $param, int $level, string $file): mixed`

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




### `logout(): \Amp\Promise`

Log out currently logged in user.


#### See also: 
* `\Amp\Promise`




### `loop(callable|null $callback): \Amp\Promise`

Start MadelineProto's update handling loop, or run the provided async callable.


Parameters:

* `$callback`: `callable|null` Async callable to run  


#### See also: 
* `\Amp\Promise`




### `loopFork(): \Amp\Promise`

Start MadelineProto's update handling loop in background.


#### See also: 
* `\Amp\Promise`




### `markdownEscape(string $hwat): string`

Escape string for markdown.


Parameters:

* `$hwat`: `string` String to escape  



### `mbStrSplit(string $text, int $length): array`

Telegram UTF-8 multibyte split.


Parameters:

* `$text`: `string` Text  
* `$length`: `int` Length  



### `mbStrlen(string $text): float|int`

Get Telegram UTF-8 length of string.


Parameters:

* `$text`: `string` Text  



### `mbSubstr(string $text, int $offset, ?int $length): string`

Telegram UTF-8 multibyte substring.


Parameters:

* `$text`: `string` Text to substring  
* `$offset`: `int` Offset  
* `$length`: `?int` Length  



### `methodCall(string $method, array|\Generator $args, array $aargs): \Amp\Promise`

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
* `\Amp\Promise`




### `methodCallWrite(string $method, array|\Generator $args, array $aargs): \Amp\Promise`

Call method and make sure it is asynchronously sent.


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
* `\Amp\Promise`




### `methodEscape(string $method): string`

Escape method name.


Parameters:

* `$method`: `string` Method name  



### `packDouble(float $value): string`

Convert double to binary version.


Parameters:

* `$value`: `float` Value to convert  



### `packSignedInt(int $value): string`

Convert integer to base256 signed int.


Parameters:

* `$value`: `int` Value to convert  



### `packSignedLong(int $value): string`

Convert integer to base256 long.


Parameters:

* `$value`: `int` Value to convert  



### `packUnsignedInt(int $value): string`

Convert value to unsigned base256 int.


Parameters:

* `$value`: `int` Value  



### `peerIsset(mixed $id): \Amp\Promise`

Check if peer is present in internal peer database.


Parameters:

* `$id`: `mixed` Peer  


Fully typed return value:
```
\Amp\Promise<bool>
```
#### See also: 
* `\Amp\Promise`




### `phoneLogin(string $number, int $sms_type): \Amp\Promise`

Login as user.


Parameters:

* `$number`: `string` Phone number  
* `$sms_type`: `int` SMS type  


#### See also: 
* `\Amp\Promise`




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


### `randomInt(int $modulus): int`

Get random integer.


Parameters:

* `$modulus`: `int` Modulus  



### `readLine(string $prompt): \Amp\Promise<string>`

Asynchronously read line.


Parameters:

* `$prompt`: `string` Prompt  


#### See also: 
* `\Amp\Promise`




### `refreshFullPeerCache(mixed $id): \Amp\Promise`

Refresh full peer cache for a certain peer.


Parameters:

* `$id`: `mixed` The peer to refresh  


#### See also: 
* `\Amp\Promise`




### `refreshPeerCache(mixed $id): \Amp\Promise`

Refresh peer cache for a certain peer.


Parameters:

* `$id`: `mixed` The peer to refresh  


#### See also: 
* `\Amp\Promise`




### `rekey(int $chat): \Amp\Promise`

Rekey secret chat.


Parameters:

* `$chat`: `int` Secret chat to rekey  


#### See also: 
* `\Amp\Promise`




### `report(string $message, string $parseMode): \Amp\Promise`

Report an error to the previously set peer.


Parameters:

* `$message`: `string` Error to report  
* `$parseMode`: `string` Parse mode  


#### See also: 
* `\Amp\Promise`




### `requestCall(mixed $user): \Amp\Promise`

Request VoIP call.


Parameters:

* `$user`: `mixed` User  


#### See also: 
* `\Amp\Promise`




### `requestSecretChat(mixed $user): \Amp\Promise`

Request secret chat.


Parameters:

* `$user`: `mixed` User to start secret chat with  


#### See also: 
* `\Amp\Promise`




### `resetUpdateState(): mixed`

Reset the update state and fetch all updates from the beginning.


Fully typed return value:
```
void|\Amp\Promise<void>
```
#### See also: 
* `\Amp\Promise`




### `resolveUsername(string $username): \Amp\Promise`

Resolve username (use getInfo instead).


Parameters:

* `$username`: `string` Username  


#### See also: 
* `\Amp\Promise`




### `restart(): void`

Restart update loop.



### `rethrow(\Throwable $e, string $file): void`

Rethrow error catched in strand.


Parameters:

* `$e`: `\Throwable` Exception  
* `$file`: `string` File where the strand started  


#### See also: 
* `\Throwable`




### `rleDecode(string $string): string`

null-byte RLE decode.


Parameters:

* `$string`: `string` Data to decode  



### `rleEncode(string $string): string`

null-byte RLE encode.


Parameters:

* `$string`: `string` Data to encode  



### `secretChatStatus(int $chat): mixed`

Get secret chat status.


Parameters:

* `$chat`: `int` Chat ID  


Fully typed return value:
```
int|\Amp\Promise<int>
```
#### See also: 
* `\Amp\Promise`




### `serializeAll(): void`

Serialize all instances.
CALLED ONLY ON SHUTDOWN.


### `setCallback(callable $callback): mixed`

Set update handling callback.


Parameters:

* `$callback`: `callable` Callback  


Fully typed return value:
```
void|\Amp\Promise<void>
```
#### See also: 
* `\Amp\Promise`




### `setEventHandler(class-string<\danog\MadelineProto\EventHandler> $eventHandler): \Amp\Promise`

Set event handler.


Parameters:

* `$eventHandler`: `class-string<\danog\MadelineProto\EventHandler>` Event handler  


#### See also: 
* [`\danog\MadelineProto\EventHandler`: Event handler.](../../danog/MadelineProto/EventHandler.md)
* `\Amp\Promise`




### `setNoop(): mixed`

Set NOOP update handler, ignoring all updates.


Fully typed return value:
```
void|\Amp\Promise<void>
```
#### See also: 
* `\Amp\Promise`




### `setReportPeers(int|string $userOrId): \Amp\Promise`

Set peer(s) where to send errors occurred in the event loop.


Parameters:

* `$userOrId`: `int|string` Username(s) or peer ID(s)  


#### See also: 
* `\Amp\Promise`




### `setVar(object $obj, string $var, mixed $val): void`

Sets a private variable in an object.


Parameters:

* `$obj`: `object` Object  
* `$var`: `string` Attribute name  
* `$val`: `mixed` Attribute value  



### `setWebTemplate(string $template): mixed`

Set web template.


Parameters:

* `$template`: `string` Template  


Fully typed return value:
```
void|\Amp\Promise<void>
```
#### See also: 
* `\Amp\Promise`




### `setWebhook(string $hook_url, string $pem_path): mixed`

Set webhook update handler.


Parameters:

* `$hook_url`: `string` Webhook URL  
* `$pem_path`: `string` PEM path for self-signed certificate  


Fully typed return value:
```
void|\Amp\Promise<void>
```
#### See also: 
* `\Amp\Promise`




### `setupLogger(): mixed`

Setup logger.


Fully typed return value:
```
void|\Amp\Promise<void>
```
#### See also: 
* `\Amp\Promise`




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




### `start(): \Amp\Promise`

Log in to telegram (via CLI or web).


#### See also: 
* `\Amp\Promise`




### `stop(): void`

Stop update loop.



### `tdToMTProto(array $params): \Amp\Promise<array>`

Convert TD to MTProto parameters.


Parameters:

* `$params`: `array` Parameters  


#### See also: 
* `\Amp\Promise`




### `tdToTdcli(mixed $params): mixed`

Convert TD parameters to tdcli.


Parameters:

* `$params`: `mixed` Parameters  



### `tdcliToTd(array $params, array $key): mixed`

Convert tdcli parameters to tdcli.


Parameters:

* `$params`: `array` Params  
* `$key`: `array` Key  


Fully typed return value:
```
array|\Amp\Promise<array>
```
#### See also: 
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




### `timeoutWithDefault(\Promise|\Generator $promise, int $timeout, mixed $default): \Amp\Promise<\TReturn>|\Promise<\TReturnAlt>`

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
* `$default`: `mixed`   
  Full type:
  ```
  \TReturnAlt
  ```


#### See also: 
* `\Promise`
* `\Generator`
* `\TReturn`
* `\TGenerator`
* `\TReturnAlt`
* `\Amp\Promise`




### `toCamelCase(string $input): string`

Convert to camelCase.


Parameters:

* `$input`: `string` String  



### `toSnakeCase(string $input): string`

Convert to snake_case.


Parameters:

* `$input`: `string` String  



### `toSupergroup(int $id): int`

Convert MTProto channel ID to bot API channel ID.


Parameters:

* `$id`: `int` MTProto channel ID  



### `typeEscape(string $type): string`

Escape type name.


Parameters:

* `$type`: `string` String to escape  



### `unpackDouble(string $value): float`

Unpack binary double.


Parameters:

* `$value`: `string` Value to unpack  



### `unpackFileId(string $fileId): mixed`

Unpack bot API file ID.


Parameters:

* `$fileId`: `string` Bot API file ID  


Fully typed return value:
```
array|\Amp\Promise<array>
```
#### See also: 
* `\Amp\Promise`




### `unpackSignedInt(string $value): int`

Unpack base256 signed int.


Parameters:

* `$value`: `string` base256 int  



### `unpackSignedLong(string $value): int`

Unpack base256 signed long.


Parameters:

* `$value`: `string` base256 long  



### `unpackSignedLongString(string|int|array $value): string`

Unpack base256 signed long to string.


Parameters:

* `$value`: `string|int|array` base256 long  



### `unsetEventHandler(bool $disableUpdateHandling): mixed`

Unset event handler.


Parameters:

* `$disableUpdateHandling`: `bool` Whether to also disable internal update handling (will cause errors, otherwise will simply use the NOOP handler)  


Fully typed return value:
```
void|\Amp\Promise<void>
```
#### See also: 
* `\Amp\Promise`




### `update2fa(array $params): \Amp\Promise`

Update the 2FA password.
The params array can contain password, new_password, email and hint params.

Parameters:

* `$params`: `array` The params  


#### See also: 
* `\Amp\Promise`




### `updateSettings(\danog\MadelineProto\SettingsAbstract $settings): \Amp\Promise`

Parse, update and store settings.


Parameters:

* `$settings`: `\danog\MadelineProto\SettingsAbstract` Settings  


#### See also: 
* `\danog\MadelineProto\SettingsAbstract`
* `\Amp\Promise`




### `upload(\danog\MadelineProto\FileCallbackInterface|string|array $file, string $fileName, callable $cb, bool $encrypted): \Amp\Promise`

Upload file.


Parameters:

* `$file`: `\danog\MadelineProto\FileCallbackInterface|string|array` File, URL or Telegram file to upload  
* `$fileName`: `string` File name  
* `$cb`: `callable` Callback (DEPRECATED, use FileCallbackInterface)  
* `$encrypted`: `bool` Whether to encrypt file for secret chats  


Fully typed return value:
```
\Amp\Promise<mixed>
```
#### See also: 
* [`\danog\MadelineProto\FileCallbackInterface`: File callback interface.](../../danog/MadelineProto/FileCallbackInterface.md)
* `\Amp\Promise`




### `uploadEncrypted(\danog\MadelineProto\FileCallbackInterface|string|array $file, string $fileName, callable $cb): \Amp\Promise`

Upload file to secret chat.


Parameters:

* `$file`: `\danog\MadelineProto\FileCallbackInterface|string|array` File, URL or Telegram file to upload  
* `$fileName`: `string` File name  
* `$cb`: `callable` Callback (DEPRECATED, use FileCallbackInterface)  


Fully typed return value:
```
\Amp\Promise<mixed>
```
#### See also: 
* [`\danog\MadelineProto\FileCallbackInterface`: File callback interface.](../../danog/MadelineProto/FileCallbackInterface.md)
* `\Amp\Promise`




### `uploadFromCallable(mixed $callable, int $size, string $mime, string $fileName, callable $cb, bool $seekable, bool $encrypted): \Amp\Promise`

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
\Amp\Promise<array{_: string, id: string, parts: int, name: string, mime_type: string, key_fingerprint?: mixed, key?: mixed, iv?: mixed, md5_checksum: string}>
```
#### See also: 
* `\Amp\Promise`




### `uploadFromStream(mixed $stream, int $size, string $mime, string $fileName, callable $cb, bool $encrypted): \Amp\Promise`

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
\Amp\Promise<mixed>
```
#### See also: 
* `\Amp\Promise`




### `uploadFromTgfile(mixed $media, callable $cb, bool $encrypted): \Amp\Promise`

Reupload telegram file.


Parameters:

* `$media`: `mixed` Telegram file  
* `$cb`: `callable` Callback (DEPRECATED, use FileCallbackInterface)  
* `$encrypted`: `bool` Whether to encrypt file for secret chats  


Fully typed return value:
```
\Amp\Promise<mixed>
```
#### See also: 
* `\Amp\Promise`




### `uploadFromUrl(string|\danog\MadelineProto\FileCallbackInterface $url, int $size, string $fileName, callable $cb, bool $encrypted): \Amp\Promise`

Upload file from URL.


Parameters:

* `$url`: `string|\danog\MadelineProto\FileCallbackInterface` URL of file  
* `$size`: `int` Size of file  
* `$fileName`: `string` File name  
* `$cb`: `callable` Callback (DEPRECATED, use FileCallbackInterface)  
* `$encrypted`: `bool` Whether to encrypt file for secret chats  


Fully typed return value:
```
\Amp\Promise<mixed>
```
#### See also: 
* [`\danog\MadelineProto\FileCallbackInterface`: File callback interface.](../../danog/MadelineProto/FileCallbackInterface.md)
* `\Amp\Promise`




### `viewSponsoredMessage(int|array $peer): \Amp\Promise Bool`

Mark sponsored message as read.


Parameters:

* `$peer`: `int|array` Channel ID, or Update, or Message, or Peer.  


Return value: Bool


### `wait(\Generator|\Promise $promise, bool $ignoreSignal): mixed`

Synchronously wait for a promise|generator.


Parameters:

* `$promise`: `\Generator|\Promise` The promise to wait for  
* `$ignoreSignal`: `bool` Whether to ignore shutdown signals  


#### See also: 
* `\Generator`
* `\Promise`




### `async(bool $async): void`

Enable or disable async.


Parameters:

* `$async`: `bool` Whether to enable or disable async  



### `init(): void`

Blockingly init.



### `initAsynchronously(): \Generator`

Asynchronously init.


#### See also: 
* `\Generator`




### `inited(): bool`

Check if we've already inited.



### `forceInit(bool $inited): void`

Mark instance as (de)inited forcefully.


Parameters:

* `$inited`: `bool` Whether to mark the instance as inited or deinited  



---
Generated by [danog/phpdoc](https://phpdoc.daniil.it)
