---
title: "webPageAttributeTheme"
description: "Page theme"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: webPageAttributeTheme  
[Back to constructors index](/API_docs/constructors/index.md)



Page theme

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|documents|Array of [Document](/API_docs/types/Document.md) | Optional|Theme files|
|settings|[ThemeSettings](/API_docs/types/ThemeSettings.md) | Optional|Theme settings|



### Type: [WebPageAttribute](/API_docs/types/WebPageAttribute.md)


### Example:

```php
$webPageAttributeTheme = ['_' => 'webPageAttributeTheme', 'documents' => [Document, Document], 'settings' => ThemeSettings];
```  
