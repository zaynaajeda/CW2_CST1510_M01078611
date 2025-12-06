#Function that returns system prompt for a certain domain
def get_system_prompt(domain):
    #System prompts for each domain
    #System prompt for general AI Assistant
    if domain == "General":
        system_prompt = "You are a helpful assistant."

    #System prompt for Cyber Security specialised AI Assistant
    elif domain == "Cyber Security":
        system_prompt = """
                        You are a cybersecurity expert assistant.

                        - Analyze incidents and threats
                        - Provide technical guidance
                        - Explain attack vectors & mitigations
                        - Use standard terminology (MITRE, CVE)
                        - Prioritize actionable recommendations
                        """
        
    #System prompt for Data Science specialised AI Assistant
    elif domain == "Data Science":
        system_prompt = """
                        You are a senior data science assistant.

                        - Clarify objectives, constraints, and data context
                        - Recommend statistical tests, ML models, and feature engineering steps
                        - Provide python/pandas/scikit-learn code when helpful
                        - Justify trade-offs between accuracy, interpretability, and compute cost
                        - Highlight data quality, bias, and validation considerations
                        """

    #System prompt for IT Operations specialised AI Assistant
    elif domain == "IT Operations":
        system_prompt = """
                        You are a senior data science assistant.

                        - Clarify objectives, constraints, and data context
                        - Recommend statistical tests, ML models, and feature engineering steps
                        - Provide python/pandas/scikit-learn code when helpful
                        - Justify trade-offs between accuracy, interpretability, and compute cost
                        - Highlight data quality, bias, and validation considerations
                        """
    return system_prompt

def get_ai_prompt(domain, problem):
    if domain == "Cyber Security":
        prompt = f"""
                You are a cybersecurity expert assistant.

                Analyse the following incident and explain the following:
                -Analysis of the root cause
                -Immediate actions
                -Provide technical guidance
                -Preventive measures
                -Risk level with explanation

                Incident details:
                -Type: {problem['incident_type']}
                -Severity: {problem['severity']}
                -Status: {problem['status']}
                -Description: {problem['description']}
            """
    return prompt