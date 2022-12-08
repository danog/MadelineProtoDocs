---
title: "danog\\MadelineProto\\Settings\\Connection: Connection settings."
description: ""
image: "https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png"
parent: "MadelineProto API"

---
# `danog\MadelineProto\Settings\Connection`
[Back to index](../../../index.html)

> Author: Daniil Gentili <daniil@daniil.it>  
  

Connection settings.  




## Method list:
* `getProtocol()`
* `setProtocol(class-string<\danog\MadelineProto\Stream\MTProtoBufferInterface> $protocol)`
* `getIpv6()`
* `setIpv6(bool $ipv6)`
* `getSslSubdomains()`
* `setSslSubdomains(array $sslSubdomains)`
* `getMinMediaSocketCount()`
* `setMinMediaSocketCount(int $minMediaSocketCount)`
* `getMaxMediaSocketCount()`
* `setMaxMediaSocketCount(int $maxMediaSocketCount)`
* `getRobinPeriod()`
* `setRobinPeriod(int $robinPeriod)`
* `getDefaultDc()`
* `getDefaultDcParams()`
* `setDefaultDc(int $defaultDc)`
* `getProxies()`
* `addProxy(class-string<\danog\MadelineProto\Stream\StreamInterface> $proxy, array $extra)`
* `setProxy(array $proxies)`
* `clearProxies()`
* `removeProxy()`
* `getObfuscated()`
* `setObfuscated(bool $obfuscated)`
* `getTestMode()`
* `setTestMode(bool $testMode)`
* `getTransport(): class-string<\danog\MadelineProto\Stream\RawStreamInterface>`
* `setTransport(class-string<\danog\MadelineProto\Stream\RawStreamInterface> $transport)`
* `getRetry()`
* `setRetry(bool $retry)`
* `getTimeout()`
* `setTimeout(int $timeout)`
* `getPingInterval()`
* `setPingInterval(int $pingInterval)`
* `getUseDoH()`
* `setUseDoH(bool $useDoH)`
* `getBindTo(): ?string`
* `setBindTo(?string $bindTo)`

## Methods:
### `getProtocol()`

Get protocol identifier.



### `setProtocol(class-string<\danog\MadelineProto\Stream\MTProtoBufferInterface> $protocol)`

Set protocol identifier.
Available MTProto transport protocols (smaller overhead is better):

* `\danog\MadelineProto\Stream\MTProtoTransport\AbridgedStream`: Lightest protocol available
  * Overhead: Very small
  * Minimum envelope length: 1 byte (length)
  * Maximum envelope length: 4 bytes (length)

* `\danog\MadelineProto\Stream\MTProtoTransport\IntermediateStream`: I guess they like having multiple protocols
  * Overhead: small
  * Minimum envelope length: 4 bytes (length)
  * Maximum envelope length: 4 bytes (length)

* `\danog\MadelineProto\Stream\MTProtoTransport\IntermediatePaddedStream`: Padded version of the intermediate protocol, to use with obfuscation enabled to bypass ISP blocks
  * Overhead: small-medium
  * Minimum envelope length: random
  * Maximum envelope length: random

* `\danog\MadelineProto\Stream\MTProtoTransport\FullStream`: The basic MTProto transport protocol
  * Overhead: medium
  * Minimum envelope length: 12 bytes (length+seqno+crc)
  * Maximum envelope length: 12 bytes (length+seqno+crc)
  * Pros:
    * Initial integrity check with crc32
    * Transport sequence number check

  * Cons:
    * Initial integrity check with crc32 is not that useful since the TCP protocol already uses it internally
    * Transport sequence number check is also not that useful since transport sequence numbers are not encrypted and thus cannot be used to avoid replay attacks, and MadelineProto already uses MTProto sequence numbers and message ids for that.

* `\danog\MadelineProto\Stream\MTProtoTransport\HttpStream`: MTProto over HTTP for browsers and webhosts
  * Overhead: medium
  * Pros:
    * Can be used on restricted webhosts or browsers
  * Cons:
    * Very big envelope length

* `\danog\MadelineProto\Stream\MTProtoTransport\HttpsStream`: MTProto over HTTPS for browsers and webhosts, very secure
  * Overhead: high
  * Pros:
    * Can be used on restricted webhosts or browsers
    * Provides an additional layer of security by trasmitting data over TLS
    * Integrity checks with HMAC built into TLS
    * Sequence number checks built into TLS
  * Cons:
    * Very big envelope length
    * Requires an additional round of encryption

Parameters:

* `$protocol`: `class-string<\danog\MadelineProto\Stream\MTProtoBufferInterface>` Protocol identifier  


#### See also: 
* `\danog\MadelineProto\Stream\MTProtoBufferInterface`




### `getIpv6()`

Get whether to use ipv6.



### `setIpv6(bool $ipv6)`

Set whether to use ipv6.


Parameters:

* `$ipv6`: `bool` Whether to use ipv6  



### `getSslSubdomains()`

Get subdomains of web.telegram.org for https protocol.



### `setSslSubdomains(array $sslSubdomains)`

Set subdomains of web.telegram.org for https protocol.


Parameters:

* `$sslSubdomains`: `array` Subdomains of web.telegram.org for https protocol.  



### `getMinMediaSocketCount()`

Get minimum media socket count.



### `setMinMediaSocketCount(int $minMediaSocketCount)`

Set minimum media socket count.


Parameters:

* `$minMediaSocketCount`: `int` Minimum media socket count.  



### `getMaxMediaSocketCount()`

Get maximum media socket count.



### `setMaxMediaSocketCount(int $maxMediaSocketCount)`

Set maximum media socket count.


Parameters:

* `$maxMediaSocketCount`: `int` Maximum media socket count.  



### `getRobinPeriod()`

Get robin period (seconds).



### `setRobinPeriod(int $robinPeriod)`

Set robin period (seconds).


Parameters:

* `$robinPeriod`: `int` Robin period (seconds).  



### `getDefaultDc()`

Get default DC ID.



### `getDefaultDcParams()`

Get default DC params.



### `setDefaultDc(int $defaultDc)`

Set default DC ID.


Parameters:

* `$defaultDc`: `int` Default DC ID.  



### `getProxies()`

Get proxy identifiers.


Fully typed return value:
```
array<class-string<\danog\MadelineProto\Stream\StreamInterface>, array>
```
#### See also: 
* `\danog\MadelineProto\Stream\StreamInterface`




### `addProxy(class-string<\danog\MadelineProto\Stream\StreamInterface> $proxy, array $extra)`

Add proxy identifier to list, one of:.
* `\danog\MadelineProto\Stream\MTProtoTransport\ObfuscatedStream::class`
* `\danog\MadelineProto\Stream\Proxy\HttpProxy::class`
* `\danog\MadelineProto\Stream\Proxy\SocksProxy::class`

Parameters:

* `$proxy`: `class-string<\danog\MadelineProto\Stream\StreamInterface>` Proxy identifier  
* `$extra`: `array` Extra  


#### See also: 
* `\danog\MadelineProto\Stream\StreamInterface`




### `setProxy(array $proxies)`

Set proxies.


Parameters:

* `$proxies`: `array` Proxies  



### `clearProxies()`

Clear proxies.



### `removeProxy()`

Remove specific proxy pair.



### `getObfuscated()`

Get whether to use the obfuscated protocol: useful to bypass ISP blocks.



### `setObfuscated(bool $obfuscated)`

Set whether to use the obfuscated protocol: useful to bypass ISP blocks.


Parameters:

* `$obfuscated`: `bool` Whether to use the obfuscated protocol.  



### `getTestMode()`

Get whether we're in test mode.



### `setTestMode(bool $testMode)`

Set whether we're in test mode.


Parameters:

* `$testMode`: `bool` Whether we're in test mode.  



### `getTransport(): class-string<\danog\MadelineProto\Stream\RawStreamInterface>`

Get transport identifier.


#### See also: 
* `\danog\MadelineProto\Stream\RawStreamInterface`




### `setTransport(class-string<\danog\MadelineProto\Stream\RawStreamInterface> $transport)`

Sets the transport protocol to use when connecting to telegram.
Not supported by HTTP and HTTPS protocols, obfuscation must be enabled.

* `danog\MadelineProto\Stream\Transport`: Default TCP transport
* `danog\MadelineProto\Stream\WsTransport`: Plain websocket transport
* `danog\MadelineProto\Stream\WssTransport`: TLS websocket transport

Parameters:

* `$transport`: `class-string<\danog\MadelineProto\Stream\RawStreamInterface>` Transport identifier.  


#### See also: 
* `\danog\MadelineProto\Stream\RawStreamInterface`




### `getRetry()`

Get whether to retry connection.



### `setRetry(bool $retry)`

Set whether to retry connection.


Parameters:

* `$retry`: `bool` Whether to retry connection.  



### `getTimeout()`

Get connection timeout.



### `setTimeout(int $timeout)`

Set connection timeout.


Parameters:

* `$timeout`: `int` Connection timeout.  



### `getPingInterval()`

Get ping interval.



### `setPingInterval(int $pingInterval)`

Set ping interval.


Parameters:

* `$pingInterval`: `int` Ping interval  



### `getUseDoH()`

Get whether to use DNS over HTTPS.



### `setUseDoH(bool $useDoH)`

Set whether to use DNS over HTTPS.


Parameters:

* `$useDoH`: `bool` Whether to use DNS over HTTPS  



### `getBindTo(): ?string`

Get bind on specific address and port.



### `setBindTo(?string $bindTo)`

Set bind on specific address and port.


Parameters:

* `$bindTo`: `?string` Bind on specific address and port.  



---
Generated by [danog/phpdoc](https://phpdoc.daniil.it)
