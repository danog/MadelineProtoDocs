---
title: "pendingSuggestion"
description: "pendingSuggestion attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pendingSuggestion  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|suggestion|[string](/API_docs/types/string.html) | Yes|
|title|[TextWithEntities](/API_docs/types/TextWithEntities.html) | Yes|
|description|[TextWithEntities](/API_docs/types/TextWithEntities.html) | Yes|
|url|[string](/API_docs/types/string.html) | Yes|



### Type: [PendingSuggestion](/API_docs/types/PendingSuggestion.html)


### Example:

```
$pendingSuggestion = ['_' => 'pendingSuggestion', 'suggestion' => 'string', 'title' => TextWithEntities, 'description' => TextWithEntities, 'url' => 'string'];
```  
