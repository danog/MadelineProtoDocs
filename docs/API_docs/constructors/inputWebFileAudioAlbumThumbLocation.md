---
title: "inputWebFileAudioAlbumThumbLocation"
description: "Used to download an album cover for any music file using upload.getWebFile, see the webfile docs for more info »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputWebFileAudioAlbumThumbLocation  
[Back to constructors index](/API_docs/constructors/index.html)



Used to download an album cover for any music file using [upload.getWebFile](../methods/upload.getWebFile.html), see the [webfile docs for more info »](https://core.telegram.org/api/files#downloading-webfiles).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|small|[Bool](/API_docs/types/Bool.html) | Optional|Used to return a thumbnail with `100x100` resolution (instead of the default `600x600`)|
|document|[MessageMedia, Message, Update or InputDocument](/API_docs/types/InputDocument.html) | Optional|The audio file in question: must NOT be provided in secret chats, provide the `title` and `performer` fields instead.|
|title|[string](/API_docs/types/string.html) | Optional|Song title: should only be used in secret chats, in normal chats provide `document` instead, as it has more lax rate limits.|
|performer|[string](/API_docs/types/string.html) | Optional|Song performer: should only be used in secret chats, in normal chats provide `document` instead, as it has more lax rate limits.|



### Type: [InputWebFileLocation](/API_docs/types/InputWebFileLocation.html)


### Example:

```
$inputWebFileAudioAlbumThumbLocation = ['_' => 'inputWebFileAudioAlbumThumbLocation', 'small' => Bool, 'document' => InputDocument, 'title' => 'string', 'performer' => 'string'];
```  
