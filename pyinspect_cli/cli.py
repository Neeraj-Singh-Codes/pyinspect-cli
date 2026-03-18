import sys
import os

def main():
    args = sys.argv[1:]
    
    if not args:
        print("Usage: pyinspect-cli <number> | pyinspect-cli list")
        sys.exit(1)
        
    cmd = args[0]
    
    # Get the directory of this file
    package_dir = os.path.dirname(os.path.abspath(__file__))
    modules_dir = os.path.join(package_dir, 'modules')
    
    if cmd == 'list':
        for i in range(1, 9):
            print(f"{i} - Module {i}")
        return

    if cmd.isdigit():
        module_num = int(cmd)
        if 1 <= module_num <= 8:
            file_name = f"m{module_num:02d}.py"
            file_path = os.path.join(modules_dir, file_name)
            
            if os.path.exists(file_path):
                with open(file_path, 'r') as f:
                    print(f.read())
            else:
                print(f"Error: Module file {file_name} not found.")
                sys.exit(1)
        else:
            print("Error: Please provide a module number between 1 and 8.")
            sys.exit(1)
    else:
        print(f"Error: Invalid command or module number '{cmd}'.")
        print("Usage: pyinspect-cli <number> | pyinspect-cli list")
        sys.exit(1)

if __name__ == "__main__":
    main()
