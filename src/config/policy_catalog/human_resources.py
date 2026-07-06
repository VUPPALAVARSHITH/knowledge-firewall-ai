from src.config.blueprints.human_resources import *
from src.config.title_templates.hr_titles import (
    LEAVE_MANAGEMENT_TITLES,
    EMPLOYEE_CONDUCT_TITLES,
    RECRUITMENT_TITLES,
    PERFORMANCE_MANAGEMENT_TITLES,
    EMPLOYEE_BENEFITS_TITLES
)

HUMAN_RESOURCE_POLICIES = {

    "Leave_Management": {

        "title_templates": LEAVE_MANAGEMENT_TITLES,
        "department": "Human Resources",
        "folder_name": "Human_Resources",

        "security_domain": "Leave Management",

        "owner": "HR Operations",

        "classification": "Internal",

        "risk_level": "Low",

        "document_prefix": "HR-LVE",

        "documents_to_generate": 25,

        "actions": HR_ACTIONS,

        "objects": HR_OBJECTS + [
            "Annual Leave",
            "Medical Leave",
            "Emergency Leave"
        ],

        "purposes": HR_PURPOSES,

        "rules": HR_RULES,

        "keywords": HR_KEYWORDS,
        
    },

    "Employee_Conduct": {

        "title_templates": EMPLOYEE_CONDUCT_TITLES,
        "department": "Human Resources",
        "folder_name": "Human_Resources",

        "security_domain": "Employee Conduct",

        "owner": "HR Compliance",

        "classification": "Internal",

        "risk_level": "Medium",

        "document_prefix": "HR-CON",

        "documents_to_generate": 25,

        "actions": HR_ACTIONS,

        "objects": HR_OBJECTS + [
            "Employee Behaviour",
            "Workplace Conduct",
            "Professional Ethics"
        ],

        "purposes": HR_PURPOSES,

        "rules": HR_RULES,

        "keywords": HR_KEYWORDS,
         },

    "Recruitment": {

        "title_templates": RECRUITMENT_TITLES,
        "department": "Human Resources",
        "folder_name": "Human_Resources",

        "security_domain": "Recruitment",

        "owner": "Talent Acquisition Team",

        "classification": "Internal",

        "risk_level": "Medium",

        "document_prefix": "HR-REC",

        "documents_to_generate": 25,

        "actions": HR_ACTIONS,

        "objects": HR_OBJECTS + [
            "Candidate",
            "Interview",
            "Job Application",
            "Hiring Process"
        ],

        "purposes": HR_PURPOSES,

        "rules": HR_RULES,

        "keywords": HR_KEYWORDS,
        
    },

    ###############################################################################
# PERFORMANCE MANAGEMENT
###############################################################################

"Performance_Management": {


    "title_templates": PERFORMANCE_MANAGEMENT_TITLES,
    "department": "Human Resources",

    "folder_name": "Human_Resources",

    "security_domain": "Performance Management",

    "owner": "HR Performance Team",

    "classification": "Internal",

    "risk_level": "Medium",

    "document_prefix": "HR-PRF",

    "documents_to_generate": 25,

    "actions": HR_ACTIONS,

    "objects": HR_OBJECTS + [

        "Performance Review",
        "Performance Rating",
        "Employee Goal",
        "Development Plan"

    ],

    "purposes": HR_PURPOSES + [

        "Improve employee performance."

    ],

    "rules": HR_RULES + [

        "must be conducted annually",

        "must include manager feedback",

        "must define measurable objectives"

    ],

    "keywords": HR_KEYWORDS + [

        "performance",

        "KPI",

        "review",

        "goals"

    ],
    
},

###############################################################################
# EMPLOYEE BENEFITS
###############################################################################

"Employee_Benefits": {


    "title_templates": EMPLOYEE_BENEFITS_TITLES,
    "department": "Human Resources",

    "folder_name": "Human_Resources",

    "security_domain": "Employee Benefits",

    "owner": "Benefits Administration Team",

    "classification": "Internal",

    "risk_level": "Low",

    "document_prefix": "HR-BEN",

    "documents_to_generate": 25,

    "actions": HR_ACTIONS,

    "objects": HR_OBJECTS + [

        "Health Insurance",

        "Retirement Plan",

        "Employee Benefit",

        "Wellness Program"

    ],

    "purposes": HR_PURPOSES + [

        "Support employee wellbeing."

    ],

    "rules": HR_RULES + [

        "must comply with organizational benefits policy",

        "must be communicated to employees",

        "must follow eligibility criteria"

    ],

    "keywords": HR_KEYWORDS + [

        "benefits",

        "insurance",

        "retirement",

        "wellness"

    ],
   
}

}