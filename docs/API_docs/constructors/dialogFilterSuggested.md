---
title: "dialogFilterSuggested"
description: "Suggested folders"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: dialogFilterSuggested  
[Back to constructors index](index.md)



Suggested [folders](https://core.telegram.org/api/folders)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|filter|[DialogFilter](../types/DialogFilter.md) | Yes|[Folder info](https://core.telegram.org/api/folders)|
|description|[string](../types/string.md) | Yes|[Folder](https://core.telegram.org/api/folders) description|



### Type: [DialogFilterSuggested](../types/DialogFilterSuggested.md)


### Example:

```php
$dialogFilterSuggested = ['_' => 'dialogFilterSuggested', 'filter' => DialogFilter, 'description' => 'string'];
```  


Or, if you're into Lua:

```lua
dialogFilterSuggested={_='dialogFilterSuggested', filter=DialogFilter, description='string'}

```


