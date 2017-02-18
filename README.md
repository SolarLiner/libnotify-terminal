# libnotify-terminal
terminal-notifier port for linux using libnotify and zenity.

## Usage
### Basic
This allows you to "fire and forget" notifications.

```--app-title <application-title>``` sets the application title (TODO)

```--title <title>``` sets the notification title

```--body <body>``` sets the notification body

```--subtitle <subtitle>``` inserts text before the notification body (provided for completeness)

*Note*: only ```--body``` is required.

### Add actions
This allows you to add buttons to the notification.

```--action <name>,<label>``` adds the button shown as ```<label>```, and ```libnotify-terminal``` will pipe ```<name>```, if clicked, through stdout.

*Note*: Only one button can be clicked, as the notification closes after.

### Reply mode
On top of adding action, you can add the possibility to reply.

```--reply``` sets the reply mode. In this mode, if the user clicks "Reply", ```libnotify-terminal``` will spawn a ```zenity``` entry dialog, and will pipe the entered text through stdout.

```--reply-to <contact>``` sets the name of the contact the user is replying to.

```--reply-message <message>``` sets the sent message, displayed in the ```zenity``` dialog box.

*Note*: Neither ```--reply-to``` or ```--reply-message``` is required. Generic messages will be substitued. ```--reply-message``` is kept separate from ```--body``` for customization purposes - or privacy, whichever you end up choosing.

## Installing
### Dependencies
```libnotify-terminal``` is written with python2.7 and requires the following packages:
* ```make```
* ```python-gobject```
* ```python-notify2```

### Download
Head over to the [releases](https://github.com/SolarLiner/libnotify-terminal/releases) page and download the latest source code.

Or clone the repo:
* the ```master``` branch follows more or less the releases versions. It is kept this way to show the stable version with the binary that they use.
* the ```staging``` branch is the latest code version that "works" (that is, should normally fire notifications). However don't expect stability or promises kept there.
* the ```develop``` branch... don't download it for compilation, unless you're a masochist (which, I mean, I'm okay, but here... 😶)

### Compiling
* ```$ make && sudo make install```
* ```make test``` (optional) tests for successful installation. If this fails, try ```make test-compile``` to see if it compiled successfully.
