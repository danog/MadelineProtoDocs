---
title: "emojiStatusCollectible"
description: "emojiStatusCollectible attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: emojiStatusCollectible  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|collectible\_id|[long](/API_docs/types/long.html) | Yes|
|document\_id|[long](/API_docs/types/long.html) | Yes|
|title|[string](/API_docs/types/string.html) | Yes|
|slug|[string](/API_docs/types/string.html) | Yes|
|pattern\_document\_id|[long](/API_docs/types/long.html) | Yes|
|center\_color|[int](/API_docs/types/int.html) | Yes|
|edge\_color|[int](/API_docs/types/int.html) | Yes|
|pattern\_color|[int](/API_docs/types/int.html) | Yes|
|text\_color|[int](/API_docs/types/int.html) | Yes|
|until|[int](/API_docs/types/int.html) | Optional|



### Type: [EmojiStatus](/API_docs/types/EmojiStatus.html)


### Example:

```
$emojiStatusCollectible = ['_' => 'emojiStatusCollectible', 'collectible_id' => long, 'document_id' => long, 'title' => 'string', 'slug' => 'string', 'pattern_document_id' => long, 'center_color' => int, 'edge_color' => int, 'pattern_color' => int, 'text_color' => int, 'until' => int];
```  
