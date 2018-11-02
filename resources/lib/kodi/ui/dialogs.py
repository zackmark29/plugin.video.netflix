# -*- coding: utf-8 -*-
"""Various simple dialogs"""
# pylint: disable=wildcard-import
from __future__ import unicode_literals

import xbmc
import xbmcgui

from resources.lib.globals import g
import resources.lib.common as common


def show_notification(msg, title='Netflix'):
    """Show a notification"""
    xbmc.executebuiltin('Notification({}, {}, 3000, {})'
                        .format(title, msg, g.ICON)
                        .encode('utf-8'))


def ask_credentials():
    """
    Show some dialogs and ask the user for account credentials
    """
    email = xbmcgui.Dialog().input(
        heading=common.get_local_string(30005),
        type=xbmcgui.INPUT_ALPHANUM) or None
    password = xbmcgui.Dialog().input(
        heading=common.get_local_string(30004),
        type=xbmcgui.INPUT_ALPHANUM,
        option=xbmcgui.ALPHANUM_HIDE_INPUT) or None
    common.verify_credentials(email, password)
    common.set_credentials(email, password)
    return {
        'email': email,
        'password': password
    }


def ask_for_rating():
    """Ask the user for a rating"""
    heading = '{} {}'.format(common.get_local_string(30019),
                             common.get_local_string(30022))
    try:
        return int(xbmcgui.Dialog().numeric(heading=heading, type=0,
                                            defaultt=''))
    except ValueError:
        return None


def ask_for_pin():
    """Ask the user for the adult pin"""
    return xbmcgui.Dialog().numeric(
        heading=common.get_local_string(30002),
        type=0,
        defaultt='') or None


def ask_for_search_term():
    """Ask the user for a search term"""
    return xbmcgui.Dialog().input(
        heading=common.get_local_string(30003),
        type=xbmcgui.INPUT_ALPHANUM) or None


def ask_for_custom_title(original_title):
    """Ask the user for a custom title (for library export)"""
    if g.ADDON.getSettingBool('customexportname'):
        return original_title
    return xbmcgui.Dialog().input(
        heading=common.get_local_string(30031),
        type=xbmcgui.INPUT_ALPHANUM) or original_title


def ask_for_removal_confirmation(title, year=None):
    """Ask the user to finally remove title from the Kodi library"""
    return xbmcgui.Dialog().yesno(
        heading=common.get_local_string(30047),
        line1=title + (' ({})'.format(year) if year else ''))


def show_error_info(title, message, unknown_error=False, netflix_error=False):
    """Show a dialog that displays the error message"""
    prefix = (30104, 30101, 30102)[unknown_error + netflix_error]
    return xbmcgui.Dialog().ok(title,
                               line1=common.get_local_string(prefix),
                               line2=message,
                               line3=common.get_local_string(30103))
