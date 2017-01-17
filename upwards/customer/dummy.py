social_login = {
    "response": {
        "meta": {},
        "data": {
            "token": "4784_1a78c556660a403878754070537badfa",
            "customerId": "12345"}
    },
    "request": ["accessToken", "source", "sourceType"]
}

homepage = {
    "response": {
        "meta": {},
        "data": {
            "customer": {
                "firstName": "Alia",
                "lastName": "Sharma",
                "displayMessage": "Lets get you started Alia"
            },
            "forms": {
                "eligibilityAndCredit": {
                    "title": "Eligibility & Credit Limit Check",
                    "completedState": "PAN",
                    "result": {
                        "status": "eligible",
                        "message": "You are approved of a credit limit of 20,000 Rs"
                    }
                },
                "KYC": {
                    "title": "KYC & Document Upload",
                    "completedState": "AADHAAR",
                    "result": {
                        "status": "eligible/ineligible",
                        "message": "You are approved or a credit limit of 20000 Rs"
                    }
                }
            }
        }
    },
    "request": []
}
