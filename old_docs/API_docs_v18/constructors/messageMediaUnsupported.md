---
title: messageMediaUnsupported
description: Current version of the client does not support this media type.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageMediaUnsupported  
[Back to constructors index](index.md)



Current version of the client does not support this media type.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|bytes|[bytes](../types/bytes.md) | Yes|Bytes|



### Type: [MessageMedia](../types/MessageMedia.md)


### Example:

```php
$messageMediaUnsupported = ['_' => 'messageMediaUnsupported', 'bytes' => 'bytes'];
```  


Or, if you're into Lua:

```lua
messageMediaUnsupported={_='messageMediaUnsupported', bytes='bytes'}

```


