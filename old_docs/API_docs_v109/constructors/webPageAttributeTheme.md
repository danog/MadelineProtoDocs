---
title: webPageAttributeTheme
description: webPageAttributeTheme attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: webPageAttributeTheme  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|documents|Array of [Document](../types/Document.md) | Optional|
|settings|[ThemeSettings](../types/ThemeSettings.md) | Optional|



### Type: [WebPageAttribute](../types/WebPageAttribute.md)


### Example:

```php
$webPageAttributeTheme = ['_' => 'webPageAttributeTheme', 'documents' => [Document, Document], 'settings' => ThemeSettings];
```  


Or, if you're into Lua:

```lua
webPageAttributeTheme={_='webPageAttributeTheme', documents={Document}, settings=ThemeSettings}

```


