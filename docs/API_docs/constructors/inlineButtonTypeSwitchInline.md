---
title: "inlineButtonTypeSwitchInline"
description: "inlineButtonTypeSwitchInline attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inlineButtonTypeSwitchInline  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|same\_peer|[Bool](/API_docs/types/Bool.html) | Optional|
|query|[string](/API_docs/types/string.html) | Yes|
|peer\_types|Array of [InlineQueryPeerType](/API_docs/types/InlineQueryPeerType.html) | Optional|



### Type: [InlineButtonType](/API_docs/types/InlineButtonType.html)


### Example:

```
$inlineButtonTypeSwitchInline = ['_' => 'inlineButtonTypeSwitchInline', 'same_peer' => Bool, 'query' => 'string', 'peer_types' => [InlineQueryPeerType, InlineQueryPeerType]];
```  
