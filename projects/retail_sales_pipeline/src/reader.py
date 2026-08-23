def read_sales_data(file_path):
    with open(file_path, "r") as f1:
            
            header = next(f1)
            process_data= []
            for file in f1:
                  column = file.strip().split(",")
                  process_data.append(column)
            return(process_data)

