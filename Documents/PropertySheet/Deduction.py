##############################################################################
#
# Copyright (c) 2010-16 Ignatius Kunjumon All Rights Reserved.
#          Ignatius Kunjumon <ignatius.kunjumon@gmail.com>
#
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
##############################################################################

class Deduction:

    _properties = (
    {   "id"                : "deduction_state"
      , "description"       : "Deduction State"
      , "type"              : "string"
      , "mode"              : "w"
    },

    {   "id"                : "amount"
      , "description"       : "Amount"
      , "type"              : "int"
      , "mode"              : "w"
    },

    )

    _categories = (
                   "deduction_type",
    )

