---
title: "Login"
description: "There are many ways you can login with MadelineProto."
nav_order: 5
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Login

There are many ways you can login with MadelineProto.

* [Getting permission to use the telegram API](#getting-permission-to-use-the-telegram-api)
* [Automatic](#automatic)
* [Manual (user)](#manual-user)
  * [API ID](#api-id)
* [Manual (bot)](#manual-bot)
* [Logout](#logout)
* [Changing 2FA password](#changing-2fa-password)

## Getting permission to use the telegram API

Before you start using MadelineProto with the Telegram API, you have to understand that Telegram strictly controls userbots created on their platform.  

If you use MadelineProto or any other Telegram client, **including official clients**, for flooding, spamming, botting channels, you **will be banned forever**.  

Due to excessive abuse of the Telegram API, **all phone numbers** that sign up or log in using **even official or approved by telegram** API clients like MadelineProto are automatically put **under observation**, and __may__ get banned **even if you did nothing wrong**, simply because some internal flags are triggered in the **telegram servers**.  

To avoid this, you must let telegram know that you will use your account with a userbot:  
When or before you first sign up or login you have to **send an email with the phone number to [recover@telegram.org](mailto:recover@telegram.org)**; explaining **what will your userbot do**.  
**DO NOT LIE**, just tell them **what will you do with the userbot** you intend to create, asking them to not ban your account.  

If your account does get banned, write to [recover@telegram.org](mailto:recover@telegram.org) asking to unban it.  

**DO NOT ABUSE OF THIS OR ANY OTHER API FOR FLOODING; SPAMMING; BOTTING**; the consequences will fall not only on you, but on all other users of this and other libraries, and even normal users.  

There were cases when several **normal user accounts that did nothing wrong** were banned when telegram deployed a new spambot detection system: this is bad for the community, and it is bad for Telegram, so please do not abuse.  


## Automatic

```php
yield $MadelineProto->start();
```

This will start an interactive login prompt via console (if running via CLI), or a login web UI (if running in the browser).  
You will get to choose if login as user, or as bot.


## Manual (user)

### API ID

Before logging in, you must obtain an [API ID](https://docs.madelineproto.xyz/docs/SETTINGS.html) (if you're using the [automatic mode you don't have to do this](#automatic)).  
You can do that either by logging in to [my.telegram.org](https://my.telegram.org) and getting your API ID/hash, or automatically, by using MadelineProto's `MyTelegramOrgWrapper` API:

```php
use danog\MadelineProto\MyTelegramOrgWrapper;

$wrapper = new MyTelegramOrgWrapper($settings);
$wrapper->async(true);

yield $wrapper->login(yield $wrapper->readline('Enter your phone number (this number must already be signed up to telegram)'));

yield $wrapper->completeLogin(yield $wrapper->readline('Enter the code'));

if (yield $wrapper->loggedIn()) {
    if (yield $wrapper->hasApp()) {
        $app = yield $wrapper->getApp();
    } else {
        $app_title = yield $wrapper->readLine('Enter the app\'s name, can be anything: ');
        $short_name = yield $wrapper->readLine('Enter the app\'s short name, can be anything: ');
        $url = yield $wrapper->readLine('Enter the app/website\'s URL, or t.me/yourusername: ');
        $description = yield $wrapper->readLine('Describe your app: ');
        
        $app = yield $wrapper->createApp(['app_title' => $app_title, 'app_shortname' => $short_name, 'app_url' => $url, 'app_platform' => 'web', 'app_desc' => $description]);
    }
    
    \danog\MadelineProto\Logger::log($app);

}
```

This wrapper allows you to automatically login to [my.telegram.org](https://my.telegram.org) and create an app associated to the specified user (the specified phone number must be already signed up to telegram).  

[Async](ASYNC.html) is handled exactly like in MadelineProto, with an `async` method that can be used to enable or disable async functionality.  
The readline wrapper (see [Async](ASYNC.html)) can also be used with the the `MyTelegramOrgWrapper` API.  

The constructor of the API is optional, and can be an array of [MadelineProto settings](https://docs.madelineproto.xyz/docs/SETTINGS.html): it can be used to set proxy info (only HTTP and SOCKS is supported for this).    


After you provide an API ID, you can then login (if you're using the [automatic mode you don't have to do this](#automatic)).  

```php
yield $MadelineProto->phoneLogin(yield $MadelineProto->readline('Enter your phone number: '));
$authorization = yield $MadelineProto->completePhoneLogin(yield $MadelineProto->readline('Enter the phone code: '));
if ($authorization['_'] === 'account.password') {
    $authorization = yield $MadelineProto->complete2falogin(yield $MadelineProto->readline('Please enter your password (hint '.$authorization['hint'].'): '));
}
if ($authorization['_'] === 'account.needSignup') {
    $authorization = yield $MadelineProto->completeSignup(yield $MadelineProto->readline('Please enter your first name: '), readline('Please enter your last name (can be empty): '));
}
```

First, you must call `phoneLogin` to send the verification code, see [here for the parameters and the result](https://docs.madelineproto.xyz/phoneLogin.html).  
Then, use `completePhoneLogin` to complete the login, see [here for the parameters and the result](https://docs.madelineproto.xyz/completePhoneLogin.html).  

Use `complete2falogin` to complete the login to an account with 2FA enabled, see [here for the parameters and the result](https://docs.madelineproto.xyz/complete2FALogin.html).  

If the account does not have an account, use `completeSignup` to signup, see [here for the parameters and the result](https://docs.madelineproto.xyz/completeSignup.html).  


## Manual (bot)

```php
yield $MadelineProto->botLogin('34298141894:aflknsaflknLKNFS');
```

Use `botLogin` to login as a bot, see [here for the parameters and the result](https://docs.madelineproto.xyz/botLogin.html).  

Note that when you login as a bot, MadelineProto also logins using the [PWRTelegram](https://pwrtelegram.xyz) API, to allow persistant storage of peers, even after a logout and another login.  


## Logout

```php
yield $MadelineProto->logout();
```

If you want to logout, you can use the logout function, see [here for the parameters and the result](https://docs.madelineproto.xyz/logout.html).  

## Changing 2FA password

```php
$result = yield $MadelineProto->update2fa(['password' => 'current password', 'new_password' => 'New password', 'email' => 'daniil@daniil.it', 'hint' => 'ponies']);
```

If you want to change the password, you can use the update2fa function, see [here for the parameters and the result](https://docs.madelineproto.xyz/update2fa.html).  

<a href="https://docs.madelineproto.xyz/docs/FEATURES.html">Next section</a>