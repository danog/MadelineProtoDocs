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
* [`__construct()`](#__construct)
* [`init(): void`](#init)
* [`getProtocol(): string`](#getProtocol)
* [`setProtocol(class-string<\danog\MadelineProto\Stream\MTProtoBufferInterface> $protocol): self`](#setProtocol)
* [`getIpv6(): bool`](#getIpv6)
* [`setIpv6(bool $ipv6): self`](#setIpv6)
* [`getSslSubdomains(): array`](#getSslSubdomains)
* [`setSslSubdomains(array $sslSubdomains): self`](#setSslSubdomains)
* [`getMaxMediaSocketCount(): int`](#getMaxMediaSocketCount)
* [`setMaxMediaSocketCount(int $maxMediaSocketCount): self`](#setMaxMediaSocketCount)
* [`getRobinPeriod(): int`](#getRobinPeriod)
* [`setRobinPeriod(int $robinPeriod): self`](#setRobinPeriod)
* [`getProxies(): array<class-string<\danog\MadelineProto\Stream\StreamInterface>, array>`](#getProxies)
* [`addProxy(class-string<\danog\MadelineProto\Stream\StreamInterface> $proxy, array $extra = []): self`](#addProxy)
* [`setProxies(array<class-string<\danog\MadelineProto\Stream\StreamInterface>, list<array>> $proxies): self`](#setProxies)
* [`clearProxies(): self`](#clearProxies)
* [`removeProxy(string $proxy, array $extra): self`](#removeProxy)
* [`getObfuscated(): bool`](#getObfuscated)
* [`setObfuscated(bool $obfuscated): self`](#setObfuscated)
* [`getTestMode(): bool`](#getTestMode)
* [`setTestMode(bool $testMode): self`](#setTestMode)
* [`getTransport(): class-string<\danog\MadelineProto\Stream\RawStreamInterface>`](#getTransport)
* [`setTransport(class-string<\danog\MadelineProto\Stream\RawStreamInterface> $transport): self`](#setTransport)
* [`getRetry(): bool`](#getRetry)
* [`setRetry(bool $retry): self`](#setRetry)
* [`getTimeout(): float`](#getTimeout)
* [`setTimeout(float $timeout): self`](#setTimeout)
* [`getPingInterval(): int`](#getPingInterval)
* [`setPingInterval(int $pingInterval): self`](#setPingInterval)
* [`getUseDoH(): bool`](#getUseDoH)
* [`setUseDoH(bool $useDoH): self`](#setUseDoH)
* [`getBindTo(): ?string`](#getBindTo)
* [`setBindTo((null|string) $bindTo): self`](#setBindTo)
* [`getRsaKeys(): array`](#getRsaKeys)
* [`setRsaKeys(array $rsaKeys): self`](#setRsaKeys)
* [`getTestRsaKeys(): array`](#getTestRsaKeys)
* [`setTestRsaKeys(array $testRsaKeys): self`](#setTestRsaKeys)

## Methods:
### <a name="__construct"></a> `__construct()`





### <a name="init"></a> `init(): void`





### <a name="getProtocol"></a> `getProtocol(): string`

Get protocol identifier.



### <a name="setProtocol"></a> `setProtocol(class-string<\danog\MadelineProto\Stream\MTProtoBufferInterface> $protocol): self`

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




### <a name="getIpv6"></a> `getIpv6(): bool`

Get whether to use ipv6.



### <a name="setIpv6"></a> `setIpv6(bool $ipv6): self`

Set whether to use ipv6.


Parameters:

* `$ipv6`: `bool` Whether to use ipv6  



### <a name="getSslSubdomains"></a> `getSslSubdomains(): array`

Get subdomains of web.telegram.org for https protocol.



### <a name="setSslSubdomains"></a> `setSslSubdomains(array $sslSubdomains): self`

Set subdomains of web.telegram.org for https protocol.


Parameters:

* `$sslSubdomains`: `array` Subdomains of web.telegram.org for https protocol.  



### <a name="getMaxMediaSocketCount"></a> `getMaxMediaSocketCount(): int`

Get maximum media socket count.



### <a name="setMaxMediaSocketCount"></a> `setMaxMediaSocketCount(int $maxMediaSocketCount): self`

Set maximum media socket count.


Parameters:

* `$maxMediaSocketCount`: `int` Maximum media socket count.  



### <a name="getRobinPeriod"></a> `getRobinPeriod(): int`

Get robin period (seconds).



### <a name="setRobinPeriod"></a> `setRobinPeriod(int $robinPeriod): self`

Set robin period (seconds).


Parameters:

* `$robinPeriod`: `int` Robin period (seconds).  



### <a name="getProxies"></a> `getProxies(): array<class-string<\danog\MadelineProto\Stream\StreamInterface>, array>`

Get proxy identifiers.


#### See also: 
* `\danog\MadelineProto\Stream\StreamInterface`




### <a name="addProxy"></a> `addProxy(class-string<\danog\MadelineProto\Stream\StreamInterface> $proxy, array $extra = []): self`

Add proxy identifier to list, one of:.
  
* `\danog\MadelineProto\Stream\MTProtoTransport\ObfuscatedStream::class`  
* `\danog\MadelineProto\Stream\Proxy\HttpProxy::class`  
* `\danog\MadelineProto\Stream\Proxy\SocksProxy::class`  


Parameters:

* `$proxy`: `class-string<\danog\MadelineProto\Stream\StreamInterface>` Proxy identifier  
* `$extra`: `array` Extra  


#### See also: 
* `\danog\MadelineProto\Stream\StreamInterface`




### <a name="setProxies"></a> `setProxies(array<class-string<\danog\MadelineProto\Stream\StreamInterface>, list<array>> $proxies): self`

Set proxies.
  
The key must be one of:  
  
* `\danog\MadelineProto\Stream\MTProtoTransport\ObfuscatedStream::class`  
* `\danog\MadelineProto\Stream\Proxy\HttpProxy::class`  
* `\danog\MadelineProto\Stream\Proxy\SocksProxy::class`  
  
The value must be a list of extra (URI, username, password) for that proxy.  


Parameters:

* `$proxies`: `array<class-string<\danog\MadelineProto\Stream\StreamInterface>, list<array>>` Proxies  


#### See also: 
* `\danog\MadelineProto\Stream\StreamInterface`




### <a name="clearProxies"></a> `clearProxies(): self`

Clear proxies.



### <a name="removeProxy"></a> `removeProxy(string $proxy, array $extra): self`

Remove specific proxy pair.


Parameters:

* `$proxy`: `string`   
* `$extra`: `array`   



### <a name="getObfuscated"></a> `getObfuscated(): bool`

Get whether to use the obfuscated protocol: useful to bypass ISP blocks.



### <a name="setObfuscated"></a> `setObfuscated(bool $obfuscated): self`

Set whether to use the obfuscated protocol: useful to bypass ISP blocks.


Parameters:

* `$obfuscated`: `bool` Whether to use the obfuscated protocol.  



### <a name="getTestMode"></a> `getTestMode(): bool`

Get whether we're in test mode.



### <a name="setTestMode"></a> `setTestMode(bool $testMode): self`

Set whether we're in test mode.


Parameters:

* `$testMode`: `bool` Whether we're in test mode.  



### <a name="getTransport"></a> `getTransport(): class-string<\danog\MadelineProto\Stream\RawStreamInterface>`

Get transport identifier.


#### See also: 
* `\danog\MadelineProto\Stream\RawStreamInterface`




### <a name="setTransport"></a> `setTransport(class-string<\danog\MadelineProto\Stream\RawStreamInterface> $transport): self`

Sets the transport protocol to use when connecting to telegram.
Not supported by HTTP and HTTPS protocols, obfuscation must be enabled.  
  
* `danog\MadelineProto\Stream\Transport`: Default TCP transport  
* `danog\MadelineProto\Stream\WsTransport`: Plain websocket transport  
* `danog\MadelineProto\Stream\WssTransport`: TLS websocket transport  


Parameters:

* `$transport`: `class-string<\danog\MadelineProto\Stream\RawStreamInterface>` Transport identifier.  


#### See also: 
* `\danog\MadelineProto\Stream\RawStreamInterface`




### <a name="getRetry"></a> `getRetry(): bool`

Get whether to retry connection.



### <a name="setRetry"></a> `setRetry(bool $retry): self`

Set whether to retry connection.


Parameters:

* `$retry`: `bool` Whether to retry connection.  



### <a name="getTimeout"></a> `getTimeout(): float`

Get connection timeout.



### <a name="setTimeout"></a> `setTimeout(float $timeout): self`

Set connection timeout.


Parameters:

* `$timeout`: `float` Connection timeout.  



### <a name="getPingInterval"></a> `getPingInterval(): int`

Get ping interval.



### <a name="setPingInterval"></a> `setPingInterval(int $pingInterval): self`

Set ping interval.


Parameters:

* `$pingInterval`: `int` Ping interval  



### <a name="getUseDoH"></a> `getUseDoH(): bool`

Get whether to use DNS over HTTPS.



### <a name="setUseDoH"></a> `setUseDoH(bool $useDoH): self`

Set whether to use DNS over HTTPS.


Parameters:

* `$useDoH`: `bool` Whether to use DNS over HTTPS  



### <a name="getBindTo"></a> `getBindTo(): ?string`

Get bind on specific address and port.



### <a name="setBindTo"></a> `setBindTo((null|string) $bindTo): self`

Set bind on specific address and port.


Parameters:

* `$bindTo`: `(null|string)` Bind on specific address and port.  



### <a name="getRsaKeys"></a> `getRsaKeys(): array`

Get RSA keys.



### <a name="setRsaKeys"></a> `setRsaKeys(array $rsaKeys): self`

Set RSA keys.


Parameters:

* `$rsaKeys`: `array` RSA keys  



### <a name="getTestRsaKeys"></a> `getTestRsaKeys(): array`

Get test RSA keys.



### <a name="setTestRsaKeys"></a> `setTestRsaKeys(array $testRsaKeys): self`

Set test RSA keys.


Parameters:

* `$testRsaKeys`: `array` Test RSA keys  



---
Generated by [danog/phpdoc](https://phpdoc.daniil.it)
