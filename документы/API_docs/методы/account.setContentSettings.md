---
title: "account.setContentSettings"
description: "Set sensitive content settings (for viewing or hiding NSFW content)"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_setContentSettings.html
---
# Method: account.setContentSettings
[Back to methods index](index.html)



Set sensitive content settings (for viewing or hiding NSFW content)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|чувствительный\_enabled| [Bool] (/API_docs/types/Bool.html) | Включить контент NSFW | Дополнительно|


### Тип возвращаемого зlначения: [Bool] (/API_docs/types/Bool.html)

### Can bots use this method: **NO**


### Пример MadelineProto ( [теперь асинхронно для огромной скорости и параллелизма!] (https://docs.madelneproto.xyz/docs/ASYNC.html) ):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
овкючить 'madeline.php'

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

// PHP 8+ syntax, use an array on PHP 7.
$Bool = $MadelineProto->account->setContentSettings(sensitive_enabled: Bool, );
```

