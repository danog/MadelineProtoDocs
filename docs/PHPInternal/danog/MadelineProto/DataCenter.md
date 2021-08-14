---
title: danog\MadelineProto\DataCenter: Manages datacenters.
description: 

---
# `danog\MadelineProto\DataCenter`
[Back to index](../../index.md)

> Author: Daniil Gentili <daniil@daniil.it>  
  

Manages datacenters.  




## Method list:
* `setDataCenterConnections(array $saved): void`
* `setVoIPEndpoints(array $endpoints): void`
* `dcConnect(string $dc_number, int $id): \Generator<bool>`
* `generateContexts(int $dc_number, string $uri, \Amp\Socket\ConnectContext $context): \danog\MadelineProto\Stream\ConnectionContext[]`
* `getAPI(): \danog\MadelineProto\MTProto`
* `getHTTPClient(): \Amp\Http\Client\HttpClient`
* `getCookieJar(): \Amp\Http\Client\Cookie\CookieJar`
* `getDNSClient(): \Amp\Dns\Resolver`
* `getNonProxiedDNSClient(): \Amp\Dns\Resolver`
* `fileGetContents(string $url): \Generator`
* `getAuthConnection(string $dc): \danog\MadelineProto\Connection`
* `getConnection(string $dc): \danog\MadelineProto\Connection`
* `waitGetConnection(string $dc): \Generator`
* `getDataCenterConnection(string $dc): \danog\MadelineProto\DataCenterConnection`
* `getDataCenterConnections(): array<int|string, \danog\MadelineProto\DataCenterConnection>`
* `has(string $dc): bool`
* `isHttp(string $datacenter): bool`
* `byIPAddress(string $datacenter): bool`
* `getDcs(bool $all): array`

## Methods:
### `setDataCenterConnections(array $saved): void`

Set auth key information from saved auth array.


Parameters:
* `$saved`: `array` Saved auth array  



### `setVoIPEndpoints(array $endpoints): void`

Set VoIP endpoints.


Parameters:
* `$endpoints`: `array` Endpoints  



### `dcConnect(string $dc_number, int $id): \Generator<bool>`

Connect to specified DC.


Parameters:
* `$dc_number`: `string` DC to connect to  
* `$id`: `int` Connection ID to re-establish (optional)  


#### See also: 
* `\Generator`




### `generateContexts(int $dc_number, string $uri, \Amp\Socket\ConnectContext $context): \danog\MadelineProto\Stream\ConnectionContext[]`

Generate contexts.


Parameters:
* `$dc_number`: `int` DC ID to generate contexts for  
* `$uri`: `string` URI  
* `$context`: `\Amp\Socket\ConnectContext` Connection context  


#### See also: 
* `\Amp\Socket\ConnectContext`
* [`\danog\MadelineProto\Stream\ConnectionContext`: Connection context class.](./Stream/ConnectionContext.md)




### `getAPI(): \danog\MadelineProto\MTProto`

Get main API.


#### See also: 
* `\danog\MadelineProto\MTProto`




### `getHTTPClient(): \Amp\Http\Client\HttpClient`

Get async HTTP client.


#### See also: 
* `\Amp\Http\Client\HttpClient`




### `getCookieJar(): \Amp\Http\Client\Cookie\CookieJar`

Get async HTTP client cookies.


#### See also: 
* `\Amp\Http\Client\Cookie\CookieJar`




### `getDNSClient(): \Amp\Dns\Resolver`

Get DNS over HTTPS async DNS client.


#### See also: 
* `\Amp\Dns\Resolver`




### `getNonProxiedDNSClient(): \Amp\Dns\Resolver`

Get non-proxied DNS over HTTPS async DNS client.


#### See also: 
* `\Amp\Dns\Resolver`




### `fileGetContents(string $url): \Generator`

Get contents of file.


Parameters:
* `$url`: `string` URL to fetch  


Fully typed return value:
```
\Generator<int, \Amp\Promise<string>, mixed, string>
```
#### See also: 
* `\Amp\Promise`
* `\Generator`




### `getAuthConnection(string $dc): \danog\MadelineProto\Connection`

Get Connection instance for authorization.


Parameters:
* `$dc`: `string` DC ID  


#### See also: 
* `\danog\MadelineProto\Connection`




### `getConnection(string $dc): \danog\MadelineProto\Connection`

Get Connection instance.


Parameters:
* `$dc`: `string` DC ID  


#### See also: 
* `\danog\MadelineProto\Connection`




### `waitGetConnection(string $dc): \Generator`

Get Connection instance asynchronously.


Parameters:
* `$dc`: `string` DC ID  


Fully typed return value:
```
\Generator<int, \Amp\Promise, mixed, \danog\MadelineProto\Connection>
```
#### See also: 
* `\Amp\Promise`
* `\danog\MadelineProto\Connection`
* `\Generator`




### `getDataCenterConnection(string $dc): \danog\MadelineProto\DataCenterConnection`

Get DataCenterConnection instance.


Parameters:
* `$dc`: `string` DC ID  


#### See also: 
* [`\danog\MadelineProto\DataCenterConnection`: Datacenter connection.](./DataCenterConnection.md)




### `getDataCenterConnections(): array<int|string, \danog\MadelineProto\DataCenterConnection>`

Get all DataCenterConnection instances.


#### See also: 
* [`\danog\MadelineProto\DataCenterConnection`: Datacenter connection.](./DataCenterConnection.md)




### `has(string $dc): bool`

Check if a DC is present.


Parameters:
* `$dc`: `string` DC ID  



### `isHttp(string $datacenter): bool`

Check if connected to datacenter using HTTP.


Parameters:
* `$datacenter`: `string` DC ID  



### `byIPAddress(string $datacenter): bool`

Check if connected to datacenter directly using IP address.


Parameters:
* `$datacenter`: `string` DC ID  



### `getDcs(bool $all): array`

Get all DC IDs.


Parameters:
* `$all`: `bool` Whether to get all possible DC IDs, or only connected ones  



---
Generated by [danog/phpdoc](https://phpdoc.daniil.it)
