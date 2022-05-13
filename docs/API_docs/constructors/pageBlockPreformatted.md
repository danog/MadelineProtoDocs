---
title: "pageBlockPreformatted"
description: "Preformatted (<pre> text)"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockPreformatted  
[Back to constructors index](/API_docs/constructors/index.html)



Preformatted (`<pre>` text)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|text|[RichText](/API_docs/types/RichText.html) | Yes|Text|
|language|[string](/API_docs/types/string.html) | Yes|Programming language of preformatted text|



### Type: [PageBlock](/API_docs/types/PageBlock.html)


### Example:

```
$pageBlockPreformatted = ['_' => 'pageBlockPreformatted', 'text' => RichText, 'language' => 'string'];
```  
