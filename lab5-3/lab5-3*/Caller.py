class Caller:
    def __init__(self, base_address: any) -> None:
        self.base_address = base_address
        self.value = self.read_file("/Users/andrey/Documents/programs/lessons/test/memory_addresses.txt")
    
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
    def cmp_z(call_object, rax, rbx) -> str:
        if rax == rbx:
            return "Access Denied!"
        else:
            return call_object.__next__block__(call_object, rax-1, rbx+1) 
    
    @staticmethod
    def cmp_j(rax, rbx) -> str:
        if rax > rbx:
            return "Access Denied!"
        else:
            return "Access Granted!"
    
    @staticmethod
    def __next__block__(call_object, rax, rbx) -> str:
        rdx = rax * 5 + 1
        rdi, rsi = -1, 0
        rbx -= rdi + rsi - rdx
        return call_object.cmp_j(rax, rbx)
    
    @staticmethod
    def __call__access__(call_object, *args, **kwargs) -> str:
        stack = []
        rax = args[0] * 2
        r13, r14, r15 = 0, 1, 0
        stack.append(r13)
        stack.append(r14)
        stack.append(r15)
        rbx = args[len(args) - 1] % 100 + 1
        stack[0], stack[1] = rax, rax + rbx * 8
        ctn = 1
        stack[2] = ctn - stack[0] / stack[1]
        rbx = 0
        del stack[0], stack[1]
        r12 = int(call_object.value)
        stack.append(r12)
        rcx = args[kwargs["arg"]] - 1000 * stack[1] + stack[0]
        rcx -= -1
        rbx = rcx
        rcx = 0
        return call_object.cmp_z(call_object, rax, rbx)
