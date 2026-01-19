// Purpose: Contains all the prompts that the bot will use to interact with the user.

export const prompts = {
    system_prompt: "You are an experienced developer who knows the security vulnerability very well.",
    binary: `Classify the following code in vulnerable or not vulnerable. Output either only 'vulnerable' or 'not vulnerable'.`, 
    cwe: `
    Classify the following code in a CWE category. The code should have a vulnerability. 
    In addition, please provide an analysis of your classification in terms of the vulnerability.
    Below is the list of the top 25 CWEs that you could use to classify the code:
        
    CWE-787: Out-of-bounds Write
    CWE-79: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')
    CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')
    CWE-416: Use After Free
    CWE-78: Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')
    CWE-20: Improper Input Validation
    CWE-125: Out-of-bounds Read
    CWE-22: Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal')
    CWE-352: Cross-Site Request Forgery (CSRF)
    CWE-434: Unrestricted Upload of File with Dangerous Type
    CWE-862: Missing Authorization
    CWE-476: NULL Pointer Dereference
    CWE-287: Improper Authentication
    CWE-190: Integer Overflow or Wraparound
    CWE-502: Deserialization of Untrusted Data
    CWE-77: Improper Neutralization of Special Elements used in a Command ('Command Injection')
    CWE-119: Improper Restriction of Operations within the Bounds of a Memory Buffer
    CWE-798: Use of Hard-coded Credentials
    CWE-918: Server-Side Request Forgery (SSRF)
    CWE-306: Missing Authentication for Critical Function
    CWE-362: Concurrent Execution using Shared Resource with Improper Synchronization ('Race Condition')
    CWE-269: Improper Privilege Management
    CWE-94: Improper Control of Generation of Code ('Code Injection')
    CWE-863: Incorrect Authorization
    CWE-276: Incorrect Default Permissions.

    If you cannot see any vulnerability related to the above CWEs, return a CWE tag that you think is most relevant to the code.
    `,
};
