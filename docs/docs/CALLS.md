---
title: "Telegram VoIP phone calls"
description: "MadelineProto provides an easy wrapper to work with phone calls."
nav_order: 21
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Telegram VoIP phone calls

MadelineProto provides an easy wrapper to work with phone calls.

[Full webradio example](https://github.com/danog/magnaluna)

* Please read the whole [VoIP API documentation](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/VoIP.html) before proceeding.
* [Requesting a call](#requesting-a-call)
* [Playing audio files](#playing-audio-files)
  * [Webhost support!](#webhost-support)
* [Accepting calls](#accepting-calls)


## Requesting a call
```php
<?php

if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$call = $MadelineProto->requestCall('@danogentili');
```

The [requestCall](https://docs.madelineproto.xyz/requestCall.html) function accepts one parameter with the ID/username/Peer/User/InputPeer of the person to call, and returns a VoIP object that can be used to play audio files, set the hold files, change the configuration and set the output file (see the [VoIP API documentation](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/VoIP.html) for more info).

You can play audio files of any format as follows:

## Playing audio files

To play audio files of any format, install `ffmpeg`, `libopus` and enable the PHP `ffi` extension.  

If you can't do the above (for example on webhosts), **no problem**: simply pre-convert the files to a special format using [@libtgvoipbot, see here &raquo;](#webhost-support) for more info.  

You can play audio files:

```php
<?php

if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

use danog\MadelineProto\LocalFile;

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$call = $MadelineProto->requestCall('@danogentili');
$call->play(new LocalFile("audio.mp3"))
     ->then(new LocalFile("audio.flac"))
     ->then(new LocalFile("audio.wav"))
     ->then(new LocalFile("audio_with_video.mp4"));
```

You can also play remote streams (or simple remote files) by URL:

```php
<?php

if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

use danog\MadelineProto\RemoteUrl;

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$call = $MadelineProto->requestCall('@danogentili');
$call->play(new RemoteUrl("http://icestreaming.rai.it/1.mp3"));
```

You can also play Telegram files, using AMP streams!


## Webhost support

Starting from MadelineProto 8, VoIP now works on webhosts, too, thanks to a pure PHP implementation of libtgvoip and a pure PHP OGG demuxer!

The only limitation when running on webhosts is that audio files must be preconverted using by sending them to [@libtgvoip_bot](https://t.me/libtgvoip_bot) ([source code](https://github.com/danog/MadelineProto/blob/v8/examples/libtgvoipbot.php)), or by using the following script on your PC:

```php
<?php

if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

use danog\MadelineProto\LocalFile;

\danog\MadelineProto\Ogg::convert(new LocalFile("in.mp3"), new LocalFile("out.ogg"));
```

Copy out.ogg to your webhost, and then run this script on your webhost:

```php
<?php

if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

use danog\MadelineProto\LocalFile;

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$call = $MadelineProto->requestCall('@danogentili');
$call->play(new LocalFile("out.ogg"));
```

## Accepting calls

Accepting calls is just as easy:

```php
<?php

declare(strict_types=1);

if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

use danog\MadelineProto\EventHandler\SimpleFilter\Incoming;
use danog\MadelineProto\VoIP;
use danog\MadelineProto\RemoteUrl;
use danog\MadelineProto\EventHandler\Attributes\Handler;

class PonyHandler extends \danog\MadelineProto\SimpleEventHandler
{
    #[Handler]
    public function handleIncomingCall(VoIP&Incoming $call): void
    {
        $call->accept()->play(new RemoteUrl('http://icestreaming.rai.it/1.mp3'));
    }
}

PonyHandler::startAndLoop('session.madeline');
```

## Recording calls

To record the incoming audio stream in a call, simply use `setOutput`:

```php
<?php

declare(strict_types=1);

if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

use danog\MadelineProto\EventHandler\SimpleFilter\Incoming;
use danog\MadelineProto\VoIP;
use danog\MadelineProto\RemoteUrl;
use danog\MadelineProto\LocalFile;
use danog\MadelineProto\EventHandler\Attributes\Handler;
use Amp\ByteStream\WritableStream;

class PonyHandler extends \danog\MadelineProto\SimpleEventHandler
{
    #[Handler]
    public function handleIncomingCall(VoIP&Incoming $call): void
    {
        $call->accept();
        $call->play(new RemoteUrl('http://icestreaming.rai.it/1.mp3'));

        $call->setOutput(new LocalFile('output.ogg'));
        
        // $stream can also be a WritableStream.
        // Can be used to pipe OGG OPUS audio data to ffmpeg, asterisk via amphp/process, amphp/socket, etc...
        //
        //$call->setOutput($stream);
    }
}

PonyHandler::startAndLoop('session.madeline');
```

<a href="https://docs.madelineproto.xyz/docs/FILES.html">Next section</a>
