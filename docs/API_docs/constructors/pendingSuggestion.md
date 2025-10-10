---
title: "pendingSuggestion"
description: "Represents a custom pending suggestion »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pendingSuggestion  
[Back to constructors index](/API_docs/constructors/index.html)



Represents a [custom pending suggestion »](https://core.telegram.org/api/config#custom-suggestions).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|suggestion|[string](/API_docs/types/string.html) | Yes|The suggestion ID, can be passed to [help.dismissSuggestion](../methods/help.dismissSuggestion.html).|
|title|[TextWithEntities](/API_docs/types/TextWithEntities.html) | Yes|Title of the suggestion.|
|description|[TextWithEntities](/API_docs/types/TextWithEntities.html) | Yes|Body of the suggestion.|
|url|[string](/API_docs/types/string.html) | Yes|URL to open when the user clicks on the suggestion.|



### Type: [PendingSuggestion](/API_docs/types/PendingSuggestion.html)


### Example:

```
$pendingSuggestion = ['_' => 'pendingSuggestion', 'suggestion' => 'string', 'title' => TextWithEntities, 'description' => TextWithEntities, 'url' => 'string'];
```  
