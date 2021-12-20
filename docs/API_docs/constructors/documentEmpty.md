---
title: "documentEmpty"
description: "Empty constructor, document doesn't exist."
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: documentEmpty  
[Back to constructors index](index.md)



Empty constructor, document doesn't exist.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](../types/long.md) | Yes|Document ID or `0`|



### Type: [Document](../types/Document.md)


### Example:

```php
$documentEmpty = ['_' => 'documentEmpty', 'id' => long];
```  


Or, if you're into Lua:

```lua
documentEmpty={_='documentEmpty', id=long}

```


