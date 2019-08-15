---
title: textUrl
description: Text URL
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: textUrl  
[Back to constructors index](index.md)



Text URL

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|text|[RichText](../types/RichText.md) | Yes|Text|
|url|[string](../types/string.md) | Yes|URL|
|webpage\_id|[long](../types/long.md) | Yes|Webpage ID|



### Type: [RichText](../types/RichText.md)


### Example:

```php
$textUrl = ['_' => 'textUrl', 'text' => RichText, 'url' => 'string', 'webpage_id' => long];
```  


Or, if you're into Lua:

```lua
textUrl={_='textUrl', text=RichText, url='string', webpage_id=long}

```


