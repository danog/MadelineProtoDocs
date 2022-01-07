---
title: "availableReaction"
description: "availableReaction attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: availableReaction  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|inactive|[Bool](/API_docs/types/Bool.html) | Optional|
|reaction|[string](/API_docs/types/string.html) | Yes|
|title|[string](/API_docs/types/string.html) | Yes|
|static\_icon|[Document](/API_docs/types/Document.html) | Optional|
|appear\_animation|[Document](/API_docs/types/Document.html) | Optional|
|select\_animation|[Document](/API_docs/types/Document.html) | Optional|
|activate\_animation|[Document](/API_docs/types/Document.html) | Optional|
|effect\_animation|[Document](/API_docs/types/Document.html) | Optional|



### Type: [AvailableReaction](/API_docs/types/AvailableReaction.html)


### Example:

```php
$availableReaction = ['_' => 'availableReaction', 'inactive' => Bool, 'reaction' => 'string', 'title' => 'string', 'static_icon' => Document, 'appear_animation' => Document, 'select_animation' => Document, 'activate_animation' => Document, 'effect_animation' => Document];
```  
