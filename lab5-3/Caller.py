class Caller:
    def __init__(self, base_address: any) -> None:
        self.base_address = base_address
        self.value = self.read_file("/your_path/memory_addresses.txt")
    
    def read_file(self, file_path):
        result_dict = {}
        with open(file_path, 'r') as file:
            data = file.read()
            data = data.split("\n")
            for line in data:
                parts = line.strip().split("-")
                if len(parts) == 2:
                    key, value = parts
                    result_dict[key] = value
        if self.base_address in result_dict:
            print(result_dict[self.base_address])
            return result_dict[self.base_address]
        else:
            return f"No value found for key: {self.base_address}"
    
    @staticmethod
    def cmp_j(rax, rbx) -> str:
        if rbx == -1:
            return "RBX error!"
        if rax > rbx:
            return "Access Denied!"
        else:
            return "Access Granted!" 
    
    @staticmethod
    def __call__access__(call_object, *args, **kwargs) -> str:
        rax = args[0]
        rax *= -1
        r12 = 0
        rbx = args[len(args) - 1]
        rax *= rbx / 2
        rbx = 0.1
        r12 = int(call_object.value)
        rcx = -1 * 100 * (10 - args[kwargs["arg"]] + r12) / 80
        rbx *= rcx
        rcx = 0
        return call_object.cmp_j(rax, rbx)
