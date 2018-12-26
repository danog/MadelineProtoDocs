---
title: http_wait
description: Http wait
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: http\_wait  
[Back to constructors index](index.md)



Http wait

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|max\_delay|[int](../types/int.md) | Yes|Max delay|
|wait\_after|[int](../types/int.md) | Yes|Wait after|
|max\_wait|[int](../types/int.md) | Yes|Max wait|



### Type: [HttpWait](../types/HttpWait.md)


### Example:

```php
$http_wait = ['_' => 'http_wait', 'max_delay' => int, 'wait_after' => int, 'max_wait' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "http_wait", "max_delay": int, "wait_after": int, "max_wait": int}
```


Or, if you're into Lua:

```lua
http_wait={_='http_wait', max_delay=int, wait_after=int, max_wait=int}

```


