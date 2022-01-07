---
title: "textConcat"
description: "Concatenation of rich texts"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: textConcat  
[Back to constructors index](/API_docs/constructors/index.md)



Concatenation of rich texts

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|texts|Array of [RichText](/API_docs/types/RichText.md) | Yes|Concatenated rich texts|



### Type: [RichText](/API_docs/types/RichText.md)


### Example:

```php
$textConcat = ['_' => 'textConcat', 'texts' => [RichText, RichText]];
```  
