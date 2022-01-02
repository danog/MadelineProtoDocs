---
title: "inputMessagesFilterPhoneCalls"
description: "Return only phone calls"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMessagesFilterPhoneCalls  
[Back to constructors index](index.md)



Return only phone calls

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|missed|[Bool](../types/Bool.md) | Optional|Return only missed phone calls|



### Type: [MessagesFilter](../types/MessagesFilter.md)


### Example:

```php
$inputMessagesFilterPhoneCalls = ['_' => 'inputMessagesFilterPhoneCalls', 'missed' => Bool];
```  


Or, if you're into Lua:

```lua
inputMessagesFilterPhoneCalls={_='inputMessagesFilterPhoneCalls', missed=Bool}

```


