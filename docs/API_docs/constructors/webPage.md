---
title: "webPage"
description: "Webpage preview"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: webPage  
[Back to constructors index](/API_docs/constructors/index.html)



Webpage preview

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|has\_large\_media|[Bool](/API_docs/types/Bool.html) | Optional|Whether the size of the media in the preview can be changed.|
|video\_cover\_photo|[Bool](/API_docs/types/Bool.html) | Optional|Represents a custom [video cover](https://core.telegram.org/api/files#video-covers).|
|id|[long](/API_docs/types/long.html) | Yes|Preview ID|
|url|[string](/API_docs/types/string.html) | Yes|URL of previewed webpage|
|display\_url|[string](/API_docs/types/string.html) | Yes|Webpage URL to be displayed to the user|
|hash|[int](/API_docs/types/int.html) | Yes|
|type|[string](/API_docs/types/string.html) | Optional|Type of the web page. One of the following: <!-- start type --><br><br>- `app`<br>- `article`<br>- `document`<br>- `gif`<br>- `photo`<br>- `profile`<br>- `telegram_album`<br>- `telegram_background`<br>- `telegram_bot`<br>- `telegram_botapp`<br>- `telegram_call`<br>- `telegram_channel`<br>- `telegram_channel_boost`<br>- `telegram_channel_direct`<br>- `telegram_channel_request`<br>- `telegram_chat`<br>- `telegram_chat_request`<br>- `telegram_chatlist`<br>- `telegram_collection`<br>- `telegram_community`<br>- `telegram_giftcode`<br>- `telegram_group_boost`<br>- `telegram_livestream`<br>- `telegram_megagroup`<br>- `telegram_megagroup_request`<br>- `telegram_message`<br>- `telegram_nft`<br>- `telegram_stickerset`<br>- `telegram_story`<br>- `telegram_story_album`<br>- `telegram_theme`<br>- `telegram_user`<br>- `telegram_videochat`<br>- `telegram_voicechat`<br>- `video`<br><br><!-- end type -->|
|site\_name|[string](/API_docs/types/string.html) | Optional|Short name of the site (e.g., Google Docs, App Store)|
|title|[string](/API_docs/types/string.html) | Optional|Title of the content|
|description|[string](/API_docs/types/string.html) | Optional|Content description|
|photo|[Photo](/API_docs/types/Photo.html) | Optional|Image representing the content|
|embed\_url|[string](/API_docs/types/string.html) | Optional|URL to show in the embedded preview|
|embed\_type|[string](/API_docs/types/string.html) | Optional|MIME type of the embedded preview, (e.g., text/html or video/mp4)|
|embed\_width|[int](/API_docs/types/int.html) | Optional|Width of the embedded preview|
|embed\_height|[int](/API_docs/types/int.html) | Optional|Height of the embedded preview|
|duration|[int](/API_docs/types/int.html) | Optional|Duration of the content, in seconds|
|author|[string](/API_docs/types/string.html) | Optional|Author of the content|
|document|[Document](/API_docs/types/Document.html) | Optional|Preview of the content as a media file|
|cached\_page|[Page](/API_docs/types/Page.html) | Optional|Page contents in [instant view](https://instantview.telegram.org) format|
|attributes|Array of [WebPageAttribute](/API_docs/types/WebPageAttribute.html) | Optional|Webpage attributes|



### Type: [WebPage](/API_docs/types/WebPage.html)


### Example:

```
$webPage = ['_' => 'webPage', 'has_large_media' => Bool, 'video_cover_photo' => Bool, 'id' => long, 'url' => 'string', 'display_url' => 'string', 'hash' => int, 'type' => 'string', 'site_name' => 'string', 'title' => 'string', 'description' => 'string', 'photo' => Photo, 'embed_url' => 'string', 'embed_type' => 'string', 'embed_width' => int, 'embed_height' => int, 'duration' => int, 'author' => 'string', 'document' => Document, 'cached_page' => Page, 'attributes' => [WebPageAttribute, WebPageAttribute]];
```  
