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
|id|[long](/API_docs/types/long.html) | Yes|Preview ID|
|url|[string](/API_docs/types/string.html) | Yes|URL of previewed webpage|
|display\_url|[string](/API_docs/types/string.html) | Yes|Webpage URL to be displayed to the user|
|hash|[int](/API_docs/types/int.html) | Yes|
|type|[string](/API_docs/types/string.html) | Optional|Type of the web page. Can be: article, photo, audio, video, document, profile, app, or something else|
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
$webPage = ['_' => 'webPage', 'id' => long, 'url' => 'string', 'display_url' => 'string', 'hash' => int, 'type' => 'string', 'site_name' => 'string', 'title' => 'string', 'description' => 'string', 'photo' => Photo, 'embed_url' => 'string', 'embed_type' => 'string', 'embed_width' => int, 'embed_height' => int, 'duration' => int, 'author' => 'string', 'document' => Document, 'cached_page' => Page, 'attributes' => [WebPageAttribute, WebPageAttribute]];
```  
