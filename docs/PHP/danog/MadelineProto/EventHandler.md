---
title: "danog\\MadelineProto\\EventHandler: Event handler."
description: ""
image: "https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png"
parent: "MadelineProto API"

---
# `danog\MadelineProto\EventHandler`
[Back to index](../../index.html)

> Author: Daniil Gentili <daniil@daniil.it>  
  

Event handler.  




## Method list:
* `startAndLoop(string $session, \danog\MadelineProto\SettingsAbstract $settings)`
* `startAndLoopBot(string $session, string $token, \danog\MadelineProto\SettingsAbstract $settings)`
* `getReportPeers(): string|int|(string|int)[]`
* `MTProtoToBotAPI(array $data)`
* `MTProtoToTd(mixed $params)`
* `MTProtoToTdcli(mixed $params)`
* `acceptCall(array $call)`
* `acceptSecretChat(array $params)`
* `addUser(array $user)`
* `arr(mixed $params)`
* `base64urlDecode(string $data)`
* `base64urlEncode(string $data)`
* `botAPIToMTProto(array $arguments)`
* `botLogin(string $token)`
* `broadcastCustom(\Action $action)`
* `broadcastForwardMessages(mixed $from_peer, list<int> $message_ids, bool $drop_author)`
* `broadcastMessages(array $messages)`
* `callStatus(int $id)`
* `cancelBroadcast(int $id)`
* `closeConnection(string $message)`
* `complete2faLogin(string $password)`
* `completeCall(array $params)`
* `completePhoneLogin(string $code)`
* `completeSignup(string $first_name, string $last_name)`
* `confirmCall(array $params)`
* `connectToAllDcs(bool $reconnectAll)`
* `discardCall(array $call, array $rating, bool $need_debug)`
* `discardSecretChat(int $chat)`
* `downloadToBrowser(array|string|\danog\MadelineProto\FileCallbackInterface $messageMedia, null|callable $cb, null|int $size, null|string $mime, null|string $name)`
* `downloadToCallable(mixed $messageMedia, callable|\danog\MadelineProto\FileCallbackInterface $callable, callable $cb, bool $seekable, int $offset, int $end, int $part_size)`
* `downloadToDir(mixed $messageMedia, string|\danog\MadelineProto\FileCallbackInterface $dir, callable $cb)`
* `downloadToFile(mixed $messageMedia, string|\danog\MadelineProto\FileCallbackInterface $file, callable $cb)`
* `downloadToResponse(array|string|\danog\MadelineProto\FileCallbackInterface $messageMedia, \Amp\Http\Server\Request $request, callable $cb, null|int $size, null|string $name, null|string $mime)`
* `downloadToStream(mixed $messageMedia, mixed|\danog\MadelineProto\FileCallbackInterface|\resource|\Amp\ByteStream\WritableStream $stream, callable $cb, int $offset, int $end)`
* `echo(string $string)`
* `end(array $what)`
* `exportAuthorization(): array{0: int|string, 1: string}`
* `extractBotAPIFile(array $info)`
* `extractMessage()`
* `extractMessageId()`
* `extractMessageUpdate()`
* `extractUpdates(): array[]`
* `fileGetContents(string $url)`
* `flock(string $file, int $operation, float $polling, ?\Amp\Cancellation $token, ?\Closure $failureCb): mixed`
* `fromSupergroup(int $id)`
* `fullChatLastUpdated(mixed $id)`
* `fullGetSelf()`
* `genVectorHash(array $ints): \string Vector hash`
* `getAllMethods()`
* `getAuthorization()`
* `getBroadcastProgress(int $id)`
* `getCachedConfig()`
* `getCall(int $call)`
* `getCdnConfig()`
* `getConfig(array $config)`
* `getDNSClient()`
* `getDhConfig()`
* `getDialogIds(): list<int>`
* `getDialogs(): list<array>`
* `getDownloadInfo(mixed $messageMedia)`
* `getEventHandler()`
* `getExtensionFromLocation(mixed $location, string $default)`
* `getExtensionFromMime(string $mime)`
* `getFileInfo(mixed $constructor)`
* `getFolderId(mixed $id)`
* `getFullDialogs(): array<int, array>`
* `getFullInfo(mixed $id)`
* `getHTTPClient()`
* `getHint()`
* `getId(mixed $id)`
* `getInfo(mixed $id, \MTProto::INFO_TYPE_* $type): mixed`
* `getLogger()`
* `getMaps()`
* `getMaxMaps()`
* `getMethodNamespaces()`
* `getMethodsNamespaced()`
* `getMimeFromBuffer(string $buffer)`
* `getMimeFromExtension(string $extension, string $default)`
* `getMimeFromFile(string $file)`
* `getPropicInfo()`
* `getPsrLogger()`
* `getPwrChat(mixed $id)`
* `getSecretChat(array|int $chat)`
* `getSelf()`
* `getSessionName()`
* `getSettings()`
* `getSponsoredMessages(int|string|array $peer)`
* `getTL()`
* `getType(mixed $id): \"user"|\"bot"|\"chat"|\"supergroup"|\"channel"`
* `getUpdates(array{offset?: int, limit?: int, timeout?: float} $params): list<array{update_id: mixed, update: mixed}>`
* `getVar(object $obj, string $var)`
* `getWebMessage()`
* `getWebTemplate()`
* `hasAllAuth()`
* `hasEventHandler()`
* `hasReportPeers()`
* `hasSecretChat(array|int $chat)`
* `hasVar(object $obj, string $var)`
* `importAuthorization(array<int, string> $authorization, int $mainDcID)`
* `inflateStripped(string $stripped): \string JPG payload`
* `initSelfRestart()`
* `isAltervista()`
* `isArrayOrAlike(mixed $var)`
* `isIpc()`
* `isIpcWorker()`
* `isPremium()`
* `isSupergroup(int $id)`
* `logger(mixed $param, int $level, string $file)`
* `markdownEscape(string $hwat)`
* `mbStrSplit(string $text, int $length): string[]`
* `mbStrlen(string $text)`
* `mbSubstr(string $text, int $offset, null|int $length)`
* `methodEscape(string $method)`
* `packDouble(float $value)`
* `packSignedInt(int $value)`
* `packSignedLong(int $value)`
* `packUnsignedInt(int $value)`
* `peerIsset(mixed $id)`
* `phoneLogin(string $number, int $sms_type)`
* `posmod(int $a, int $b): \int Modulo`
* `random(int $length): \string Random string`
* `randomInt(int $modulus)`
* `readLine(string $prompt)`
* `refreshFullPeerCache(mixed $id)`
* `refreshPeerCache()`
* `rekey(int $chat)`
* `report(string $message, string $parseMode)`
* `requestCall(mixed $user)`
* `requestSecretChat(mixed $user)`
* `resetUpdateState()`
* `restart()`
* `rethrow()`
* `rleDecode(string $string)`
* `rleEncode(string $string)`
* `secretChatStatus(int $chat): \int One of MTProto::SECRET_EMPTY, MTProto::SECRET_REQUESTED, MTProto::SECRET_READY`
* `sendCustomEvent()`
* `setNoop()`
* `setReportPeers(int|string|(int|string)[] $userOrId)`
* `setVar(object $obj, string $var, mixed $val)`
* `setWebTemplate(string $template)`
* `setWebhook(string $webhookUrl)`
* `setupLogger()`
* `sleep(float $time)`
* `start()`
* `stop()`
* `subscribeToUpdates(mixed $channel): \bool False if we were already subscribed`
* `tdToMTProto(array $params)`
* `tdToTdcli(mixed $params)`
* `tdcliToTd(mixed $params, array $key)`
* `testFibers(): array{maxFibers: int, realMemoryMb: int, maps: ?int, maxMaps: ?int}`
* `toCamelCase(string $input)`
* `toSnakeCase(string $input)`
* `toSupergroup(int $id)`
* `typeEscape(string $type)`
* `unpackDouble(string $value)`
* `unpackFileId(string $fileId): \array Unpacked file ID`
* `unpackSignedInt(string $value)`
* `unpackSignedLong(string $value)`
* `unpackSignedLongString(string|int|array $value)`
* `unsetEventHandler()`
* `update2fa(array{password?: string, new_password?: string, email?: string, hint?: string} $params)`
* `updateSettings(\danog\MadelineProto\SettingsAbstract $settings)`
* `upload(\danog\MadelineProto\FileCallbackInterface|string|array $file, string $fileName, callable $cb, bool $encrypted)`
* `uploadEncrypted(\danog\MadelineProto\FileCallbackInterface|string|array $file, string $fileName, callable $cb)`
* `uploadFromCallable(mixed $callable, int $size, string $mime, string $fileName, callable $cb, bool $seekable, bool $encrypted)`
* `uploadFromStream(mixed $stream, int $size, string $mime, string $fileName, callable $cb, bool $encrypted)`
* `uploadFromTgfile(mixed $media, callable $cb, bool $encrypted)`
* `uploadFromUrl(string|\danog\MadelineProto\FileCallbackInterface $url, int $size, string $fileName, callable $cb, bool $encrypted)`
* `viewSponsoredMessage(int|array $peer, string|array{random_id: string} $message)`

## Methods:
### `startAndLoop(string $session, \danog\MadelineProto\SettingsAbstract $settings)`

Start MadelineProto and the event handler.
Also initializes error reporting, catching and reporting all errors surfacing from the event loop.

Parameters:

* `$session`: `string` Session name  
* `$settings`: `\danog\MadelineProto\SettingsAbstract` Settings  


#### See also: 
* `\danog\MadelineProto\SettingsAbstract`




### `startAndLoopBot(string $session, string $token, \danog\MadelineProto\SettingsAbstract $settings)`

Start MadelineProto as a bot and the event handler.
Also initializes error reporting, catching and reporting all errors surfacing from the event loop.

Parameters:

* `$session`: `string` Session name  
* `$token`: `string` Bot token  
* `$settings`: `\danog\MadelineProto\SettingsAbstract` Settings  


#### See also: 
* `\danog\MadelineProto\SettingsAbstract`




### `getReportPeers(): string|int|(string|int)[]`

Get peers where to send error reports.



### `MTProtoToBotAPI(array $data)`

Convert MTProto parameters to bot API parameters.


Parameters:

* `$data`: `array` Data  



### `MTProtoToTd(mixed $params)`

MTProto to TD params.


Parameters:

* `$params`: `mixed` Params  



### `MTProtoToTdcli(mixed $params)`

MTProto to TDCLI params.


Parameters:

* `$params`: `mixed` Params  



### `acceptCall(array $call)`

Accept call.


Parameters:

* `$call`: `array` Call  



### `acceptSecretChat(array $params)`

Accept secret chat.


Parameters:

* `$params`: `array` Secret chat ID  



### `addUser(array $user)`

Add user info.


Parameters:

* `$user`: `array` User info  



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



### `botAPIToMTProto(array $arguments)`

Convert bot API parameters to MTProto parameters.


Parameters:

* `$arguments`: `array` Arguments  



### `botLogin(string $token)`

Login as bot.


Parameters:

* `$token`: `string` Bot token  



### `broadcastCustom(\Action $action)`

Executes a custom broadcast action with all peers (users, chats, channels) of the bot.
Will return an integer ID that can be used to:

- Get the current broadcast progress with getBroadcastProgress
- Cancel the broadcast using cancelBroadcast

Note that to avoid manually polling the progress,
MadelineProto will also periodically emit updateBroadcastProgress updates,
containing a Progress object for all broadcasts currently in-progress.

Parameters:

* `$action`: `\Action` A custom, serializable Action class that will be called once for every peer.  


#### See also: 
* `\Action`




### `broadcastForwardMessages(mixed $from_peer, list<int> $message_ids, bool $drop_author)`

Forwards a list of messages to all peers (users, chats, channels) of the bot.
Will return an integer ID that can be used to:

- Get the current broadcast progress with getBroadcastProgress
- Cancel the broadcast using cancelBroadcast

Note that to avoid manually polling the progress,
MadelineProto will also periodically emit updateBroadcastProgress updates,
containing a Progress object for all broadcasts currently in-progress.

Parameters:

* `$from_peer`: `mixed` Bot API ID or Update, from where to forward the messages.  
* `$message_ids`: `list<int>` IDs of the messages to forward.  
* `$drop_author`: `bool` If true, will forward messages without quoting the original author.  



### `broadcastMessages(array $messages)`

Sends a list of messages to all peers (users, chats, channels) of the bot.
A simplified version of this method is also available: broadcastForwardMessages can work with pre-prepared messages.

Will return an integer ID that can be used to:

- Get the current broadcast progress with getBroadcastProgress
- Cancel the broadcast using cancelBroadcast

Note that to avoid manually polling the progress,
MadelineProto will also periodically emit updateBroadcastProgress updates,
containing a Progress object for all broadcasts currently in-progress.

Parameters:

* `$messages`: `array` The messages to send: an array of arrays, containing parameters to pass to messages.sendMessage.  



### `callStatus(int $id)`

Get call status.


Parameters:

* `$id`: `int` Call ID  



### `cancelBroadcast(int $id)`

Cancel a running broadcast.


Parameters:

* `$id`: `int` Broadcast ID  



### `closeConnection(string $message)`

Close connection with client, connected via web.


Parameters:

* `$message`: `string` Message  



### `complete2faLogin(string $password)`

Complete 2FA login.


Parameters:

* `$password`: `string` Password  



### `completeCall(array $params)`

Complete call handshake.


Parameters:

* `$params`: `array` Params  



### `completePhoneLogin(string $code)`

Complet user login using login code.


Parameters:

* `$code`: `string` Login code  



### `completeSignup(string $first_name, string $last_name)`

Complete signup to Telegram.


Parameters:

* `$first_name`: `string` First name  
* `$last_name`: `string` Last name  



### `confirmCall(array $params)`

Confirm call.


Parameters:

* `$params`: `array` Params  



### `connectToAllDcs(bool $reconnectAll)`

Connects to all datacenters and if necessary creates authorization keys, binds them and writes client info.


Parameters:

* `$reconnectAll`: `bool` Whether to reconnect to all DCs  



### `discardCall(array $call, array $rating, bool $need_debug)`

Discard call.


Parameters:

* `$call`: `array` Call  
* `$rating`: `array` Rating  
* `$need_debug`: `bool` Need debug?  



### `discardSecretChat(int $chat)`

Discard secret chat.


Parameters:

* `$chat`: `int` Secret chat ID  



### `downloadToBrowser(array|string|\danog\MadelineProto\FileCallbackInterface $messageMedia, null|callable $cb, null|int $size, null|string $mime, null|string $name)`

Download file to browser.
Supports HEAD requests and content-ranges for parallel and resumed downloads.

Parameters:

* `$messageMedia`: `array|string|\danog\MadelineProto\FileCallbackInterface` File to download  
* `$cb`: `null|callable` Status callback (can also use FileCallback)  
* `$size`: `null|int` Size of file to download, required for bot API file IDs.  
* `$mime`: `null|string` MIME type of file to download, required for bot API file IDs.  
* `$name`: `null|string` Name of file to download, required for bot API file IDs.  


#### See also: 
* [`\danog\MadelineProto\FileCallbackInterface`: File callback interface.](../../danog/MadelineProto/FileCallbackInterface.html)




### `downloadToCallable(mixed $messageMedia, callable|\danog\MadelineProto\FileCallbackInterface $callable, callable $cb, bool $seekable, int $offset, int $end, int $part_size)`

Download file to callable.
The callable must accept two parameters: string $payload, int $offset
The callable will be called (possibly out of order, depending on the value of $seekable).

Parameters:

* `$messageMedia`: `mixed` File to download  
* `$callable`: `callable|\danog\MadelineProto\FileCallbackInterface` Chunk callback  
* `$cb`: `callable` Status callback (DEPRECATED, use FileCallbackInterface)  
* `$seekable`: `bool` Whether the callable can be called out of order  
* `$offset`: `int` Offset where to start downloading  
* `$end`: `int` Offset where to stop downloading (inclusive)  
* `$part_size`: `int` Size of each chunk  


#### See also: 
* [`\danog\MadelineProto\FileCallbackInterface`: File callback interface.](../../danog/MadelineProto/FileCallbackInterface.html)




### `downloadToDir(mixed $messageMedia, string|\danog\MadelineProto\FileCallbackInterface $dir, callable $cb)`

Download file to directory.


Parameters:

* `$messageMedia`: `mixed` File to download  
* `$dir`: `string|\danog\MadelineProto\FileCallbackInterface` Directory where to download the file  
* `$cb`: `callable` Callback (DEPRECATED, use FileCallbackInterface)  


#### See also: 
* [`\danog\MadelineProto\FileCallbackInterface`: File callback interface.](../../danog/MadelineProto/FileCallbackInterface.html)




### `downloadToFile(mixed $messageMedia, string|\danog\MadelineProto\FileCallbackInterface $file, callable $cb)`

Download file.


Parameters:

* `$messageMedia`: `mixed` File to download  
* `$file`: `string|\danog\MadelineProto\FileCallbackInterface` Downloaded file path  
* `$cb`: `callable` Callback (DEPRECATED, use FileCallbackInterface)  


#### See also: 
* [`\danog\MadelineProto\FileCallbackInterface`: File callback interface.](../../danog/MadelineProto/FileCallbackInterface.html)




### `downloadToResponse(array|string|\danog\MadelineProto\FileCallbackInterface $messageMedia, \Amp\Http\Server\Request $request, callable $cb, null|int $size, null|string $name, null|string $mime)`

Download file to amphp/http-server response.
Supports HEAD requests and content-ranges for parallel and resumed downloads.

Parameters:

* `$messageMedia`: `array|string|\danog\MadelineProto\FileCallbackInterface` File to download  
* `$request`: `\Amp\Http\Server\Request` Request  
* `$cb`: `callable` Status callback (can also use FileCallback)  
* `$size`: `null|int` Size of file to download, required for bot API file IDs.  
* `$name`: `null|string` Name of file to download, required for bot API file IDs.  
* `$mime`: `null|string` MIME type of file to download, required for bot API file IDs.  


#### See also: 
* [`\danog\MadelineProto\FileCallbackInterface`: File callback interface.](../../danog/MadelineProto/FileCallbackInterface.html)
* `\Amp\Http\Server\Request`




### `downloadToStream(mixed $messageMedia, mixed|\danog\MadelineProto\FileCallbackInterface|\resource|\Amp\ByteStream\WritableStream $stream, callable $cb, int $offset, int $end)`

Download file to stream.


Parameters:

* `$messageMedia`: `mixed` File to download  
* `$stream`: `mixed|\danog\MadelineProto\FileCallbackInterface|\resource|\Amp\ByteStream\WritableStream` Stream where to download file  
* `$cb`: `callable` Callback (DEPRECATED, use FileCallbackInterface)  
* `$offset`: `int` Offset where to start downloading  
* `$end`: `int` Offset where to end download  


#### See also: 
* [`\danog\MadelineProto\FileCallbackInterface`: File callback interface.](../../danog/MadelineProto/FileCallbackInterface.html)
* `\resource`
* `\Amp\ByteStream\WritableStream`




### `echo(string $string)`

Asynchronously write to stdout/browser.


Parameters:

* `$string`: `string` Message to echo  



### `end(array $what)`

Get final element of array.


Parameters:

* `$what`: `array` Array  



### `exportAuthorization(): array{0: int|string, 1: string}`

Export authorization.



### `extractBotAPIFile(array $info)`

Extract file info from bot API message.


Parameters:

* `$info`: `array` Bot API message object  



### `extractMessage()`

Extract a message constructor from an Updates constructor.



### `extractMessageId()`

Extract a message ID from an Updates constructor.



### `extractMessageUpdate()`

Extract an update message constructor from an Updates constructor.



### `extractUpdates(): array[]`

Extract Update constructors from an Updates constructor.



### `fileGetContents(string $url)`

Get contents of remote file asynchronously.


Parameters:

* `$url`: `string` URL  



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




### `fromSupergroup(int $id)`

Convert bot API channel ID to MTProto channel ID.


Parameters:

* `$id`: `int` Bot API channel ID  



### `fullChatLastUpdated(mixed $id)`

When were full info for this chat last cached.


Parameters:

* `$id`: `mixed` Chat ID  



### `fullGetSelf()`

Get info about the logged-in user, not cached.



### `genVectorHash(array $ints): \string Vector hash`

Generate MTProto vector hash.


Parameters:

* `$ints`: `array` IDs  


Return value: Vector hash


### `getAllMethods()`

Get full list of MTProto and API methods.



### `getAuthorization()`

Get authorization info.



### `getBroadcastProgress(int $id)`

Get the progress of a currently running broadcast.
Will return null if the broadcast doesn't exist, has already completed or was cancelled.

Use updateBroadcastProgress updates to get real-time progress status without polling.

Parameters:

* `$id`: `int` Broadcast ID  



### `getCachedConfig()`

Get cached server-side config.



### `getCall(int $call)`

Get call info.


Parameters:

* `$call`: `int` Call ID  



### `getCdnConfig()`

Store RSA keys for CDN datacenters.



### `getConfig(array $config)`

Get cached (or eventually re-fetch) server-side config.


Parameters:

* `$config`: `array` Current config  



### `getDNSClient()`

Get async DNS client.



### `getDhConfig()`

Get diffie-hellman configuration.



### `getDialogIds(): list<int>`

Get dialog IDs.



### `getDialogs(): list<array>`

Get dialog peers.



### `getDownloadInfo(mixed $messageMedia)`

Get download info of file
Returns an array with the following structure:.
`$info['ext']` - The file extension
`$info['name']` - The file name, without the extension
`$info['mime']` - The file mime type
`$info['size']` - The file size

Parameters:

* `$messageMedia`: `mixed` File ID  



### `getEventHandler()`

Get event handler.



### `getExtensionFromLocation(mixed $location, string $default)`

Get extension from file location.


Parameters:

* `$location`: `mixed` File location  
* `$default`: `string` Default extension  



### `getExtensionFromMime(string $mime)`

Get extension from mime type.


Parameters:

* `$mime`: `string` MIME type  



### `getFileInfo(mixed $constructor)`

Get info about file.


Parameters:

* `$constructor`: `mixed` File ID  



### `getFolderId(mixed $id)`

Get folder ID from object.


Parameters:

* `$id`: `mixed` Object  



### `getFullDialogs(): array<int, array>`

Get full info of all dialogs.
Bots should use getDialogs or getDialogIds, instead.


### `getFullInfo(mixed $id)`

Get full info about peer, returns an FullInfo object.


Parameters:

* `$id`: `mixed` Peer  


#### See also: 
* [https://docs.madelineproto.xyz/FullInfo.html](https://docs.madelineproto.xyz/FullInfo.html)




### `getHTTPClient()`

Get async HTTP client.



### `getHint()`

Get current password hint.



### `getId(mixed $id)`

Get the bot API ID of a peer.


Parameters:

* `$id`: `mixed` Peer  



### `getInfo(mixed $id, \MTProto::INFO_TYPE_* $type): mixed`

Get info about peer, returns an Info object.


Parameters:

* `$id`: `mixed` Peer  
* `$type`: `\MTProto::INFO_TYPE_*` Whether to generate an Input*, an InputPeer or the full set of constructors  


#### See also: 
* [https://docs.madelineproto.xyz/Info.html](https://docs.madelineproto.xyz/Info.html)




### `getLogger()`

Get logger.



### `getMaps()`

Get current number of memory-mapped regions, UNIX only.



### `getMaxMaps()`

Get maximum number of memory-mapped regions, UNIX only.
Use testFibers to get the maximum number of fibers on any platform.


### `getMethodNamespaces()`

Get TL namespaces.



### `getMethodsNamespaced()`

Get namespaced methods (method => namespace).



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



### `getPropicInfo()`

Get download info of the propic of a user
Returns an array with the following structure:.
`$info['ext']` - The file extension
`$info['name']` - The file name, without the extension
`$info['mime']` - The file mime type
`$info['size']` - The file size


### `getPsrLogger()`

Get PSR logger.



### `getPwrChat(mixed $id)`

Get full info about peer (including full list of channel members), returns a Chat object.


Parameters:

* `$id`: `mixed` Peer  


#### See also: 
* [https://docs.madelineproto.xyz/Chat.html](https://docs.madelineproto.xyz/Chat.html)




### `getSecretChat(array|int $chat)`

Get secret chat.


Parameters:

* `$chat`: `array|int` Secret chat ID  



### `getSelf()`

Get info about the logged-in user, cached.
Use fullGetSelf to bypass the cache.


### `getSessionName()`

Returns the session name.



### `getSettings()`

Return current settings.



### `getSponsoredMessages(int|string|array $peer)`

Get sponsored messages for channel.
This method will return an array of [sponsored message objects](https://docs.madelineproto.xyz/API_docs/constructors/sponsoredMessage.html).

See [the API documentation](https://core.telegram.org/api/sponsored-messages) for more info on how to handle sponsored messages.

Parameters:

* `$peer`: `int|string|array` Channel ID, or Update, or Message, or Peer.  



### `getTL()`

Get TL serializer.



### `getType(mixed $id): \"user"|\"bot"|\"chat"|\"supergroup"|\"channel"`

Get type of peer.


Parameters:

* `$id`: `mixed` Peer  



### `getUpdates(array{offset?: int, limit?: int, timeout?: float} $params): list<array{update_id: mixed, update: mixed}>`

Get updates.


Parameters:

* `$params`: `array{offset?: int, limit?: int, timeout?: float}` Params  



### `getVar(object $obj, string $var)`

Accesses a private variable from an object.


Parameters:

* `$obj`: `object` Object  
* `$var`: `string` Attribute name  



### `getWebMessage()`

Get a message to show to the user when starting the bot.



### `getWebTemplate()`

Get web template.



### `hasAllAuth()`

Checks whether all datacenters are authorized.



### `hasEventHandler()`

Check if an event handler instance is present.



### `hasReportPeers()`

Check if has report peers.



### `hasSecretChat(array|int $chat)`

Check whether secret chat exists.


Parameters:

* `$chat`: `array|int` Secret chat ID  



### `hasVar(object $obj, string $var)`

Checks private property exists in an object.


Parameters:

* `$obj`: `object` Object  
* `$var`: `string` Attribute name  



### `importAuthorization(array<int, string> $authorization, int $mainDcID)`

Import authorization.


Parameters:

* `$authorization`: `array<int, string>` Authorization info  
* `$mainDcID`: `int` Main DC ID  



### `inflateStripped(string $stripped): \string JPG payload`

Inflate stripped photosize to full JPG payload.


Parameters:

* `$stripped`: `string` Stripped photosize  


Return value: JPG payload


### `initSelfRestart()`

Initialize self-restart hack.



### `isAltervista()`

Whether this is altervista.



### `isArrayOrAlike(mixed $var)`

Check if is array or similar (traversable && countable && arrayAccess).


Parameters:

* `$var`: `mixed` Value to check  



### `isIpc()`

Whether we're an IPC client instance.



### `isIpcWorker()`

Whether we're an IPC server process (as opposed to an event handler).



### `isPremium()`

Returns whether the current user is a premium user, cached.



### `isSupergroup(int $id)`

Check whether provided bot API ID is a channel.


Parameters:

* `$id`: `int` Bot API ID  



### `logger(mixed $param, int $level, string $file)`

Logger.


Parameters:

* `$param`: `mixed` Parameter  
* `$level`: `int` Logging level  
* `$file`: `string` File where the message originated  



### `markdownEscape(string $hwat)`

Escape string for markdown.


Parameters:

* `$hwat`: `string` String to escape  



### `mbStrSplit(string $text, int $length): string[]`

Telegram UTF-8 multibyte split.


Parameters:

* `$text`: `string` Text  
* `$length`: `int` Length  



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



### `peerIsset(mixed $id)`

Check if peer is present in internal peer database.


Parameters:

* `$id`: `mixed` Peer  



### `phoneLogin(string $number, int $sms_type)`

Login as user.


Parameters:

* `$number`: `string` Phone number  
* `$sms_type`: `int` SMS type  



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



### `readLine(string $prompt)`

Asynchronously read line.


Parameters:

* `$prompt`: `string` Prompt  



### `refreshFullPeerCache(mixed $id)`

Refresh full peer cache for a certain peer.


Parameters:

* `$id`: `mixed` The peer to refresh  



### `refreshPeerCache()`

Refresh peer cache for a certain peer.



### `rekey(int $chat)`

Rekey secret chat.


Parameters:

* `$chat`: `int` Secret chat to rekey  



### `report(string $message, string $parseMode)`

Report an error to the previously set peer.


Parameters:

* `$message`: `string` Error to report  
* `$parseMode`: `string` Parse mode  



### `requestCall(mixed $user)`

Request VoIP call.


Parameters:

* `$user`: `mixed` User  



### `requestSecretChat(mixed $user)`

Request secret chat.


Parameters:

* `$user`: `mixed` User to start secret chat with  



### `resetUpdateState()`

Reset the update state and fetch all updates from the beginning.



### `restart()`

Restart update loop.



### `rethrow()`

Rethrow exception into event loop.



### `rleDecode(string $string)`

null-byte RLE decode.


Parameters:

* `$string`: `string` Data to decode  



### `rleEncode(string $string)`

null-byte RLE encode.


Parameters:

* `$string`: `string` Data to encode  



### `secretChatStatus(int $chat): \int One of MTProto::SECRET_EMPTY, MTProto::SECRET_REQUESTED, MTProto::SECRET_READY`

Get secret chat status.


Parameters:

* `$chat`: `int` Chat ID  


Return value: One of MTProto::SECRET_EMPTY, MTProto::SECRET_REQUESTED, MTProto::SECRET_READY


### `sendCustomEvent()`

Sends an updateCustomEvent update to the event handler.



### `setNoop()`

Set NOOP update handler, ignoring all updates.



### `setReportPeers(int|string|(int|string)[] $userOrId)`

Set peer(s) where to send errors occurred in the event loop.


Parameters:

* `$userOrId`: `int|string|(int|string)[]` Username(s) or peer ID(s)  



### `setVar(object $obj, string $var, mixed $val)`

Sets a private variable in an object.


Parameters:

* `$obj`: `object` Object  
* `$var`: `string` Attribute name  
* `$val`: `mixed` Attribute value  



### `setWebTemplate(string $template)`

Set web template.


Parameters:

* `$template`: `string` Template  



### `setWebhook(string $webhookUrl)`

Set webhook update handler.


Parameters:

* `$webhookUrl`: `string` Webhook URL  



### `setupLogger()`

Setup logger.



### `sleep(float $time)`

Asynchronously sleep.


Parameters:

* `$time`: `float` Number of seconds to sleep for  



### `start()`

Log in to telegram (via CLI or web).



### `stop()`

Stop update loop.



### `subscribeToUpdates(mixed $channel): \bool False if we were already subscribed`

Subscribe to event handler updates for a channel/supergroup we're not a member of.


Parameters:

* `$channel`: `mixed` Channel/supergroup to subscribe to  


Return value: False if we were already subscribed


### `tdToMTProto(array $params)`

Convert TD to MTProto parameters.


Parameters:

* `$params`: `array` Parameters  



### `tdToTdcli(mixed $params)`

Convert TD parameters to tdcli.


Parameters:

* `$params`: `mixed` Parameters  



### `tdcliToTd(mixed $params, array $key)`

Convert tdcli parameters to tdcli.


Parameters:

* `$params`: `mixed` Params  
* `$key`: `array` Key  



### `testFibers(): array{maxFibers: int, realMemoryMb: int, maps: ?int, maxMaps: ?int}`

Test fibers.



### `toCamelCase(string $input)`

Convert to camelCase.


Parameters:

* `$input`: `string` String  



### `toSnakeCase(string $input)`

Convert to snake_case.


Parameters:

* `$input`: `string` String  



### `toSupergroup(int $id)`

Convert MTProto channel ID to bot API channel ID.


Parameters:

* `$id`: `int` MTProto channel ID  



### `typeEscape(string $type)`

Escape type name.


Parameters:

* `$type`: `string` String to escape  



### `unpackDouble(string $value)`

Unpack binary double.


Parameters:

* `$value`: `string` Value to unpack  



### `unpackFileId(string $fileId): \array Unpacked file ID`

Unpack bot API file ID.


Parameters:

* `$fileId`: `string` Bot API file ID  


Return value: Unpacked file ID


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



### `unsetEventHandler()`

Unset event handler.



### `update2fa(array{password?: string, new_password?: string, email?: string, hint?: string} $params)`

Update the 2FA password.
The params array can contain password, new_password, email and hint params.

Parameters:

* `$params`: `array{password?: string, new_password?: string, email?: string, hint?: string}` The params  



### `updateSettings(\danog\MadelineProto\SettingsAbstract $settings)`

Parse, update and store settings.


Parameters:

* `$settings`: `\danog\MadelineProto\SettingsAbstract` Settings  


#### See also: 
* `\danog\MadelineProto\SettingsAbstract`




### `upload(\danog\MadelineProto\FileCallbackInterface|string|array $file, string $fileName, callable $cb, bool $encrypted)`

Upload file.


Parameters:

* `$file`: `\danog\MadelineProto\FileCallbackInterface|string|array` File, URL or Telegram file to upload  
* `$fileName`: `string` File name  
* `$cb`: `callable` Callback (DEPRECATED, use FileCallbackInterface)  
* `$encrypted`: `bool` Whether to encrypt file for secret chats  


#### See also: 
* [`\danog\MadelineProto\FileCallbackInterface`: File callback interface.](../../danog/MadelineProto/FileCallbackInterface.html)




### `uploadEncrypted(\danog\MadelineProto\FileCallbackInterface|string|array $file, string $fileName, callable $cb)`

Upload file to secret chat.


Parameters:

* `$file`: `\danog\MadelineProto\FileCallbackInterface|string|array` File, URL or Telegram file to upload  
* `$fileName`: `string` File name  
* `$cb`: `callable` Callback (DEPRECATED, use FileCallbackInterface)  


#### See also: 
* [`\danog\MadelineProto\FileCallbackInterface`: File callback interface.](../../danog/MadelineProto/FileCallbackInterface.html)




### `uploadFromCallable(mixed $callable, int $size, string $mime, string $fileName, callable $cb, bool $seekable, bool $encrypted)`

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



### `uploadFromStream(mixed $stream, int $size, string $mime, string $fileName, callable $cb, bool $encrypted)`

Upload file from stream.


Parameters:

* `$stream`: `mixed` PHP resource or AMPHP async stream  
* `$size`: `int` File size  
* `$mime`: `string` Mime type  
* `$fileName`: `string` File name  
* `$cb`: `callable` Callback (DEPRECATED, use FileCallbackInterface)  
* `$encrypted`: `bool` Whether to encrypt file for secret chats  



### `uploadFromTgfile(mixed $media, callable $cb, bool $encrypted)`

Reupload telegram file.


Parameters:

* `$media`: `mixed` Telegram file  
* `$cb`: `callable` Callback (DEPRECATED, use FileCallbackInterface)  
* `$encrypted`: `bool` Whether to encrypt file for secret chats  



### `uploadFromUrl(string|\danog\MadelineProto\FileCallbackInterface $url, int $size, string $fileName, callable $cb, bool $encrypted)`

Upload file from URL.


Parameters:

* `$url`: `string|\danog\MadelineProto\FileCallbackInterface` URL of file  
* `$size`: `int` Size of file  
* `$fileName`: `string` File name  
* `$cb`: `callable` Callback (DEPRECATED, use FileCallbackInterface)  
* `$encrypted`: `bool` Whether to encrypt file for secret chats  


#### See also: 
* [`\danog\MadelineProto\FileCallbackInterface`: File callback interface.](../../danog/MadelineProto/FileCallbackInterface.html)




### `viewSponsoredMessage(int|array $peer, string|array{random_id: string} $message)`

Mark sponsored message as read.


Parameters:

* `$peer`: `int|array` Channel ID, or Update, or Message, or Peer.  
* `$message`: `string|array{random_id: string}` Random ID or sponsored message to mark as read.  



---
Generated by [danog/phpdoc](https://phpdoc.daniil.it)
