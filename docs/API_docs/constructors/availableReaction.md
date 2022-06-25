---
title: "availableReaction"
description: "Animations associated with a message reaction"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: availableReaction  
[Back to constructors index](/API_docs/constructors/index.html)



Animations associated with a message reaction

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|inactive|[Bool](/API_docs/types/Bool.html) | Optional|If not set, the reaction can be added to new messages and enabled in chats.|
|premium|[Bool](/API_docs/types/Bool.html) | Optional|
|reaction|[string](/API_docs/types/string.html) | Yes|Reaction emoji|
|title|[string](/API_docs/types/string.html) | Yes|Reaction description|
|static\_icon|[Document](/API_docs/types/Document.html) | Optional|Static icon for the reaction|
|appear\_animation|[Document](/API_docs/types/Document.html) | Optional|The animated sticker to show when the user opens the reaction dropdown|
|select\_animation|[Document](/API_docs/types/Document.html) | Optional|The animated sticker to show when the user selects this reaction|
|activate\_animation|[Document](/API_docs/types/Document.html) | Optional|The animated sticker to show when the reaction is chosen and activated|
|effect\_animation|[Document](/API_docs/types/Document.html) | Optional|The background effect (still an animated sticker) to play under the `activate_animation`, when the reaction is chosen and activated|
|around\_animation|[Document](/API_docs/types/Document.html) | Optional|The animation that plays around the button when you press an existing reaction (played together with `center_icon`).|
|center\_icon|[Document](/API_docs/types/Document.html) | Optional|The animation of the emoji inside the button when you press an existing reaction (played together with `around_animation`).|



### Type: [AvailableReaction](/API_docs/types/AvailableReaction.html)


### Example:

```
$availableReaction = ['_' => 'availableReaction', 'inactive' => Bool, 'premium' => Bool, 'reaction' => 'string', 'title' => 'string', 'static_icon' => Document, 'appear_animation' => Document, 'select_animation' => Document, 'activate_animation' => Document, 'effect_animation' => Document, 'around_animation' => Document, 'center_icon' => Document];
```  
