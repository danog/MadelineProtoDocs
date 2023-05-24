---
title: "inputChatUploadedPhoto"
description: "New photo to be set as group profile photo."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputChatUploadedPhoto  
[Back to constructors index](/API_docs/constructors/index.html)



New photo to be set as group profile photo.

The `file`, `video` and `video_emoji_markup` flags are mutually exclusive.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|file|[File path or InputFile](/API_docs/types/InputFile.html) | Optional|File saved in parts using the method [upload.saveFilePart](../methods/upload.saveFilePart.html)|
|video|[File path or InputFile](/API_docs/types/InputFile.html) | Optional|Square video for animated profile picture|
|video\_start\_ts|[double](/API_docs/types/double.html) | Optional|Floating point UNIX timestamp in seconds, indicating the frame of the video/sticker that should be used as static preview; can only be used if `video` or `video_emoji_markup` is set.|
|video\_emoji\_markup|[VideoSize](/API_docs/types/VideoSize.html) | Optional|Animated sticker profile picture, must contain either a [videoSizeEmojiMarkup](../constructors/videoSizeEmojiMarkup.html) or a [videoSizeStickerMarkup](../constructors/videoSizeStickerMarkup.html) constructor.|



### Type: [InputChatPhoto](/API_docs/types/InputChatPhoto.html)


### Example:

```
$inputChatUploadedPhoto = ['_' => 'inputChatUploadedPhoto', 'file' => InputFile, 'video' => InputFile, 'video_start_ts' => double, 'video_emoji_markup' => VideoSize];
```  
