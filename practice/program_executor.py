import commands
import os

BaseDir = 'io_files/'

def file_exists(filename):
  if os.path.exists(filename):
    return True
  return False

# The result_code returned has the following meanings
# 0 : Program ran successfully and produced correct answer!
# 1 : Server Error
# 2 : Compilation Error
# 3 : Runtime Error
# 4 : Wrong Answer
# @param : source_code - input source code, multi line
# @param : question_id - integer, to identify input/output files
def execute_on(source_code, question_id):
  input_filename  = BaseDir + '%d.in' % question_id
  output_filename = BaseDir + '%d.out' % question_id
  
  # Step 0: Generate a file from the source code
  f = open('code.cpp', 'w')
  f.write(source_code)
  f.close()

  if not file_exists('code.cpp'):
    return 1, "Server Error: Source file not created!"
  if not file_exists(input_filename):
    return 1, "Server Error: Input file not found!"

  # Step 1: Compile the code
  cmd = "g++ code.cpp -o code"
  (status, output) = commands.getstatusoutput(cmd)
  if status:
    return 2, "Compilation error: " +output

  # Step 2: Run the code  
  cmd = "./code <%s >%s" % (input_filename, output_filename)
  (status, output) = commands.getstatusoutput(cmd)
  if status:
    return 3, "Runtime error: " + output
  
  # Step 3: Compare the outputs
  cmd = "diff %s %s" % (output_filename, output_filename + '.correct')
  (status, output) = commands.getstatusoutput(cmd)
  if status:
    return 4, "Wrong Answer!"
  return 0, "success!"

# Used to clean up the intermediate files generated during the process.
def cleanup(question_id):
  output_file = BaseDir + '%d.out' % question_id
  cmd = "rm code.cpp code " + output_file
  commands.getstatusoutput(cmd)

