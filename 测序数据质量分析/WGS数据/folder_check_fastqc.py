import argparse
import os
# description参数可以用于描述脚本的参数作用，默认为空
parser=argparse.ArgumentParser(description="Check all subfolders\' fastq status within specified sequence data storage folder")
parser.add_argument('--folder','-f',help='Folder path of all your sequence data storage.')
parser.add_argument('--output_folder','-o',help='Output fastqc check results\' folder path.')


args=parser.parse_args()

threads = 80

if not os.path.exists(args.output_folder):
    os.system(f"mkdir {args.output_folder}")


if __name__ == "__main__":

    fq_file_loc_list = []

    for root,dirs,files in os.walk(args.folder):
        # determine fq.gz file location
        for file_name in files:
            if "fq.gz" in file_name:
                fq_file_loc_list.append(os.path.join(root, file_name))
    
    fastqc_files_cmd = " ".join(fq_file_loc_list)

    os.system(f"fastqc {fastqc_files_cmd} -o {args.output_folder} -t {threads}")



    

