---
title: changeChatReportSpamState
description: Reports chat as a spam chat or as not a spam chat. Can be used only if ChatReportSpamState.can_report_spam is true. After this request ChatReportSpamState.can_report_spam became false forever
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: changeChatReportSpamState  
[Back to methods index](index.md)


YOU CANNOT USE THIS METHOD IN MADELINEPROTO


Reports chat as a spam chat or as not a spam chat. Can be used only if ChatReportSpamState.can_report_spam is true. After this request ChatReportSpamState.can_report_spam became false forever

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|chat\_id|[int53](../types/int53.md) | Chat identifier | Yes|
|is\_spam\_chat|[Bool](../types/Bool.md) | If true, chat will be reported as a spam chat, otherwise it will be marked as not a spam chat | Yes|


### Return type: [Ok](../types/Ok.md)

