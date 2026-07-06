"""
Finance Department Policy Catalog

Knowledge Firewall AI

Defines all Finance related enterprise policy categories.
"""

from src.config.blueprints.compliance import (
    COMPLIANCE_ACTIONS,
    COMPLIANCE_OBJECTS,
    COMPLIANCE_PURPOSES,
    COMPLIANCE_RULES,
    COMPLIANCE_KEYWORDS
)

from src.config.blueprints.data_management import (
    DATA_ACTIONS,
    DATA_OBJECTS,
    DATA_PURPOSES,
    DATA_RULES,
    DATA_KEYWORDS
)

from src.config.title_templates.finance_titles import (
    EXPENSE_MANAGEMENT_TITLES,
    PROCUREMENT_TITLES,
    PAYROLL_TITLES,
    BUDGET_PLANNING_TITLES,
    FINANCIAL_REPORTING_TITLES
)

FINANCE_POLICIES = {

    ###########################################################################
    # EXPENSE MANAGEMENT
    ###########################################################################

    "Expense_Management": {

        "title_templates": EXPENSE_MANAGEMENT_TITLES,
        "department": "Finance",
        "folder_name": "Finance",

        "security_domain": "Expense Management",

        "owner": "Finance Operations",

        "classification": "Internal",

        "risk_level": "Medium",

        "document_prefix": "FIN-EXP",

        "documents_to_generate": 25,

        "actions": DATA_ACTIONS,

        "objects": DATA_OBJECTS + [
            "Expense Claim",
            "Travel Expense",
            "Corporate Card Expense",
            "Employee Reimbursement"
        ],

        "purposes": DATA_PURPOSES,

        "rules": DATA_RULES + [
            "must include supporting receipts",
            "must receive manager approval",
            "must comply with expense policy"
        ],

        "keywords": DATA_KEYWORDS + [
            "expense",
            "reimbursement",
            "travel"
        ]

    },

    ###########################################################################
    # PROCUREMENT
    ###########################################################################

    "Procurement": {

        "title_templates": PROCUREMENT_TITLES,
        "department": "Finance",
        "folder_name": "Finance",

        "security_domain": "Procurement",

        "owner": "Procurement Team",

        "classification": "Internal",

        "risk_level": "Medium",

        "document_prefix": "FIN-PRC",

        "documents_to_generate": 25,

        "actions": COMPLIANCE_ACTIONS,

        "objects": COMPLIANCE_OBJECTS + [
            "Purchase Order",
            "Vendor Invoice",
            "Procurement Request",
            "Purchase Approval"
        ],

        "purposes": COMPLIANCE_PURPOSES,

        "rules": COMPLIANCE_RULES + [
            "must follow procurement workflow",
            "must include vendor verification",
            "must comply with purchasing policy"
        ],

        "keywords": COMPLIANCE_KEYWORDS + [
            "procurement",
            "vendor",
            "purchase"
        ]

    },

    ###########################################################################
    # PAYROLL
    ###########################################################################

    "Payroll": {

        "title_templates": PAYROLL_TITLES,
        "department": "Finance",
        "folder_name": "Finance",

        "security_domain": "Payroll",

        "owner": "Payroll Team",

        "classification": "Confidential",

        "risk_level": "High",

        "document_prefix": "FIN-PAY",

        "documents_to_generate": 25,

        "actions": DATA_ACTIONS,

        "objects": DATA_OBJECTS + [
            "Payroll Record",
            "Salary Payment",
            "Tax Deduction",
            "Employee Compensation"
        ],

        "purposes": DATA_PURPOSES,

        "rules": DATA_RULES + [
            "must protect employee salary information",
            "must comply with tax regulations",
            "must be processed securely"
        ],

        "keywords": DATA_KEYWORDS + [
            "payroll",
            "salary",
            "compensation"
        ]

    },

    ###########################################################################
    # BUDGET PLANNING
    ###########################################################################

    "Budget_Planning": {

        "title_templates": BUDGET_PLANNING_TITLES,
        "department": "Finance",
        "folder_name": "Finance",

        "security_domain": "Budget Planning",

        "owner": "Financial Planning Team",

        "classification": "Internal",

        "risk_level": "Medium",

        "document_prefix": "FIN-BUD",

        "documents_to_generate": 25,

        "actions": COMPLIANCE_ACTIONS,

        "objects": COMPLIANCE_OBJECTS + [
            "Annual Budget",
            "Department Budget",
            "Financial Forecast",
            "Capital Budget"
        ],

        "purposes": COMPLIANCE_PURPOSES,

        "rules": COMPLIANCE_RULES + [
            "must be reviewed quarterly",
            "must receive executive approval",
            "must align with business objectives"
        ],

        "keywords": COMPLIANCE_KEYWORDS + [
            "budget",
            "forecast",
            "planning"
        ]

    },

    ###########################################################################
    # FINANCIAL REPORTING
    ###########################################################################

    "Financial_Reporting": {

        "title_templates": FINANCIAL_REPORTING_TITLES,
        "department": "Finance",
        "folder_name": "Finance",

        "security_domain": "Financial Reporting",

        "owner": "Corporate Finance",

        "classification": "Confidential",

        "risk_level": "High",

        "document_prefix": "FIN-REP",

        "documents_to_generate": 25,

        "actions": COMPLIANCE_ACTIONS,

        "objects": COMPLIANCE_OBJECTS + [
            "Financial Report",
            "Balance Sheet",
            "Income Statement",
            "Cash Flow Statement"
        ],

        "purposes": COMPLIANCE_PURPOSES,

        "rules": COMPLIANCE_RULES + [
            "must comply with accounting standards",
            "must be approved before publication",
            "must be retained for regulatory audit"
        ],

        "keywords": COMPLIANCE_KEYWORDS + [
            "financial reporting",
            "accounting",
            "audit"
        ]

    }

}