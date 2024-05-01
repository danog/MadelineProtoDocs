---
title: "webPageAttributeTheme"
description: "Page theme"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: webPageAttributeTheme  
[Back to constructors index](/API_docs/constructors/index.html)



Page theme

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|documents|Array of [Document](/API_docs/types/Document.html) | Optional|Theme files|
|settings|[ThemeSettings](/API_docs/types/ThemeSettings.html) | Optional|Theme settings|



### Type: [WebPageAttribute](/API_docs/types/WebPageAttribute.html)


### Example:

```
$webPageAttributeTheme = ['_' => 'webPageAttributeTheme', 'documents' => [Document, Document], 'settings' => ThemeSettings];
```  
