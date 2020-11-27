---
title: messages.dhConfigNotModified
description: Configuring parameters did not change.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_dhConfigNotModified.html
---
# Constructor: messages.dhConfigNotModified  
[Back to constructors index](index.md)



Configuring parameters did not change.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|random|[bytes](../types/bytes.md) | Yes|Random sequence of bytes of assigned length|



### Type: [messages.DhConfig](../types/messages.DhConfig.md)


### Example:

```php
$messages_dhConfigNotModified = ['_' => 'messages.dhConfigNotModified', 'random' => 'bytes'];
```  


Or, if you're into Lua:

```lua
messages_dhConfigNotModified={_='messages.dhConfigNotModified', random='bytes'}

```


