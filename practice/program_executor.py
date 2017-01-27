import commands

def execute_on(source_code, input_filename, output_filename):
  # Generate the source code file
  f = open('code.cpp', 'w')
  f.write(source_code)
  f.close()

  cmd = "g++ code.cpp -o code"
  (status, output) = commands.getstatusoutput()
  print cmd, " returned ", status, " and printed ", output

if __name__ == '__main__':
  code = """
  #include <iostream>
  using namespace std;

  int main(){
    int a;
    cin>>a;
    cout<<a*2;
    return 0;
  }

  """
  execute_on(code, None, None)