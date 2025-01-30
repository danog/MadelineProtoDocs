---
title: "reportResultAddComment"
description: "The user should enter an additional comment for the moderators, and then messages.report must be re-invoked, passing the comment to messages.report.message."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: reportResultAddComment  
[Back to constructors index](/API_docs/constructors/index.html)



The user should enter an additional comment for the moderators, and then [messages.report](../methods/messages.report.html) must be re-invoked, passing the comment to [messages.report](../methods/messages.report.html).`message`.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|optional|[Bool](/API_docs/types/Bool.html) | Optional|Whether this step can be skipped by the user, passing an empty `message` to [messages.report](../methods/messages.report.html), or if a non-empty `message` is mandatory.|
|option|[bytes](/API_docs/types/bytes.html) | Yes|The [messages.report](../methods/messages.report.html) method must be re-invoked, passing this option to `option`|



### Type: [ReportResult](/API_docs/types/ReportResult.html)


### Example:

```
$reportResultAddComment = ['_' => 'reportResultAddComment', 'optional' => Bool, 'option' => 'bytes'];
```  
