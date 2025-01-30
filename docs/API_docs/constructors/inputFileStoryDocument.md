---
title: "inputFileStoryDocument"
description: "Used to edit the thumbnail/static preview of a story, see here » for more info on the full flow."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputFileStoryDocument  
[Back to constructors index](/API_docs/constructors/index.html)



Used to [edit the thumbnail/static preview of a story, see here »](https://core.telegram.org/api/stories#editing-stories) for more info on the full flow.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[MessageMedia, Message, Update or InputDocument](/API_docs/types/InputDocument.html) | Optional|The old story video.|



### Type: [InputFile](/API_docs/types/InputFile.html)


### Example:

```
$inputFileStoryDocument = ['_' => 'inputFileStoryDocument', 'id' => InputDocument];
```  
