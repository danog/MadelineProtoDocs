---
title: pollAnswer
description: Poll answer
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pollAnswer  
[Back to constructors index](index.md)



Poll answer

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|text|[string](../types/string.md) | Yes|Text|
|option|[bytes](../types/bytes.md) | Yes|Option|



### Type: [PollAnswer](../types/PollAnswer.md)


### Example:

```php
$pollAnswer = ['_' => 'pollAnswer', 'text' => 'string', 'option' => 'bytes'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "pollAnswer", "text": "string", "option": {"_": "bytes", "bytes":"base64 encoded bytes"}}
```


Or, if you're into Lua:

```lua
pollAnswer={_='pollAnswer', text='string', option='bytes'}

```


