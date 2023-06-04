# make tss config file

#%%

for type in ['tss', 'tes']:

    file_list = open(f'{type}_list_of_files.txt').readlines()

    updated_file_list = []

    is_first = True

    for file_path in file_list:
        parts = file_path.split('/')
        last_part = parts[-1]
        updated_last_part = last_part.replace(f"_{type}.bed", "")
        if is_first:
            updated_file_path = file_path.strip() + f",True,True,{updated_last_part}"
            is_first = False
        else:
            updated_file_path = file_path.strip() + f",False,True,{updated_last_part}"
        updated_file_list.append(updated_file_path)

    with open(f'{type}_beds.txt', 'w') as ofile:
        for file_path in updated_file_list:
            ofile.write(file_path)
