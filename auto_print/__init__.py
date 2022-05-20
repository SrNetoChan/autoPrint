# -*- coding: utf-8 -*-
"""
/***************************************************************************
 autoPrint
                                 A QGIS plugin
 Update the extent of LayoutItemMap and exports PDF
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2022-05-20
        copyright            : (C) 2022 by Christoph Mohr
        email                : moin@chrissem.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load autoPrint class from file autoPrint.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .auto_print import autoPrint
    return autoPrint(iface)
