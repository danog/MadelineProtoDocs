---
title: inputMediaPoll
description: Media poll
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMediaPoll  
[Back to constructors index](index.md)



Media poll

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|poll|[Poll](../types/Poll.md) | Yes|Poll|



### Type: [InputMedia](../types/InputMedia.md)


### Example:

```php
$inputMediaPoll = ['_' => 'inputMediaPoll', 'poll' => Poll];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputMediaPoll", "poll": Poll}
```


Or, if you're into Lua:

```lua
inputMediaPoll={_='inputMediaPoll', poll=Poll}

```


