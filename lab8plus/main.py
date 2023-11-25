addresses = []
    random_address = "\x60\x61\x62\x63\x64\x65"

    for _ in range(999):  # Generate 999 random addresses
        random_address = ''.join([chr(random.randint(0, 255)) for _ in range(6)])
        addresses.append(random_address)

    # Add the required address
    addresses.append("\x60\x61\x62\x63\x64\x65")

    # Create MemoryAddress instances for each address
    memory_addresses = [MemoryAddress(addr) for addr in addresses]

    # Create a dictionary to store random values associated with each address
    stack = {addr: memory_addr.generate_random_value() for addr, memory_addr in zip(addresses, memory_addresses)}

    # Save addresses and values to a text file
    with open('memory_addresses.txt', 'w') as file:
        for addr in addresses:
            file.write(f"{addr}-{stack[addr]}\n")

    print("Addresses and values saved to memory_addresses.txt")