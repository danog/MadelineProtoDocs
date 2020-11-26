---
title: keyboardButtonUrl
description: URL button
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: keyboardButtonUrl  
[Back to constructors index](index.md)



URL button

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|text|[string](../types/string.md) | Yes|Button label|
|url|[string](../types/string.md) | Yes|URL|



### Type: [KeyboardButton](../types/KeyboardButton.md)


### Example:

```php
$keyboardButtonUrl = ['_' => 'keyboardButtonUrl', 'text' => 'string', 'url' => 'string'];
```  


Or, if you're into Lua:

```lua
keyboardButtonUrl={_='keyboardButtonUrl', text='string', url='string'}

```


