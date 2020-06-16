---
title: inputMediaPoll
description: A poll
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMediaPoll  
[Back to constructors index](index.md)



A poll

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|poll|[Poll](../types/Poll.md) | Yes|The poll to send|



### Type: [InputMedia](../types/InputMedia.md)


### Example:

```php
$inputMediaPoll = ['_' => 'inputMediaPoll', 'poll' => Poll];
```  


Or, if you're into Lua:

```lua
inputMediaPoll={_='inputMediaPoll', poll=Poll}

```


