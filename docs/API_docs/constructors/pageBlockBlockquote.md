---
title: "pageBlockBlockquote"
description: "Quote (equivalent to the HTML <blockquote>)"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockBlockquote  
[Back to constructors index](/API_docs/constructors/index.md)



Quote (equivalent to the HTML `<blockquote>`)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|text|[RichText](/API_docs/types/RichText.md) | Yes|Quote contents|
|caption|[RichText](/API_docs/types/RichText.md) | Yes|Caption|



### Type: [PageBlock](/API_docs/types/PageBlock.md)


### Example:

```php
$pageBlockBlockquote = ['_' => 'pageBlockBlockquote', 'text' => RichText, 'caption' => RichText];
```  
