---
title: danog\MadelineProto\Stream\ConnectionContext: Connection context class.
description: Is responsible for maintaining state about a certain connection to a DC.
That includes the Stream chain that is required to use the connection, the connection URI, and other connection-related data.

---
# `danog\MadelineProto\Stream\ConnectionContext`
[Back to index](../../../index.md)

> Author: Daniil Gentili <daniil@daniil.it>  
  

Connection context class.  

Is responsible for maintaining state about a certain connection to a DC.
That includes the Stream chain that is required to use the connection, the connection URI, and other connection-related data.


## Method list:
* `setSocketContext(\Amp\Socket\ConnectContext $socketContext): self`
* `getSocketContext(): \Amp\Socket\ConnectContext`
* `setUri(string|\Psr\Http\Message\UriInterface $uri): self`
* `getStringUri(): string`
* `getUri(): \Psr\Http\Message\UriInterface`
* `setCancellationToken(\Amp\CancellationToken $cancellationToken): self`
* `getCancellationToken(): \Amp\CancellationToken`
* `getCtx(): self`
* `setTest(bool $test): self`
* `isTest(): bool`
* `isMedia(): bool`
* `isCDN(): bool`
* `isDns(): bool`
* `setIsDns(bool $isDns): self`
* `secure(bool $secure): self`
* `isSecure(): bool`
* `setDc(string|int $dc): self`
* `getDc(): string|int`
* `getIntDc(): string|int`
* `setIpv6(bool $ipv6): self`
* `getIpv6(): bool`
* `addStream(string $streamName, mixed $extra): self`
* `setReadCallback(callable $callable): void`
* `hasReadCallback(): bool`
* `getReadCallback(): callable`
* `getStreamName(): string`
* `hasStreamName(string $stream): bool`
* `getStream(): \Generator<\danog\MadelineProto\Stream\StreamInterface>`
* `getInputClientProxy(): array`
* `getName(): string`

## Methods:
### `setSocketContext(\Amp\Socket\ConnectContext $socketContext): self`

Set the socket context.


Parameters:
* `$socketContext`: `\Amp\Socket\ConnectContext`   


#### See also: 
* `\Amp\Socket\ConnectContext`




### `getSocketContext(): \Amp\Socket\ConnectContext`

Get the socket context.


#### See also: 
* `\Amp\Socket\ConnectContext`




### `setUri(string|\Psr\Http\Message\UriInterface $uri): self`

Set the connection URI.


Parameters:
* `$uri`: `string|\Psr\Http\Message\UriInterface`   


#### See also: 
* `\Psr\Http\Message\UriInterface`




### `getStringUri(): string`

Get the URI as a string.



### `getUri(): \Psr\Http\Message\UriInterface`

Get the URI.


#### See also: 
* `\Psr\Http\Message\UriInterface`




### `setCancellationToken(\Amp\CancellationToken $cancellationToken): self`

Set the cancellation token.


Parameters:
* `$cancellationToken`: `\Amp\CancellationToken`   


#### See also: 
* `\Amp\CancellationToken`




### `getCancellationToken(): \Amp\CancellationToken`

Get the cancellation token.


#### See also: 
* `\Amp\CancellationToken`




### `getCtx(): self`

Return a clone of the current connection context.



### `setTest(bool $test): self`

Set the test boolean.


Parameters:
* `$test`: `bool`   



### `isTest(): bool`

Whether this is a test connection.



### `isMedia(): bool`

Whether this is a media connection.



### `isCDN(): bool`

Whether this is a CDN connection.



### `isDns(): bool`

Whether this connection context will only be used by the DNS client.



### `setIsDns(bool $isDns): self`

Whether this connection context will only be used by the DNS client.


Parameters:
* `$isDns`: `bool`   



### `secure(bool $secure): self`

Set the secure boolean.


Parameters:
* `$secure`: `bool`   



### `isSecure(): bool`

Whether to use TLS with socket connections.



### `setDc(string|int $dc): self`

Set the DC ID.


Parameters:
* `$dc`: `string|int`   



### `getDc(): string|int`

Get the DC ID.



### `getIntDc(): string|int`

Get the int DC ID.



### `setIpv6(bool $ipv6): self`

Whether to use ipv6.


Parameters:
* `$ipv6`: `bool`   



### `getIpv6(): bool`

Whether to use ipv6.



### `addStream(string $streamName, mixed $extra): self`

Add a stream to the stream chain.


Parameters:
* `$streamName`: `string`   
  Full type:
  ```
  class-string
  ```
* `$extra`: `mixed`   



### `setReadCallback(callable $callable): void`

Set read callback, called every time the socket reads at least a byte.


Parameters:
* `$callable`: `callable` Read callback  



### `hasReadCallback(): bool`

Check if a read callback is present.



### `getReadCallback(): callable`

Get read callback.



### `getStreamName(): string`

Get the current stream name from the stream chain.



### `hasStreamName(string $stream): bool`

Check if has stream within stream chain.


Parameters:
* `$stream`: `string` Stream name  



### `getStream(): \Generator<\danog\MadelineProto\Stream\StreamInterface>`

Get a stream from the stream chain.


#### See also: 
* [`\danog\MadelineProto\Stream\StreamInterface`: Generic stream interface.](./StreamInterface.md)
* `\Generator`




### `getInputClientProxy(): array`

Get the inputClientProxy proxy MTProto object.



### `getName(): string`

Get a description "name" of the context.



---
Generated by [danog/phpdoc](https://phpdoc.daniil.it)
