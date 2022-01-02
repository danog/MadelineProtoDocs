---
title: "webPageAttributeTheme"
description: "Page theme"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: webPageAttributeTheme  
[Back to constructors index](index.md)



Page theme

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|documents|Array of [Document](../types/Document.md) | Optional|Theme files|
|settings|[ThemeSettings](../types/ThemeSettings.md) | Optional|Theme settings|



### Type: [WebPageAttribute](../types/WebPageAttribute.md)


### Example:

```php
$webPageAttributeTheme = ['_' => 'webPageAttributeTheme', 'documents' => [Document, Document], 'settings' => ThemeSettings];
```  


Or, if you're into Lua:

```lua
webPageAttributeTheme={_='webPageAttributeTheme', documents={Document}, settings=ThemeSettings}

```


