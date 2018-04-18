---
title: Using a proxy
description: You can use a proxy with MadelineProto.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Using a proxy

You can use a proxy with MadelineProto.

There are three ways to do this:

* [Use pre-built Socks5 proxy](#socks5-proxy)
* [Use pre-built HTTP proxy](#http-proxy)
* [Build your own proxy](#build-your-proxy)


## Socks5 proxy

No password:

```
$settings['connection_settings']['all']['proxy'] = '\SocksProxy';
$settings['connection_settings']['all']['proxy_extra'] = ['address' => $proxy_address, 'port' => $proxy_port];

$MadelineProto = new \danog\MadelineProto\API('session.madeline', $settings);
```


With password:

```
$settings['connection_settings']['all']['proxy'] = '\SocksProxy';
$settings['connection_settings']['all']['proxy_extra'] = ['address' => $proxy_address, 'port' => $proxy_port, 'username' => 'user', 'password' => 'afnjasf'];

$MadelineProto = new \danog\MadelineProto\API('session.madeline', $settings);
```

## HTTP proxy

No password:

```
$settings['connection_settings']['all']['proxy'] = '\HttpProxy';
$settings['connection_settings']['all']['proxy_extra'] = ['address' => $proxy_address, 'port' => $proxy_port];

$MadelineProto = new \danog\MadelineProto\API('session.madeline', $settings);
```


With password:

```
$settings['connection_settings']['all']['proxy'] = '\HttpProxy';
$settings['connection_settings']['all']['proxy_extra'] = ['address' => $proxy_address, 'port' => $proxy_port, 'username' => 'user', 'password' => 'afnjasf'];

$MadelineProto = new \danog\MadelineProto\API('session.madeline', $settings);
```


## Build your proxy

```php
class MyProxy implements \danog\MadelineProto\Proxy
{
    //...
}
$MadelineProto->settings['connection_settings']['all']['proxy'] = '\MyProxy';
```

Simply create a class that implements the `\danog\MadelineProto\Proxy` interface, and enter its name in the settings.

Your proxy class MUST use the `\Socket` class for all TCP/UDP communications.

Your proxy class can also have a setExtra method that accepts an array as the first parameter, to pass the values provided in the proxy_extra setting.

The `\Socket` class has the following methods (all of the following methods must also be implemented by your proxy class):


`public function __construct(int $domain, int $type, int $protocol);`

Works exactly like the [socket_connect](http://php.net/manual/en/function.socket-connect.php) function.



`public function setOption(int $level, int $name, $value);`

Works exactly like the [socket_set_option](http://php.net/manual/en/function.socket-set-option.php) function.



`public function getOption(int $name, $value);`

Works exactly like the [socket_get_option](http://php.net/manual/en/function.socket-get-option.php) function.



`public function setBlocking(bool $blocking);`

Works like the [socket_block](http://php.net/manual/en/function.socket-set-block.php) or [socket_nonblock](http://php.net/manual/en/function.socket-set-nonblock.php) functions.



`public function bind(string $address, [ int $port = 0 ]);`

Works exactly like the [socket_bind](http://php.net/manual/en/function.socket-bind.php) function.



`public function listen([ int $backlog = 0 ]);`

Works exactly like the [socket_listen](http://php.net/manual/en/function.socket-listen.php) function.



`public function accept();`

Works exactly like the [socket_accept](http://php.net/manual/en/function.socket-accept.php) function.



`public function connect(string $address, [ int $port = 0 ]);`

Works exactly like the [socket_accept](http://php.net/manual/en/function.socket-connect.php) function.




`public function read(int $length, [ int $flags = 0 ]);`

Works exactly like the [socket_read](http://php.net/manual/en/function.socket-read.php) function.



`public function write(string $buffer, [ int $length ]);`

Works exactly like the [socket_write](http://php.net/manual/en/function.socket-write.php) function.



`public function send(string $data, int $length, int $flags);`

Works exactly like the [socket_send](http://php.net/manual/en/function.socket-send.php) function.



`public function close();`

Works exactly like the [socket_close](http://php.net/manual/en/function.socket-close.php) function.


`public function getPeerName(bool $port = true);`

Works like [socket_getpeername](http://php.net/manual/en/function.socket-getpeername.php): the difference is that it returns an array with the `host` and the `port`.


`public function getSockName(bool $port = true);`

Works like [socket_getsockname](http://php.net/manual/en/function.socket-getsockname.php): the difference is that it returns an array with the `host` and the `port`.


`public function getProxyHeaders();`

Can return additional HTTP headers to use when the HTTP protocol is being used.

`public function getResource();`

Returns the resource used for socket communication: should call `$socket->getResource()`.  

<a href="https://docs.madelineproto.xyz/docs/CONTRIB.html">Next section</a>
