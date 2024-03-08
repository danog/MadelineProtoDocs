---
title: "sponsoredWebPage"
description: "Represents a sponsored website."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: sponsoredWebPage  
[Back to constructors index](/API_docs/constructors/index.html)



Represents a sponsored website.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|url|[string](/API_docs/types/string.html) | Yes|Web page URL.|
|site\_name|[string](/API_docs/types/string.html) | Yes|Website name.|
|photo|[Photo](/API_docs/types/Photo.html) | Optional|Optional image preview.|



### Type: [SponsoredWebPage](/API_docs/types/SponsoredWebPage.html)


### Example:

```
$sponsoredWebPage = ['_' => 'sponsoredWebPage', 'url' => 'string', 'site_name' => 'string', 'photo' => Photo];
```  
