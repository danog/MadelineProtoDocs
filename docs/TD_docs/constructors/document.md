---
title: document
description: Describes document of any type
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
## Constructor: document  
[Back to constructors index](index.md)



Describes document of any type

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|file\_name|[string](../types/string.md) | Yes|Original name of a file as defined by sender|
|mime\_type|[string](../types/string.md) | Yes|MIME type of file as defined by sender|
|thumb|[photoSize](../constructors/photoSize.md) | Yes|Document thumb as defined by sender, nullable|
|document|[file](../constructors/file.md) | Yes|File with document|



### Type: [Document](../types/Document.md)


