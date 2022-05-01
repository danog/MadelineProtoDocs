---
title: "danog\\MadelineProto\\Settings\\Connection: Connection settings."
description: ""
image: "https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png"
parent: "MadelineProto API"

---
# `danog\MadelineProto\Settings\Connection`
[Back to index](../../../index.md)

> Author: Daniil Gentili <daniil@daniil.it>  
  

Connection settings.  




## Method list:
* `getProtocol(): string`
* `setProtocol(class-string<\danog\MadelineProto\Stream\MTProtoBufferInterface> $protocol): self`
* `getIpv6(): bool`
* `setIpv6(bool $ipv6): self`
* `getSslSubdomains(): array`
* `setSslSubdomains(array $sslSubdomains): self`
* `getMinMediaSocketCount(): int`
* `setMinMediaSocketCount(int $minMediaSocketCount): self`
* `getMaxMediaSocketCount(): int`
* `setMaxMediaSocketCount(int $maxMediaSocketCount): self`
* `getRobinPeriod(): int`
* `setRobinPeriod(int $robinPeriod): self`
* `getDefaultDc(): int`
* `getDefaultDcParams(): array`
* `setDefaultDc(int $defaultDc): self`
* `getProxies(): array`
* `addProxy(class-string<\danog\MadelineProto\Stream\StreamInterface> $proxy, array $extra): self`
* `setProxy(array $proxies): self`
* `clearProxies(): self`
* `removeProxy(string $proxy, array $extra): self`
* `getObfuscated(): bool`
* `setObfuscated(bool $obfuscated): self`
* `getTestMode(): bool`
* `setTestMode(bool $testMode): self`
* `getTransport(): class-string<\danog\MadelineProto\Stream\RawStreamInterface>`
* `setTransport(class-string<\danog\MadelineProto\Stream\RawStreamInterface> $transport): self`
* `getRetry(): bool`
* `setRetry(bool $retry): self`
* `getTimeout(): int`
* `setTimeout(int $timeout): self`
* `getPingInterval(): int`
* `setPingInterval(int $pingInterval): self`
* `getUseDoH(): bool`
* `setUseDoH(bool $useDoH): self`
* `getBindTo(): ?string`
* `setBindTo(?string $bindTo): self`

## Methods:
### `getProtocol(): string`

Get protocol identifier.



### `setProtocol(class-string<\danog\MadelineProto\Stream\MTProtoBufferInterface> $protocol): self`

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




### `getIpv6(): bool`

Get whether to use ipv6.



### `setIpv6(bool $ipv6): self`

Set whether to use ipv6.


Parameters:

* `$ipv6`: `bool` Whether to use ipv6  



### `getSslSubdomains(): array`

Get subdomains of web.telegram.org for https protocol.



### `setSslSubdomains(array $sslSubdomains): self`

Set subdomains of web.telegram.org for https protocol.


Parameters:

* `$sslSubdomains`: `array` Subdomains of web.telegram.org for https protocol.  



### `getMinMediaSocketCount(): int`

Get minimum media socket count.



### `setMinMediaSocketCount(int $minMediaSocketCount): self`

Set minimum media socket count.


Parameters:

* `$minMediaSocketCount`: `int` Minimum media socket count.  



### `getMaxMediaSocketCount(): int`

Get maximum media socket count.



### `setMaxMediaSocketCount(int $maxMediaSocketCount): self`

Set maximum media socket count.


Parameters:

* `$maxMediaSocketCount`: `int` Maximum media socket count.  



### `getRobinPeriod(): int`

Get robin period (seconds).



### `setRobinPeriod(int $robinPeriod): self`

Set robin period (seconds).


Parameters:

* `$robinPeriod`: `int` Robin period (seconds).  



### `getDefaultDc(): int`

Get default DC ID.



### `getDefaultDcParams(): array`

Get default DC params.



### `setDefaultDc(int $defaultDc): self`

Set default DC ID.


Parameters:

* `$defaultDc`: `int` Default DC ID.  



### `getProxies(): array`

Get proxy identifiers.


Fully typed return value:
```
array<class-string<\danog\MadelineProto\Stream\StreamInterface>, array>
```
#### See also: 
* `\danog\MadelineProto\Stream\StreamInterface`




### `addProxy(class-string<\danog\MadelineProto\Stream\StreamInterface> $proxy, array $extra): self`

Add proxy identifier to list, one of:.
* `\danog\MadelineProto\Stream\MTProtoTransport\ObfuscatedStream::class`
* `\danog\MadelineProto\Stream\Proxy\HttpProxy::class`
* `\danog\MadelineProto\Stream\Proxy\SocksProxy::class`

Parameters:

* `$proxy`: `class-string<\danog\MadelineProto\Stream\StreamInterface>` Proxy identifier  
* `$extra`: `array` Extra  


#### See also: 
* `\danog\MadelineProto\Stream\StreamInterface`




### `setProxy(array $proxies): self`

Set proxies.


Parameters:

* `$proxies`: `array` Proxies  



### `clearProxies(): self`

Clear proxies.



### `removeProxy(string $proxy, array $extra): self`

Remove specific proxy pair.


Parameters:

* `$proxy`: `string`   
* `$extra`: `array`   



### `getObfuscated(): bool`

Get whether to use the obfuscated protocol: useful to bypass ISP blocks.



### `setObfuscated(bool $obfuscated): self`

Set whether to use the obfuscated protocol: useful to bypass ISP blocks.


Parameters:

* `$obfuscated`: `bool` Whether to use the obfuscated protocol.  



### `getTestMode(): bool`

Get whether we're in test mode.



### `setTestMode(bool $testMode): self`

Set whether we're in test mode.


Parameters:

* `$testMode`: `bool` Whether we're in test mode.  



### `getTransport(): class-string<\danog\MadelineProto\Stream\RawStreamInterface>`

Get transport identifier.


#### See also: 
* `\danog\MadelineProto\Stream\RawStreamInterface`




### `setTransport(class-string<\danog\MadelineProto\Stream\RawStreamInterface> $transport): self`

Sets the transport protocol to use when connecting to telegram.
Not supported by HTTP and HTTPS protocols, obfuscation must be enabled.

* `danog\MadelineProto\Stream\Transport`: Default TCP transport
* `danog\MadelineProto\Stream\WsTransport`: Plain websocket transport
* `danog\MadelineProto\Stream\WssTransport`: TLS websocket transport

Parameters:

* `$transport`: `class-string<\danog\MadelineProto\Stream\RawStreamInterface>` Transport identifier.  


#### See also: 
* `\danog\MadelineProto\Stream\RawStreamInterface`




### `getRetry(): bool`

Get whether to retry connection.



### `setRetry(bool $retry): self`

Set whether to retry connection.


Parameters:

* `$retry`: `bool` Whether to retry connection.  



### `getTimeout(): int`

Get connection timeout.



### `setTimeout(int $timeout): self`

Set connection timeout.


Parameters:

* `$timeout`: `int` Connection timeout.  



### `getPingInterval(): int`

Get ping interval.



### `setPingInterval(int $pingInterval): self`

Set ping interval.


Parameters:

* `$pingInterval`: `int` Ping interval  



### `getUseDoH(): bool`

Get whether to use DNS over HTTPS.



### `setUseDoH(bool $useDoH): self`

Set whether to use DNS over HTTPS.


Parameters:

* `$useDoH`: `bool` Whether to use DNS over HTTPS  



### `getBindTo(): ?string`

Get bind on specific address and port.



### `setBindTo(?string $bindTo): self`

Set bind on specific address and port.


Parameters:

* `$bindTo`: `?string` Bind on specific address and port.  



---
Generated by [danog/phpdoc](https://phpdoc.daniil.it)
