# Sal

## How it works

Sal is split into Business Units, and then subdivided into Groups. Each customer would be a Business Unit, and then the machines can be divided into Machine Groups. 

##Server installation

See [Installation_on_Ubuntu_12.md](https://github.com/grahamgilbert/sal/blob/master/docs/Installation_on_Ubuntu_12.md) for server installation docs.

## Server upgrade

See [Upgrading_on_Ubuntu_12.md](https://github.com/grahamgilbert/sal/blob/master/docs/Upgrading_on_Ubuntu_12.md) for upgrade docs.

### Getting started

Log in with the username and password you set when performing the server setup. You will need to create a Business Unit and Machine Group to get started.

### User Levels

There are currently the User Levels used by Sal. To set these, log into the admin page (link at the top of the Sal screen), and choose User Profile from the menu. The Stats Only user level is not used at this time, and should not be assigned to a user.

#### Global Administrator

A Global Administrator (GA) has access to everything - they can get to all Business Unitsm, they can create new Business Units and Machine Groups. They cannot get to the admin interface though. To do this, they need to be made staff (in the Users section of the admin interface).

#### Read / Write, Read Only

These users are limited to the Business Units they are given access to. RW users can create new Machine Groups within their Business Units, Read Only users are only able to view the information.

## Client configuration

``postflight`` is in the ``scripts`` directory. This needs to be deployed in ``/usr/local/munki``, and the ``yaml`` directory should be deployed in ``/usr/local/sal/yaml`` (a luggage makefile is included).  The published package will do this for you.

If you have an existing ``postflight`` script (for example, Munki Web Admin), you will need to rename the postflight script (for example, ``sal-submit``) and put something in your existing postflight like this:

```
if [ -f /usr/local/munki/sal-submit ]
  then
    /usr/local/munki/sal-submit
fi
```

The configuration of the server, and the Machine Group key is from ``/Library/Preferences/com.grahamgilbert.sal``. Plists, MCX (untested, but should work) and Profiles can be used.

### Example

``defaults write /Library/Preferences/com.grahamgilbert.sal ServerURL http://sal.somewhere.com``

``defaults write /Library/Preferences/com.grahamgilbert.sal key e4up7l5pzaq7w4x12en3c0d5y3neiutlezvd73z9qeac7zwybv3jj5tghhmlseorzy5kb4zkc7rnc2sffgir4uw79esdd60pfzfwszkukruop0mmyn5gnhark9n8lmx9``

