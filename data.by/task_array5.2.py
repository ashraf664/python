import sys

def experiment(n):
    data = []
    data_size = sys.getsizeof(data) 
    
    print(f"Length: {len(data):3d}; Size in bytes: {data_size:4d}")
    
    for i in range(n):
        data.append(None)
        size = sys.getsizeof(data)
        
        if size != data_size:
            print(f"Length: {len(data):3d}; Size in bytes: {size:4d}")
            data_size = size


experiment(555)
