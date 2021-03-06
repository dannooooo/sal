# Using plugins with Sal

It's easy to extend Sal with plugins created by others. A plugin could consist of a "traffic light" display (similar to the built in memory plugin), a listing (e.g. the operating system breakdown), or anything else. I've created plugins that report data in graphs using Google Charts with data from a custom fact.

## Installing plugins

1. Copy the whole plugin directory into the plugins directory. This should include at minimum a ``.py`` file and a ``.yapsy-plugin`` file, but can include more (quite often a ``templates`` directory). For basic operation, all you need to do now is restart Apache and the plugin should appear on your dashboard. If not, head onto the troubleshooting section later on.
2. If you want to control what order the plugins show in, you will need to modify ``PLUGIN_ORDER`` in`` sal/settings.py``. You can find the name of the plugin in the ``.yapsy-plugin`` file - the Name can be found in the ``[Core]`` section.
3. To hide the plugin from a specific Business Unit or Machine Group, add it to the ``HIDE_PLUGIN_FROM_BUSINESS_UNIT`` or ``HIDE_PLUGIN_FROM_MACHINE_GROUP`` settings in ``sal/settings.py``. You will need the ID number of the Business Unit or Machine Group, which you can get from the URL displayed in your browser when on that BU or Group's page. Hiding a plugin from a business unit will also hide it from it's child groups. 
4. Similarly, to only show or hide the plugin on the front page, the plugin's name should be added to the list in ``sal/settings.py``.

For more details on configuring ``sal/settings.py`` please see it's [documentation](https://github.com/grahamgilbert/sal/blob/master/docs/Settings.md).

## Troubleshooting

###  I'm not seeing anything after installing the plugin

There are a few reasons you might not get any output from the plugin. 

* The plugin might be set to not display anything if there isn't anything for it to show (the Fact or Condition it relies on isn't available, or there aren't any updates to install, for example).
* If you are sure that it should be showing something, then you should check that it's in the correct directory, and that it's readable and executable by the user the application is running as (saluser if you followed the instructions here).
* If youre still having problems, then there may be something wrong with the plugin. You should contact the person who wrote the plugin for more assistance - their contact details will hopefully be in the .yapsy-plugin file.