---
title: "textUrl"
description: "Link"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: textUrl  
[Back to constructors index](index.md)



Link

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|text|[RichText](../types/RichText.md) | Yes|Text of link|
|url|[string](../types/string.md) | Yes|Webpage HTTP URL|
|webpage\_id|[long](../types/long.md) | Yes|If a preview was already generated for the page, the page ID|



### Type: [RichText](../types/RichText.md)


### Example:

```php
$textUrl = ['_' => 'textUrl', 'text' => RichText, 'url' => 'string', 'webpage_id' => long];
```  


Or, if you're into Lua:

```lua
textUrl={_='textUrl', text=RichText, url='string', webpage_id=long}

```


