"""
This file contains additional utility functions
"""

import os
import sys

import xbmc, xbmcgui, xbmcvfs, xbmcaddon
from webviewer import webviewer

__addon_id__= u'script.module.dropbox'
__Addon = xbmcaddon.Addon(__addon_id__)


def data_dir():
    """"get user data directory of this addon. 
    according to http://wiki.xbmc.org/index.php?title=Add-on_Rules#Requirements_for_scripts_and_plugins
    """
    __datapath__ = xbmc.translatePath( __Addon.getAddonInfo('profile') ).decode('utf-8')
    if not xbmcvfs.exists(__datapath__):
        xbmcvfs.mkdir(__datapath__)
    return __datapath__

def addon_dir():
    """"get source directory of this addon.
    according to http://wiki.xbmc.org/index.php?title=Add-on_Rules#Requirements_for_scripts_and_plugins
    """
    return __Addon.getAddonInfo('path').decode('utf-8')

def encode(string):
    return string.encode('UTF-8','replace')

def decode(string):
    return string.decode('UTF-8') 

def log(message,loglevel=xbmc.LOGDEBUG):
    """"save message to kodi.log.
    
    Args:
        message: has to be unicode, http://wiki.xbmc.org/index.php?title=Add-on_unicode_paths#Logging
        loglevel: xbmc.LOGDEBUG, xbmc.LOGINFO, xbmc.LOGNOTICE, xbmc.LOGWARNING, xbmc.LOGERROR, xbmc.LOGFATAL
    """
    xbmc.log(encode(__addon_id__ + u": " + message), level=loglevel)
    

def showNotification(title,message, time=4000):
    """Show Notification

    Args: 
        title: has to be unicode
        message: has to be unicode
        time: Time that the message is beeing displayed
    """
    __addoniconpath__ = os.path.join(addon_dir(),"icon.png")
    log(u'Notification. %s: %s' % (title, message) )
    xbmc.executebuiltin(encode('Notification("' + title + '","' + message + '",'+(str(time)).decode('utf-8')+',"' + __addoniconpath__ + '")'))

def getString(string_id):
    # return a localized string from resources/language/*.po
    # The returned string is unicode
    return __Addon.getLocalizedString(string_id)

def openURL(url):
    url, html = webviewer.getWebResult(url,autoForms=[],autoClose=None,dialog=True)
    #     osWin = xbmc.getCondVisibility('system.platform.windows')
    #     osOsx = xbmc.getCondVisibility('system.platform.osx')
    #     osLinux = xbmc.getCondVisibility('system.platform.linux')
    #     osAndroid = xbmc.getCondVisibility('System.Platform.Android')
    #     url = 'http://www.google.fr/'
    #     
    #     if osOsx:    
    #         # ___ Open the url with the default web browser
    #         xbmc.executebuiltin("System.Exec(open "+url+")")
    #     elif osWin:
    #         # ___ Open the url with the default web browser
    #         xbmc.executebuiltin("System.Exec(cmd.exe /c start "+url+")")
    #     elif osLinux and not osAndroid:
    #         # ___ Need the xdk-utils package
    #         xbmc.executebuiltin("System.Exec(xdg-open "+url+")") 
    #     elif osAndroid:
    #         # ___ Open media with standard android web browser
    #         xbmc.executebuiltin("StartAndroidActivity(com.android.browser,android.intent.action.VIEW,,"+url+")")
