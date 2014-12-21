# ------------------------------------------------------------
# plyRun.py
#
# Main
# version 3.0 for Markdown_python_compiler
# ------------------------------------------------------------
import plyYacc
import sys
from plyExport import html_head
from plyExport import html_tails


# Terminal command:
# python plyRun.py
# python plyRun.py <imported Markdown filename>
# python plyRun.py <imported Markdown filename> <Exported HTML filename>
commandlength = len(sys.argv)
if commandlength==1:
    Markdown_filename = "data.md"
    HTML_filename = "html_md.html"
elif commandlength==2:
    Markdown_filename = sys.argv[1]
    HTML_filename = "html_md.html"
else:
    Markdown_filename = sys.argv[1]
    HTML_filename = sys.argv[2]


# Get .md file data
# Open markdown file
markdown_input = open('./' + Markdown_filename)
try:
    data = markdown_input.read()
finally:
    markdown_input.close()
# Parse
parsing_result = plyYacc.yaccparse(data)
print "Parsing success"
# Add html heads and tails from plyExport.py
html_result = html_head + parsing_result +html_tails;

# Write to a html file
html_output = open('./'+HTML_filename, 'w')
try:
    html_output.write(html_result)
finally:
    html_output.close
    print "Exporting success"
