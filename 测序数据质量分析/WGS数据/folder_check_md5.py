import argparse
import os
from multiprocessing import Pool
# description参数可以用于描述脚本的参数作用，默认为空
parser=argparse.ArgumentParser(description="Check all subfolders\' md5 status within specified sequence data storage folder")
parser.add_argument('--folder','-f',help='Folder path of all your sequence data storage.')
parser.add_argument('--output_folder','-o',help='Output md5sum check results\' folder path.')
parser.add_argument('--output_result','-r',help='Output md5sum check results\' file name.')


args=parser.parse_args()

if not os.path.exists(args.output_folder):
    os.system(f"mkdir {args.output_folder}")


# execute md5sum check process via given MD5 file location
def md5Check(md5_file_loc, output_folder_loc):
    md5_folder_loc = os.path.split(md5_file_loc)[0]
    md5_file_name = os.path.split(md5_file_loc)[1]
    # change work dir
    os.chdir(md5_folder_loc)
    print(f"Start to calculate md5 values for files within {md5_folder_loc}")
    # get md5sum results
    md5sum_result = os.popen(f"md5sum -c {md5_file_name}").read()
    print(f"Start to write {md5_folder_loc} results to {output_folder_loc}")
    # write md5sum results
    with open(os.path.join(output_folder_loc, md5_file_name), 'w') as f:
        f.write(md5sum_result)
        f.close()

# perform fastqc quality assessment
def fastqc()


if __name__ == "__main__":

    md5_file_loc_list = []

    for root,dirs,files in os.walk(args.folder):
        # determine MD5 file location
        for file_name in files:
            if "MD5" in file_name:
                md5_file_loc_list.append(os.path.join(root, file_name))
    
    print('Parent process %s.' % os.getpid())
    p = Pool(5)
    for md5_file_loc in md5_file_loc_list:
        p.apply_async(md5Check, args=(md5_file_loc, args.output_folder, ))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
    
    # summarize single results
    with open(os.path.join(args.output_folder, args.output_result), 'w') as f:
        # open all result files
        md5_result_files = [open(os.path.join(args.output_folder, md5_result_name)) for md5_result_name in os.listdir(args.output_folder)]
        for md5_result_file in md5_result_files:
            f.write(md5_result_file.read())
            f.write("\n\n")
        # close all result files
        [md5_result_file.close() for md5_result_file in md5_result_files]
        f.close()




    

