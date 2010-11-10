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

class Bill:

    _properties = (
    {   "id"                : "bill_state"
      , "description"       : "Bill State"
      , "type"              : "string"
      , "mode"              : "w"
    },

    {   "id"                : "bill_no"
      , "description"       : "Bill No"
      , "type"              : "string"
      , "mode"              : "w"
    },

    {   "id"                : "date"
      , "description"       : "Date"
      , "type"              : "date"
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

    {   "id"                : "net_amount_claimed_in_this_bill"
      , "description"       : "Net Amount Claimed In This Bill"
      , "type"              : "int"
      , "mode"              : "w"
    },

    {   "id"                : "expenduiture_including_this_bill"
      , "description"       : "Expenduiture Including This Bill"
      , "type"              : "int"
      , "mode"              : "w"
    },

    {   "id"                : "balance_avalible_in_budget"
      , "description"       : "Balance Avalible In Budget"
      , "type"              : "int"
      , "mode"              : "w"
    },

    {   "id"                : "approved_gross_amount"
      , "description"       : "Approved Gross Amount"
      , "type"              : "int"
      , "mode"              : "w"
    },

    {   "id"                : "deduction_amount"
      , "description"       : "Deduction Amount"
      , "type"              : "int"
      , "mode"              : "w"
    },

    {   "id"                : "deduction_calculated"
      , "description"       : "Deduction Calculated"
      , "type"              : "int"
      , "mode"              : "w"
    },

    {   "id"                : "net_amount_payable"
      , "description"       : "Net Amount Payable"
      , "type"              : "int"
      , "mode"              : "w"
    },

    {   "id"                : "refund_amount"
      , "description"       : "Refund Amount"
      , "type"              : "int"
      , "mode"              : "w"
    },

    {   "id"                : "voucher_no"
      , "description"       : "Voucher No"
      , "type"              : "string"
      , "mode"              : "w"
    },

    {   "id"                : "university_order_no"
      , "description"       : "University Order No"
      , "type"              : "string"
      , "mode"              : "w"
    },

    {   "id"                : "university_order_date"
      , "description"       : "University Order Date"
      , "type"              : "date"
      , "mode"              : "w"
    },

    {   "id"                : "name_of_supplier"
      , "description"       : "Name Of Supplier"
      , "type"              : "string"
      , "mode"              : "w"
    },

    {   "id"                : "reasons_for_objection"
      , "description"       : "Reasons For Objection"
      , "type"              : "text"
      , "mode"              : "w"
    },

    )

    _categories = (
                   "bill_type",
                   "source_section",
                   "financial_year",
                   "department",
                   "plan_type",
                   "budget_head",
                   "forwardedto",
    )

