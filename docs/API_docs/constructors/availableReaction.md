---
title: "availableReaction"
description: "availableReaction attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: availableReaction  
[Back to constructors index](/API_docs/constructors/index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|inactive|[Bool](/API_docs/types/Bool.md) | Optional|
|reaction|[string](/API_docs/types/string.md) | Yes|
|title|[string](/API_docs/types/string.md) | Yes|
|static\_icon|[Document](/API_docs/types/Document.md) | Optional|
|appear\_animation|[Document](/API_docs/types/Document.md) | Optional|
|select\_animation|[Document](/API_docs/types/Document.md) | Optional|
|activate\_animation|[Document](/API_docs/types/Document.md) | Optional|
|effect\_animation|[Document](/API_docs/types/Document.md) | Optional|



### Type: [AvailableReaction](/API_docs/types/AvailableReaction.md)


### Example:

```php
$availableReaction = ['_' => 'availableReaction', 'inactive' => Bool, 'reaction' => 'string', 'title' => 'string', 'static_icon' => Document, 'appear_animation' => Document, 'select_animation' => Document, 'activate_animation' => Document, 'effect_animation' => Document];
```  
