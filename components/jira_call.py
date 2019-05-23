from jira import JIRA
from components.files.auth import jira_key

jira = JIRA('https://jira.egnyte-it.com', auth=jira_key)

issue = jira.issue('ESC-17609')
print (issue.fields.project.key)
print (issue.fields.issuetype.name)
print (issue.fields.reporter.displayName)