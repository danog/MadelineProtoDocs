---
title: "inputMediaWebPage"
description: "Specifies options that will be used to generate the link preview for the caption, or even a standalone link preview without an attached message."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMediaWebPage  
[Back to constructors index](/API_docs/constructors/index.html)



Specifies options that will be used to generate the link preview for the caption, or even a standalone link preview without an attached message.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|force\_large\_media|[Bool](/API_docs/types/Bool.html) | Optional|If set, specifies that a large media preview should be used.|
|force\_small\_media|[Bool](/API_docs/types/Bool.html) | Optional|If set, specifies that a small media preview should be used.|
|optional|[Bool](/API_docs/types/Bool.html) | Optional|If **not** set, a `WEBPAGE_NOT_FOUND` RPC error will be emitted if a webpage preview cannot be generated for the specified `url`; otherwise, no error will be emitted (unless the provided message is also empty, in which case a `MESSAGE_EMPTY` will be emitted, instead).|
|url|[string](/API_docs/types/string.html) | Yes|The URL to use for the link preview.|



### Type: [InputMedia](/API_docs/types/InputMedia.html)


### Example:

```
$inputMediaWebPage = ['_' => 'inputMediaWebPage', 'force_large_media' => Bool, 'force_small_media' => Bool, 'optional' => Bool, 'url' => 'string'];
```  
