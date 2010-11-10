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

class BudgetItem:

    _properties = (
    {   "id"                : "budget_state"
      , "description"       : "Budget State"
      , "type"              : "string"
      , "mode"              : "w"
    },

    {   "id"                : "budget_provision"
      , "description"       : "Budget Provision"
      , "type"              : "int"
      , "mode"              : "w"
    },

    {   "id"                : "budget_available"
      , "description"       : "Budget Available"
      , "type"              : "int"
      , "mode"              : "w"
    },

    {   "id"                : "amount_spent"
      , "description"       : "Amount Spent"
      , "type"              : "int"
      , "mode"              : "w"
    },

    {   "id"                : "balance_amount"
      , "description"       : "Balance Amount"
      , "type"              : "int"
      , "mode"              : "w"
    },

    {   "id"                : "letter_reference"
      , "description"       : "Letter Reference"
      , "type"              : "string"
      , "mode"              : "w"
    },

    {   "id"                : "letter_date"
      , "description"       : "Letter Date"
      , "type"              : "date"
      , "mode"              : "w"
    },

    {   "id"                : "university_order"
      , "description"       : "University Order"
      , "type"              : "string"
      , "mode"              : "w"
    },

    {   "id"                : "university_order_date"
      , "description"       : "University Order Date"
      , "type"              : "date"
      , "mode"              : "w"
    },

    )

    _categories = (
                   "financial_year",
                   "department",
                   "plan_type",
                   "budget_head",
    )

