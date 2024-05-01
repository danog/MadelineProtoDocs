---
title: "dialogFilterSuggested"
description: "Suggested folders"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: dialogFilterSuggested  
[Back to constructors index](/API_docs/constructors/index.html)



Suggested [folders](https://core.telegram.org/api/folders)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|filter|[DialogFilter](/API_docs/types/DialogFilter.html) | Yes|[Folder info](https://core.telegram.org/api/folders)|
|description|[string](/API_docs/types/string.html) | Yes|[Folder](https://core.telegram.org/api/folders) description|



### Type: [DialogFilterSuggested](/API_docs/types/DialogFilterSuggested.html)


### Example:

```
$dialogFilterSuggested = ['_' => 'dialogFilterSuggested', 'filter' => DialogFilter, 'description' => 'string'];
```  
